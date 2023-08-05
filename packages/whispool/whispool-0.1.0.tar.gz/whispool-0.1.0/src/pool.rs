use crate::whispool::{Input, WhispoolRust};
use colored::*;
use std::path::Path;
use std::sync::mpsc;
use std::sync::Arc;
use std::sync::Mutex;
use std::thread;
use uuid::Uuid;

type Job = Box<dyn FnOnce(Option<Arc<Mutex<WhispoolRust>>>, Input) + Send + 'static>;
type CleanJob = Box<dyn FnOnce(Option<Arc<Mutex<WhispoolRust>>>) + Send + 'static>;

enum Message {
    NewJob(Job, Input),
    Terminate,
    Last(CleanJob),
}

struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}

impl Worker {
    fn new(
        id: usize,
        receiver: Arc<Mutex<mpsc::Receiver<Message>>>,
        whispool: Option<Arc<Mutex<WhispoolRust>>>,
    ) -> Worker {
        let arc_in = whispool.unwrap();
        let arc_whis = Arc::clone(&arc_in);
        let thread_ = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv().unwrap();
            match message {
                Message::NewJob(job, input) => {
                    // println!("Worker {} got a job; executing.", id);
                    let whispool_dup = Some(Arc::clone(&arc_whis));
                    job(whispool_dup, input);
                }
                Message::Last(job) => {
                    let whispool_dup = Some(Arc::clone(&arc_whis));
                    job(whispool_dup);
                }
                Message::Terminate => {
                    println!(
                        "{}:\tWorker {} was told to terminate.",
                        "[TERMINATE]".magenta(),
                        id
                    );
                    break;
                }
            }
        });
        Worker {
            id: id,
            thread: Some(thread_),
        }
    }
}

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Message>,
}

impl ThreadPool {
    /// Create a new ThreadPool.
    ///
    /// The size is the number of threads in the pool.
    ///
    /// # Panics
    ///
    /// The `new` function will panic if the size is zero.
    pub fn new(size: usize, path: String) -> ThreadPool {
        assert!(size > 0);

        let mut workers = Vec::with_capacity(size);
        let (sender, receiver) = mpsc::channel();

        let receiver = Arc::new(Mutex::new(receiver));

        for id in 0..size {
            let path = path.clone();
            let uuid_sub_folder = Uuid::new_v4().to_string();
            let whispool_path = Path::new(&path)
                .join(uuid_sub_folder)
                .to_str()
                .unwrap()
                .to_string();
            let whispool = Arc::new(Mutex::new(WhispoolRust::new(whispool_path)));
            workers.push(Worker::new(id, Arc::clone(&receiver), Some(whispool)));
        }
        ThreadPool { workers, sender }
    }

    pub fn execute<F>(&self, f: F, ipt: Input)
    where
        F: FnOnce(Option<Arc<Mutex<WhispoolRust>>>, Input) + Send + 'static,
    {
        let job = Box::new(f);
        let res = self.sender.send(Message::NewJob(job, ipt));
        match res {
            Ok(_) => {}
            Err(e) => {
                println!("Execute Error: {}", e);
            }
        }
    }

    pub fn execute_last<F>(&self, f: F)
    where
        F: FnOnce(Option<Arc<Mutex<WhispoolRust>>>) + Send + 'static,
    {
        let job = Box::new(f);
        let res = self.sender.send(Message::Last(job));
        match res {
            Ok(_) => {}
            Err(e) => {
                println!("Execute Last Error: {}", e);
            }
        };
    }

    pub fn kill_all(&mut self) {
        for worker in &mut self.workers {
            println!("{}:\tShutting down worker {}","[SHUT DOWN]".magenta(), worker.id);

            if let Some(thread) = worker.thread.take() {
                // thread out of option, leaving none in place
                thread.join().unwrap();
            }
        }
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
        println!("{}:\tSending terminate to all workers.", "[DROP]".magenta());

        for _ in &self.workers {
            let res = self.sender.send(Message::Terminate);
            match res {
                Ok(_) => {}
                Err(e) => {
                    println!("{}:\tDrop Error: {}","ERROR".red(), e);
                }
            }
        }

        println!("{}:\tShutting down all workers.", "[DROPED]".magenta());
        self.kill_all()
    }
}
