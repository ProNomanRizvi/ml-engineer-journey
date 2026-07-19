# Phase 4: SQL & Data Manipulation

Part of my ML Engineer self-learning roadmap. This phase is about learning
how to pull, clean, and analyze data — the real starting point of any ML
project. Split into SQL, NumPy, and Pandas.

**Duration:** 4 weeks | 4 hrs/day

---

## What's Inside
```
phase-4-sql-data-manipulation/
├── week1_sql/          ✅ Done
├── week2_numpy/        ✅ Done
├── week3_pandas/        ✅ Done
└── week4_project/       ⏳ Pending
```

---

## Week 1 — SQL (Completed)

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

## Week 2 — NumPy (Completed)

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

## Week 3 — Pandas (Completed)

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

## Coming Up

- **Week 4:** Final project — an ETL pipeline (SQL → Pandas → NumPy)

---

## Why This Matters

Most of the real work in ML is not building models — it's getting data
ready. This phase builds that foundation before touching any ML algorithm.