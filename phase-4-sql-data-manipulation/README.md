# Phase 4: SQL & Data Manipulation ✅ COMPLETE

Part of my ML Engineer self-learning roadmap. This phase is about learning
how to pull, clean, and analyze data — the real starting point of any ML
project. Split into SQL, NumPy, and Pandas.

**Duration:** 4 weeks | 4 hrs/day

---

## What's Inside
```
phase-4-sql-data-manipulation/
├── week1_sql/          ✅ Done
├── week2_numpy/         ✅ Done
├── week3_pandas/         ✅ Done
└── week4_project/         ✅ Done
```

---

## Week 1 — SQL

Learned SQL using SQLite with a small dummy database of students and
their course enrollments.

**Topics covered:**
- `SELECT` and `WHERE` — picking columns and filtering rows
- `GROUP BY`, `ORDER BY`, `HAVING` — grouping data and calculating averages/counts
- `INNER JOIN` and `LEFT JOIN` — combining two related tables
- Window Functions — `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `PARTITION BY`
- CTEs (`WITH` clause) — writing cleaner, step-by-step queries
- Subqueries — using a query's result inside another query (`IN`, `NOT IN`, comparing to `AVG`)

**Files:**
- `setup_database.py` — creates the sample database (`students` + `enrollments` tables)
- `basics.sql` — SELECT, WHERE, GROUP BY, ORDER BY, HAVING, JOINs
- `advanced.sql` — Window Functions, CTEs, Subqueries
- `notes.md` — my own notes explaining each concept in simple words

**How to run any file:**
```bash
python3 setup_database.py
sqlite3 -header -column data/students.db < basics.sql
```

---

## Week 2 — NumPy

Learned NumPy for fast, vectorized numerical operations — the foundation
for every ML math operation.

**Topics covered:**
- Arrays — creation methods and key attributes (`.shape`, `.dtype`, `.ndim`, `.size`)
- Vectorization — applying operations to a whole array instead of looping (tested and confirmed ~13x faster than a Python loop on 1 million elements)
- Broadcasting — doing math between differently-shaped arrays (scalar, row, and bidirectional stretching)
- Indexing & Slicing — basic, 2D, boolean, and fancy indexing
- Math Operations & Dot Product — `sqrt`, `mean`, `std`, and matrix multiplication (the core operation behind neural networks)

**Files:**
- `01_arrays.py` — array creation and attributes
- `02_vectorization.py` — vectorized operations and speed comparison
- `03_broadcasting.py` — scalar, row, and bidirectional broadcasting
- `04_indexing_slicing.py` — indexing, slicing, boolean and fancy indexing
- `05_math_dot_product.py` — math functions and matrix multiplication
- `notes.md` — my own notes explaining each concept in simple words

**How to run any file:**
```bash
python3 01_arrays.py
```

---

## Week 3 — Pandas

Learned Pandas for working with real-world, table-shaped data — cleaning
it, combining it, and summarizing it.

**Topics covered:**
- DataFrame creation, `loc` and `iloc` — building tables and selecting data by label or position
- `groupby`, `apply`/`lambda`, `pivot_table` — summarizing data by category
- Merge — combining two tables (`inner`, `left`, `right`, `outer`), same idea as SQL JOIN
- Data cleaning — handling missing values (`dropna`, `fillna`), duplicates, and messy text
- String operations & dtypes — cleaning text data and safely converting data types

**Files:**
- `01_dataframe_basics.py` — DataFrame creation, loc/iloc
- `02_loc_iloc_groupby.py` — groupby, apply/lambda, pivot_table
- `03_merge_pivot.py` — merge deep dive (inner, left, right, outer)
- `04_data_cleaning.py` — missing values, duplicates, string cleanup
- `05_string_operations.py` — string operations and dtype conversions
- `notes.md` — my own notes explaining each concept in simple words

**How to run any file:**
```bash
python3 01_dataframe_basics.py
```

---

## Week 4 — ETL Project (Final Project)

Combined everything from the previous three weeks into one real,
working pipeline — the same workflow used in real data engineering and
ML projects.

**Pipeline stages:**
- **Extract** — pull raw data from a SQLite database into a Pandas DataFrame
- **Transform** — clean messy text, fill missing values (category-aware), remove duplicates
- **Analyze** — use NumPy to calculate revenue, averages, and highest values
- **Load** — save the final clean, analyzed data into a CSV report

**Files:**
- `create_source_db.py` — builds a deliberately messy sample database
- `etl_pipeline.py` — the full 4-stage ETL pipeline
- `data/output/final_report.csv` — the final cleaned and analyzed result
- `README.md` — project-specific write-up
- `notes.md` — my own notes on the ETL process

**How to run:**
```bash
python3 create_source_db.py
python3 etl_pipeline.py
```

---

## Why This Phase Mattered

Most of the real work in ML is not building models — it's getting data
ready. This phase built that foundation: pulling data with SQL, doing
fast numerical work with NumPy, and cleaning/shaping real-world data
with Pandas — then proving it all works together in one pipeline.