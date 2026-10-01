# Python Lab

Small, self-contained experiments with Python features, libraries and backend concepts.

## Structure

```
python-lab/
|
├── language/
│   │
│   ├── iterators/  # iter() and next()
│   └── generators/ # yield, generator state
│
├── databases/
│   │
│   ├── sqlite/     # sqlite3 basics
│   └── psycopg2/   # Postgres connection
│
└── profiling/
    │
    └── cprofile/   # profile with cProfile, read results with pstats
```

## Running

Run scripts inside their own folder:

```sh
cd databases/sqlite
python init_db.py
```

## Dependencies

- **databases/psycopg2**: requires `psycopg2-binary` and **Postgres** running on `localhost:5433`

> Dependency management (`pyproject.toml` + **uv**) is planned.
