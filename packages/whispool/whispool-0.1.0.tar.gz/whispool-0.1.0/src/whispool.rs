use pyo3::prelude::*;
use pyo3::types::PyType;
use std::collections::HashMap;
use std::fs::{create_dir, read_dir, File};
use std::io::prelude::*;
use std::path::Path;

use crate::pool::ThreadPool;
use crate::stats::{StatsMap, WordStats};
use crate::utils::id_in_ids;

// use scoped_threadpool::Pool;
use std::sync::mpsc;
use std::sync::Arc;
use std::sync::Mutex;

use colored::*;
use uuid::Uuid;

pub struct Input {
    sentence: Vec<String>,
    info: Vec<String>,
}

#[pyclass]
pub struct Word {
    /*
    Basic unit for vacabulary
    */
    #[pyo3(get)]
    pub word: String,
    #[pyo3(get)]
    pub belongs: HashMap<usize, usize>, /*Sentence id to count*/
    #[pyo3(get)]
    pub word_id: usize,
}

#[pymethods]
impl Word {
    #[new]
    pub fn new(word: String, word_id: usize) -> Word {
        Word {
            word,
            belongs: HashMap::new(), /*belongs to which sentence*/
            word_id,
        }
    }

    pub fn occur_in(&mut self, piece_id: usize) {
        if self.belongs.contains_key(&piece_id) {
            *self.belongs.get_mut(&piece_id).unwrap() += 1;
        } else {
            self.belongs.insert(piece_id, 1);
        }
    }

    pub fn save_belongs(&self) -> String {
        /*Format belongs to json string*/
        let mut result_vec: Vec<String> = vec![];
        for (key, value) in self.belongs.iter() {
            result_vec.push(format!("{}:{}", key, value));
        }
        result_vec.join("|")
    }

    pub fn load_belongs(&mut self, belongs: String) {
        /*Format belongs to json string*/
        let belongs_vec: Vec<&str> = belongs.split("|").collect();
        for i in 0..belongs_vec.len() {
            let belongs_pair: Vec<&str> = belongs_vec[i].split(":").collect();
            let key: usize = belongs_pair[0].parse().unwrap();
            let value: usize = belongs_pair[1].parse().unwrap();
            self.belongs.insert(key, value);
        }
    }

    pub fn total_occur(&self) -> usize {
        let mut total_occur: usize = 0;
        for (_, value) in self.belongs.iter() {
            total_occur += value;
        }
        total_occur
    }
}

impl std::clone::Clone for Word {
    fn clone(&self) -> Self {
        Word {
            word: self.word.clone(),
            belongs: self.belongs.clone(),
            word_id: self.word_id,
        }
    }
}

#[pyclass]
pub struct WordMap {
    #[pyo3(get)]
    word_map: HashMap<String, usize>,
    #[pyo3(get)]
    word_vec: Vec<Word>,
}

#[pymethods]
impl WordMap {
    #[new]
    pub fn new() -> WordMap {
        WordMap {
            word_map: HashMap::new(),
            word_vec: Vec::new(),
        }
    }

    pub fn add_word<'b>(&mut self, word_string: &str) -> usize {
        let word_id = self.word_vec.len();
        let word = Word::new(word_string.to_string(), word_id);
        self.word_vec.push(word);
        self.word_map.insert(word_string.to_string(), word_id);
        word_id
    }

    pub fn get_word_id(&mut self, word_string: &str) -> usize {
        match self.word_map.get(word_string) {
            Some(word_id) => *word_id,
            None => self.add_word(word_string),
        }
    }

    pub fn save(&self, filename: &str) {
        let mut file = File::create(filename).unwrap();
        let mut all_data = vec![];
        for word in &self.word_vec {
            let line = vec![
                word.word.to_owned(),
                word.word_id.to_string(),
                word.save_belongs(),
            ];
            all_data.push(line);
        }
        // save all data to json file
        let data = serde_json::to_string(&all_data).unwrap();
        let res = file.write(data.as_bytes());
        match res {
            Ok(_) => {
                println!("{}\tword map saved","[SAVE]".green())
            }
            Err(e_) => println!("Failed to save!:{:?}", e_),
        }
    }

    #[staticmethod]
    pub fn load(filename: &str) -> Self {
        let mut word_map = WordMap::new();
        let mut file = File::open(filename).unwrap();
        let mut contents = String::new();
        file.read_to_string(&mut contents).unwrap();
        let lines = serde_json::from_str::<Vec<Vec<String>>>(&contents).unwrap();
        for i in 0..lines.len() {
            // a single line to a vector
            let line_vec = &lines[i];
            let word_string = &line_vec[0];
            let word_id: usize = line_vec[1].parse().unwrap();
            let belongs = &line_vec[2];

            let mut word = Word::new(word_string.to_string(), word_id);
            word.load_belongs(belongs.to_string());
            word_map.word_vec.push(word);
            word_map.word_map.insert(word_string.to_string(), word_id);
        }
        word_map
    }
}

impl std::clone::Clone for WordMap {
    fn clone(&self) -> Self {
        WordMap {
            word_map: self.word_map.clone(),
            word_vec: self.word_vec.clone(),
        }
    }
}

#[pyclass]
pub struct Piece {
    /*Piece is something to hold ids*/
    #[pyo3(get, set)]
    info: Vec<String>,
    #[pyo3(get)]
    mentions: HashMap<usize, usize>, //word id, count
    #[pyo3(get)]
    piece_id: usize,
}

impl Piece {
    pub fn check_info_vec(&self, info_vec: &Vec<Option<String>>) -> bool {
        /*
        Check if this is the piece meets the set criteria
        */
        for (crit_, data) in info_vec.iter().zip(&self.info) {
            if crit_.is_some() {
                if data != crit_.as_ref().unwrap() {
                    return false;
                }
            }
        }
        true
    }
}

#[pymethods]
impl Piece {
    #[new]
    pub fn new(info: Vec<String>, piece_id: usize) -> Piece {
        Piece {
            info,
            mentions: HashMap::new(),
            piece_id,
        }
    }

    pub fn mention_word(&mut self, word_id: usize) {
        if self.mentions.contains_key(&word_id) {
            *self.mentions.get_mut(&word_id).unwrap() += 1;
        } else {
            self.mentions.insert(word_id, 1);
        }
    }

    pub fn has_words(&self, word_map: &WordMap) -> Vec<String> {
        /*
        Return a list of strings
        */
        self.mentions
            .iter()
            .map(|(word_id, _count)| {
                let word = word_map.word_vec[*word_id].word.clone();
                word
            })
            .collect()
    }

    pub fn save_mentions(&self) -> String {
        /*Format mentions to json string*/
        let mut result_vec: Vec<String> = vec![];
        for (key, value) in self.mentions.iter() {
            result_vec.push(format!("{}:{}", key, value));
        }
        result_vec.join("|")
    }

    pub fn load_mentions(&mut self, mentions: String) {
        /*Format mentions to json string*/
        let mentions_vec: Vec<&str> = mentions.split("|").collect();
        for i in 0..mentions_vec.len() {
            let mentions_pair: Vec<&str> = mentions_vec[i].split(":").collect();
            let key: usize = mentions_pair[0].parse().unwrap();
            let value: usize = mentions_pair[1].parse().unwrap();
            self.mentions.insert(key, value);
        }
    }

    pub fn save_info(&self) -> String {
        /*Format info to json string*/
        let mut result_vec: Vec<String> = vec![];
        for i in 0..self.info.len() {
            result_vec.push(format!("{}", self.info[i]));
        }
        result_vec.join("|")
    }

    pub fn load_info(&mut self, info: String) {
        /*Format info to json string*/
        let info_vec: Vec<&str> = info.split("|").collect();
        for i in 0..info_vec.len() {
            self.info.push(info_vec[i].to_string());
        }
    }
}

impl std::clone::Clone for Piece {
    fn clone(&self) -> Self {
        Piece {
            info: self.info.clone(),
            mentions: self.mentions.clone(),
            piece_id: self.piece_id,
        }
    }
}

#[pyclass]
pub struct PieceMap {
    #[pyo3(get)]
    piece_map: HashMap<String, usize>,
    #[pyo3(get)]
    piece_vec: Vec<Piece>,
}

#[pymethods]
impl PieceMap {
    #[new]
    pub fn new() -> PieceMap {
        PieceMap {
            piece_map: HashMap::new(),
            piece_vec: Vec::new(),
        }
    }

    pub fn add_piece(&mut self, piece_info: Vec<String>) -> usize {
        // create key for piece
        let piece_key = piece_info.join("-");
        let piece_id = self.piece_vec.len();
        let piece = Piece::new(piece_info, piece_id);
        self.piece_vec.push(piece);
        self.piece_map.insert(piece_key, piece_id);
        piece_id
    }

    pub fn get_piece_id(&mut self, piece_info: Vec<String>) -> usize {
        let piece_key = piece_info.join("-");
        match self.piece_map.get(&piece_key) {
            Some(piece_id) => *piece_id,
            None => self.add_piece(piece_info),
        }
    }

    pub fn save(&self, filename: &str) {
        let mut file = File::create(filename).unwrap();
        let mut all_data = vec![];
        for piece in &self.piece_vec {
            let line = vec![
                piece.save_info(),
                piece.piece_id.to_string(),
                piece.save_mentions(),
            ];
            all_data.push(line);
        }
        let data = serde_json::to_string(&all_data).unwrap();
        let res = file.write(data.as_bytes());
        match res {
            Ok(_) => {
                // println!("[PIECE]Successfully saved!")
            }
            Err(e_) => println!("Failed to save!:{:?}", e_),
        }
    }

    #[staticmethod]
    pub fn load(filename: &str) -> Self {
        let mut piece_map = PieceMap::new();
        let mut file = File::open(filename).unwrap();
        let mut contents = String::new();
        file.read_to_string(&mut contents).unwrap();
        let lines = serde_json::from_str::<Vec<Vec<String>>>(&contents).unwrap();
        for i in 0..lines.len() {
            // a single line to a vector
            let line_vec = &lines[i];

            let piece_info_string = &line_vec[0];
            let piece_id: usize = line_vec[1].parse().unwrap();
            let mentions = &line_vec[2];

            let mut piece_info: Vec<String> = vec![];
            let info_vec: Vec<&str> = piece_info_string.split("|").collect();
            for i in 0..info_vec.len() {
                piece_info.push(info_vec[i].to_string());
            }
            let mut piece = Piece::new(piece_info, piece_id);
            piece.load_mentions(mentions.to_string());
            piece_map.piece_vec.push(piece);
            piece_map
                .piece_map
                .insert(piece_info_string.to_string(), piece_id);
        }
        piece_map
    }
}

impl std::clone::Clone for PieceMap {
    fn clone(&self) -> Self {
        PieceMap {
            piece_map: self.piece_map.clone(),
            piece_vec: self.piece_vec.clone(),
        }
    }
}

#[pyclass]
pub struct WhispoolRust {
    #[pyo3(get)]
    word_map: WordMap,
    #[pyo3(get)]
    piece_map: PieceMap, // to find a sentece
    save_dir: String,
}

#[pymethods]
impl WhispoolRust {
    #[new]
    pub fn new(save_dir: String) -> WhispoolRust {
        WhispoolRust {
            word_map: WordMap::new(),
            piece_map: PieceMap::new(),
            save_dir: save_dir,
        }
    }

    pub fn match_sentence(&mut self, word: Vec<String>, piece_info: Vec<String>) {
        let piece_id = self.piece_map.get_piece_id(piece_info);
        for word_string in word {
            let word_id = self.word_map.get_word_id(&word_string);
            self.piece_map.piece_vec[piece_id].mention_word(word_id);
            self.word_map.word_vec[word_id].occur_in(piece_id);
        }
    }

    pub fn save(&self) {
        /*
        Save Whispool to directory
        */
        // check if directory exists
        if !Path::new(&self.save_dir).exists() {
            create_dir(&self.save_dir).unwrap();
        }
        let word_map_path = Path::new(&self.save_dir).join("word_map.json");
        let piece_map_path = Path::new(&self.save_dir).join("piece_map.json");
        self.word_map.save(word_map_path.to_str().unwrap());
        self.piece_map.save(piece_map_path.to_str().unwrap());
    }

    #[classmethod]
    pub fn from(_cls: &PyType, directory: &str) -> Self {
        /*
        Load Whispool from directory
        */
        let mut whispool = WhispoolRust::new(directory.to_string());
        let word_map_path = Path::new(directory).join("word_map.json");
        let piece_map_path = Path::new(directory).join("piece_map.json");
        whispool.word_map = WordMap::load(word_map_path.to_str().unwrap());
        whispool.piece_map = PieceMap::load(piece_map_path.to_str().unwrap());
        whispool
    }

    pub fn load(&mut self) {
        let word_map_path = Path::new(&self.save_dir).join("word_map.json");
        let piece_map_path = Path::new(&self.save_dir).join("piece_map.json");
        self.word_map = WordMap::load(word_map_path.to_str().unwrap());
        self.piece_map = PieceMap::load(piece_map_path.to_str().unwrap());
        println!(
            "{}:\tfrom {:?}, size:{:?}","[LOAD PIECE]".yellow(),
            &self.save_dir,
            self.piece_map.piece_vec.len()
        );
        println!(
            "{}:\tfrom {:?}, size:{:?}","[LOAD WORD]".yellow(),
            &self.save_dir,
            self.word_map.word_vec.len()
        );
    }

    pub fn calc_info(&self, info_vec: Vec<Option<String>>) -> Vec<WordStats> {
        /* Finds the ids meet the criteria */
        let mut piece_ids: Vec<usize> = Vec::new();

        for piece in &self.piece_map.piece_vec {
            if piece.check_info_vec(&info_vec) {
                piece_ids.push(piece.piece_id);
            }
        }
        // sort piece_ids in ascending order
        piece_ids.sort();

        let mut rt: Vec<WordStats> = vec![];
        for word in &self.word_map.word_vec {
            let mut match_ct: usize = 0;
            for (piece_id, piece_ct) in word.belongs.iter() {
                if id_in_ids(*piece_id, &piece_ids) {
                    match_ct += *piece_ct;
                }
            }
            rt.push(WordStats::new(&word.word, word.total_occur(), match_ct));
        }
        rt
    }

    pub fn piece_count(&self) -> usize {
        self.piece_map.piece_vec.len()
    }

    pub fn calc_from_directory(
        &mut self,
        directory: &str,
        info_vec: Vec<Option<String>>,
    ) -> Vec<WordStats> {
        self.reset_to(directory.to_string());
        self.load();
        let res = self.calc_info(info_vec);
        self.piece_map = PieceMap::new();
        self.word_map = WordMap::new();
        res
    }
}

impl WhispoolRust {
    pub fn reset_to(&mut self, save_dir: String) {
        self.save_dir = save_dir;
        self.word_map = WordMap::new();
        self.piece_map = PieceMap::new();
    }
}

#[pyclass]
pub struct WhispoolMulti {
    /*
    Multiple Thread Whispool
    */
    path: String,
    threads: usize,
    max_pieces_each: usize,
    thread_pool: ThreadPool,
}

fn new_whispool_path(path: &Arc<String>) -> String {
    /*A new path to store whispool data*/
    let uuid_sub_folder = Uuid::new_v4().to_string();
    Path::new(path.as_ref())
        .join(uuid_sub_folder)
        .to_str()
        .unwrap()
        .to_string()
}

#[pymethods]
impl WhispoolMulti {
    #[new]
    pub fn new(path: &str, threads: usize, max_pieces_each: usize) -> WhispoolMulti {
        let thread_pool = ThreadPool::new(threads, path.to_string());
        //create path if not exist
        if !Path::new(path).exists() {
            create_dir(path).unwrap();
        }
        WhispoolMulti {
            path: path.to_string(),
            threads: threads,
            max_pieces_each: max_pieces_each,
            thread_pool: thread_pool,
        }
    }

    pub fn consume(&self, sentences: Vec<Vec<String>>, infos: Vec<Vec<String>>) {
        let max_pieces_each = self.max_pieces_each;
        let path = Arc::new(self.path.clone());
        for (sentence, info) in sentences.into_iter().zip(infos) {
            let ipt = Input {
                sentence: sentence,
                info: info,
            };
            let path = Arc::clone(&path);
            self.thread_pool.execute(
                move |whispool: Option<Arc<Mutex<WhispoolRust>>>, input: Input| {
                    let whis = whispool.as_ref().unwrap();

                    if whis.lock().unwrap().piece_count() > max_pieces_each {
                        whis.lock().unwrap().save();
                        println!("{}\tsave to file:{}","[CLOSE]".green(), whis.lock().unwrap().save_dir);
                        /* reset the whispool if one whispool is full
                         */
                        let whispool_path = new_whispool_path(&path);
                        whis.lock().unwrap().reset_to(whispool_path);
                    }
                    whispool
                        .as_ref()
                        .unwrap()
                        .lock()
                        .unwrap()
                        .match_sentence(input.sentence, input.info);
                },
                ipt,
            );
        }
    }

    pub fn flush_residual(&mut self) {
        for _ in 0..self.threads {
            self.thread_pool
                .execute_last(|whispool: Option<Arc<Mutex<WhispoolRust>>>| {
                    if whispool.as_ref().unwrap().lock().unwrap().piece_count() > 0 {
                        whispool.unwrap().as_ref().lock().unwrap().save();
                    }
                });
        }
    }

    pub fn join_all(&mut self) {
        self.thread_pool.kill_all();
    }

    pub fn reset_thread_pool(&mut self) {
        self.thread_pool = ThreadPool::new(self.threads, self.path.clone());
    }

    pub fn final_stats(&mut self, infos: Vec<Option<String>>, min_total_occur: usize) -> StatsMap {
        println!("{}:\t{}", "[FINAL STATS]".cyan(), &self.path);
        self.flush_residual();
        self.reset_thread_pool();
        /*Collecting back results*/
        let sub_dirs: Vec<String> = read_dir(&self.path)
            .unwrap()
            .map(|dir| dir.unwrap().path().to_str().unwrap().to_string())
            .collect();
        println!("{}:\t{:?}", "[SUB DIRS]".cyan(), &sub_dirs);
        let arc_info = Arc::new(infos);
        // make sure there is no residual data
        let (tx, rx) = mpsc::channel();
        for dir in &sub_dirs {
            let arc_dir = Arc::new(dir.clone());
            let thread_info = Arc::clone(&arc_info);
            let txc = tx.clone();
            self.thread_pool.execute(
                move |whispool: Option<Arc<Mutex<WhispoolRust>>>, _input: Input| {
                    let folder_result = whispool
                        .as_ref()
                        .unwrap()
                        .lock()
                        .unwrap()
                        .calc_from_directory(
                            arc_dir.as_ref(),
                            thread_info.as_ref().to_vec().clone(),
                        );

                    println!("{}:\t{}", "[RESULT LENGTH]".cyan(), folder_result.len());

                    let sent = txc.send(folder_result);
                    match sent {
                        Ok(_) => {}
                        Err(e) => {
                            println!("{}:\tSending Back Thread Result: {}", "[ERROR]".red(), e);
                        }
                    }
                },
                Input {
                    sentence: vec![],
                    info: vec![],
                },
            );
        }
        // wait for threads to finish
        self.reset_thread_pool();
        // collect result
        let mut stats_map = StatsMap::new();
        loop {
            match rx.try_recv() {
                Ok(m) => {
                    println!("{}:\t{} words", "[MERGE]".blue(), m.len());
                    stats_map.extend(m)
                }
                Err(_e) => {
                    // println!("Receiver End");
                    break;
                }
            }
        }
        println!("{}:\t{}","[WORDS]".cyan(), stats_map.stats.len());
        if min_total_occur > 0 {
            stats_map.filter_min_total_occur(min_total_occur);
            println!("{}:\t{} (after filter)","[WORDS]".cyan(), stats_map.stats.len());
        }

        stats_map
    }
}
