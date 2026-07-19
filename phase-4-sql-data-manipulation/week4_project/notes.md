# Phase 4 - Week 4: ETL Pipeline Notes

## What is ETL?

ETL stands for Extract, Transform, Load — the standard workflow for
turning raw data into something usable.

- **Extract** — pull raw data from its source (a database, CSV, API, etc.)
- **Transform** — clean and reshape that data so it's actually trustworthy
- **Load** — save the final result somewhere useful (a new table, CSV, report)

This is the real starting point of almost every data or ML project —
before any model gets built, the data has to go through this process.

---

## Extract

Used `pd.read_sql_query()` to run a SQL query directly against a SQLite
database and get the result back as a Pandas DataFrame in one line —
no manual looping through rows needed.

```python
df = pd.read_sql_query("SELECT * FROM sales", conn)
```

---

## Transform

This is where most of the real work happens, because raw data is
usually messy. I cleaned:

- **Inconsistent text** — things like "electronics", "Electronics", and
  "STATIONERY" all needed to become one consistent format, using
  `.str.strip()` and `.str.title()`
- **Missing prices** — instead of filling every missing price with one
  overall average, I filled it with the average price of that specific
  product's category, using `groupby(...).transform("mean")`. This
  gives a much more accurate fill than a flat average would.
- **Missing quantities** — filled with 0
- **Duplicates** — removed exact duplicate sales records, while
  ignoring the `id` column (since two different IDs can still describe
  the same real sale)

---

## Analyze (NumPy)

Once the data was clean, I used NumPy to pull out actual insights:

- Calculated a new `revenue` column (price × quantity)
- `np.sum()` — total revenue across all sales
- `np.mean()` — average price
- `np.max()` — the single highest revenue made

This is the step where cleaned data actually becomes useful information.

---

## Load

Saved the final cleaned and analyzed DataFrame into a CSV file using
`df.to_csv()`, so the result can be opened, shared, or used elsewhere
without needing to rerun the whole pipeline.

---

## Key Lessons From This Project

- **Never hardcode a personal file path.** I originally used an
  absolute path like `/home/username/...`, which only works on my own
  machine. Fixed it using `os.path.dirname(os.path.abspath(__file__))`
  so the pipeline finds its own files no matter which machine or folder
  it's run from.
- **Splitting the pipeline into separate functions** (extract,
  transform, analyze, load) made it much easier to test and debug each
  stage on its own, instead of one giant block of code.
- **Category-aware filling** (filling missing prices per category
  instead of overall) produces more realistic results than a single
  global average would.
- Wrapping the whole pipeline in `try/except` means one bad file or
  broken connection gives a clear error message instead of crashing
  with a confusing traceback.

---

## Overall Week 4 Summary

This project connected everything from the phase:
- **SQL** to pull the raw data out of a database
- **Pandas** to clean and reshape it into something trustworthy
- **NumPy** to calculate real numbers from it
- A final CSV to hold the finished, usable result

This is the actual shape of real-world data work — most of the effort
goes into steps 1-3 before any ML model ever sees the data.