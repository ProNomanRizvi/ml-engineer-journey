# Week 4: ETL Pipeline Project

Final project for Phase 4 — combines everything learned across SQL,
NumPy, and Pandas into one real, working pipeline.

**Goal:** Extract raw data from a database, clean it, analyze it
numerically, and save the final result — the same workflow used in
real data engineering and ML projects.

---

## What's Inside
```
week4_project/
├── create_source_db.py     ← builds a messy sample sales database
├── etl_pipeline.py           ← the full ETL pipeline
├── data/
│   ├── source.db              ← generated database (messy, on purpose)
│   └── output/
│       └── final_report.csv    ← cleaned + analyzed final result
└── README.md
```

---

## The Pipeline — 4 Stages

**1. Extract**
Connects to the SQLite database and pulls the raw `sales` table
directly into a Pandas DataFrame using `pd.read_sql_query()`.

**2. Transform**
Cleans the messy raw data:
- Standardizes text (extra spaces, inconsistent casing like
  "electronics" vs "Electronics")
- Fills missing prices using the average price of that product's
  category (not just the overall average)
- Fills missing quantities with 0
- Removes duplicate records

**3. Analyze**
Uses NumPy to calculate key numbers from the cleaned data:
- Revenue per product (price × quantity)
- Total revenue
- Average price
- Highest single revenue

**4. Load**
Saves the final cleaned and analyzed data to
`data/output/final_report.csv`.

---

## How to Run

```bash
python3 create_source_db.py
python3 etl_pipeline.py
```

Check the result:
```bash
cat data/output/final_report.csv
```

---

## What This Project Proves

Real data is never clean — this project starts from deliberately messy
data (inconsistent text, missing values, duplicates) and turns it into
a trustworthy, analysis-ready report, using the exact same three tools
(SQL, Pandas, NumPy) covered earlier in this phase.