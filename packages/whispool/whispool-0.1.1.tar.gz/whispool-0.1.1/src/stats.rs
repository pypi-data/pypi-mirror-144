use pyo3::prelude::*;
use std::collections::HashMap;

#[pyclass]
pub struct WordStats {
    #[pyo3(get)]
    pub word: String,
    #[pyo3(get)]
    pub total_occur: usize,
    #[pyo3(get)]
    pub match_count: usize,
    #[pyo3(get)]
    pub ratio: f32,
}

#[pymethods]
impl WordStats {
    #[new]
    pub fn new(word: &str, total_occur: usize, match_count: usize) -> WordStats {
        WordStats {
            word: word.to_string(),
            total_occur: total_occur,
            match_count: match_count,
            ratio: match_count as f32 / total_occur as f32,
        }
    }
}

impl Clone for WordStats {
    fn clone(&self) -> Self {
        WordStats {
            word: self.word.clone(),
            total_occur: self.total_occur,
            match_count: self.match_count,
            ratio: self.ratio,
        }
    }
}

#[pyclass]
pub struct StatsMap {
    #[pyo3(get)]
    pub stats: HashMap<String, WordStats>,
}

#[pymethods]
impl StatsMap {
    #[new]
    pub fn new() -> StatsMap {
        StatsMap {
            stats: HashMap::new(),
        }
    }
    pub fn extend(&mut self, word_stats: Vec<WordStats>) {
        for word_stat in word_stats.into_iter() {
            match self.stats.get_mut(&word_stat.word) {
                Some(word_stat_) => {
                    word_stat_.total_occur += word_stat.total_occur;
                    word_stat_.match_count += word_stat.match_count;
                    word_stat_.ratio =
                        word_stat_.match_count as f32 / word_stat_.total_occur as f32;
                }
                None => {
                    self.stats.insert(word_stat.word.clone(), word_stat);
                }
            }
        }
    }

    pub fn filter_min_total_occur(&mut self, min_total_occur: usize) {
        /*
        Filter out words with total occur less than min_total_occur
        */
        self.stats = self
            .stats
            .iter()
            .filter(|(_, word_stat)| word_stat.total_occur >= min_total_occur)
            .map(|(key, word_stat)| (key.clone(), word_stat.clone()))
            .collect();
    }
}
