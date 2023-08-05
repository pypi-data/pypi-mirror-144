mod utils;
mod stats;
mod pool;
mod whispool;
use pyo3::prelude::*;
use whispool::*;
use stats::{WordStats,StatsMap};

/*
This main is basicly setup to load rust modules to python modules
*/
#[pymodule]
fn whispool(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Word>()?;
    m.add_class::<WordMap>()?;
    m.add_class::<Piece>()?;
    m.add_class::<PieceMap>()?;
    m.add_class::<WhispoolRust>()?;
    m.add_class::<WhispoolMulti>()?;
    m.add_class::<WordStats>()?;
    m.add_class::<StatsMap>()?;

    Ok(())
}

pub fn main() {

}
