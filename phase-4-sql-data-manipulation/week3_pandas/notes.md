# Phase 4 - Week 3: Pandas Notes

## Topic 1: DataFrame Creation, loc & iloc

A DataFrame is like an Excel sheet inside Python — rows and named
columns. It can be built from a dictionary, a list of lists, or read
directly from a CSV file.

Useful methods to explore a DataFrame:
- `.head()` - first few rows
- `.tail(n)` - last n rows
- `.info()` - column names, types, and non-null counts
- `.describe()` - statistics (mean, min, max, etc.) for numeric columns

**loc** finds data by label/name. **iloc** finds data by position
(like a list index), ignoring whatever the labels are.

With the default index (0,1,2...), loc and iloc give the same result.
But once you set a custom index (like using names as the index), loc
needs the actual label ("Sara"), while iloc still just uses position
(0, 1, 2...).

Slicing is different too: `loc[0:2]` includes both ends, but `iloc[0:2]`
excludes the last one — same as normal Python list slicing.

---

## Topic 2: groupby, apply/lambda, pivot_table

`groupby` groups rows by a shared value and lets you calculate something
per group, like average GPA per department. This is basically Pandas'
version of SQL's GROUP BY.

`apply()` with a `lambda` runs a small custom function on every value in
a column. I used it to convert GPA into a percentage.

`pivot_table` does something similar to groupby, but returns a cleaner,
more flexible summary table. The math result is the same either way —
groupby returns a Series, pivot_table returns a full DataFrame.

---

## Topic 3: Merge (Inner, Left, Right, Outer)

Merge combines two DataFrames based on a shared column — this is
Pandas' version of SQL JOIN.

- **inner** — only keeps rows that match in both DataFrames
- **left** — keeps all rows from the left DataFrame, fills missing
  matches with NaN
- **right** — keeps all rows from the right DataFrame, fills missing
  matches with NaN
- **outer** — keeps everything from both sides, matched or not

I tested this with students and enrollments data. A student with no
enrollment disappeared in inner merge but stayed (with NaN) in left
merge. An enrollment with no matching student disappeared in inner but
stayed in right merge. Outer merge showed all of it at once — it always
has the most rows because it combines everything.

---

## Topic 4: Data Cleaning

Real data is often messy — missing values, duplicates, extra spaces.

- `.isnull().sum()` — counts missing values per column
- `.dropna()` — removes rows that have any missing value
- `.fillna(value)` — replaces missing values with something, like the
  column's mean or a fixed number
- `.duplicated()` — flags rows that are exact duplicates
- `.drop_duplicates()` — removes those duplicate rows
- `.str.strip()` — removes extra spaces around text
- `.str.upper()` — converts text to uppercase

Important habit: always work on a `.copy()` of the DataFrame when
testing different cleaning steps, so the original data doesn't get
accidentally changed before you're done comparing.

---

## Topic 5: String Operations and Data Types

More string tools:
- `.str.title()` — capitalizes the first letter of every word
- `.str.contains("text", case=False)` — checks if a value contains
  something, ignoring uppercase/lowercase
- `.str.split("@").str[1]` — splits text and grabs a specific piece
  (like pulling the domain out of an email)

For data types:
- `.dtypes` shows what type each column is
- `pd.to_numeric(column, errors="coerce")` converts text to numbers,
  and turns anything that can't convert (like "twenty-two") into NaN
  instead of crashing

I noticed that a column built from `.str.split()` can end up as a
slightly different type (`object`) compared to normal text columns,
even though it still holds text — a small quirk worth remembering.

---

## Overall Week 3 Summary

- DataFrame = table structure for real-world data, with named columns
- loc/iloc = two ways to grab rows — by label or by position
- groupby/pivot_table = summarizing data by category
- merge = combining two related tables (like SQL JOIN)
- Data cleaning = handling missing values, duplicates, and messy text
- String ops + dtypes = fixing and converting text-based data safely