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
├── week2_numpy/        🔜 Next
├── week3_pandas/        ⏳ Pending
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

## Coming Up

- **Week 2:** NumPy — arrays, vectorization, broadcasting, math operations
- **Week 3:** Pandas — DataFrames, cleaning, merging, groupby
- **Week 4:** Final project — an ETL pipeline (SQL → Pandas → NumPy)

---

## Why This Matters

Most of the real work in ML is not building models — it's getting data
ready. This phase builds that foundation before touching any ML algorithm.