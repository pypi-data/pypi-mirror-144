# Whispool
> Fast in memory word frequency count, with Rust

## Installation
```shell
pip install whispool
```

## Basic usage
We assume we have n sentences, with each sentence broken into words. And each sentence is 
```python
sentence = [
            ['This', 'is', 'a', 'sentence'],
            ['This', 'is', 'another', 'sentence'],
            ['This', 'is', 'a', 'third', 'sentence'],
            ...
        ]
info = list([
            ['id1', 'category1', 'sci-fi', 'movie','Jan.'],
            ['id2', 'category1', 'romance', 'movie','Jan.'],
            ['id3', 'category2', 'sci-fi', 'tv','Feb.'],
            ...
        ])

```

## Build from rust
```shell
maturin build --release
```