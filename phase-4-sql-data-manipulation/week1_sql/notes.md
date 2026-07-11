# Phase 4 - Week 1: SQL Notes

## Topic 1: SELECT and WHERE

SELECT picks the columns we want. `SELECT *` grabs everything, or we can
pick specific ones like `SELECT name, gpa`.

WHERE filters rows based on a condition, like `WHERE age > 21`. We can
combine multiple conditions using AND, like `WHERE gpa >= 3.7 AND
department = 'SE'`.

Simple rule: SELECT decides which columns show up, WHERE decides which
rows show up.

---

## Topic 2: GROUP BY, ORDER BY, HAVING

ORDER BY sorts results (ASC by default, DESC for largest to smallest).

GROUP BY groups rows that share the same value, like putting all CS
students together and all SE students together.

Aggregate functions work with GROUP BY to calculate something per group:
- COUNT() - counts rows in each group
- AVG() - average value in each group
- SUM(), MAX(), MIN() - similar idea

HAVING filters groups after they're formed, unlike WHERE which filters
rows before grouping. Example: `HAVING AVG(gpa) > 3.5` only keeps
departments with a high enough average.

---

## Topic 3: JOINs (INNER JOIN and LEFT JOIN)

JOIN combines data from two related tables. We give tables short
nicknames (aliases) to keep queries clean, like `students AS s`.

**INNER JOIN** only returns rows that have a match in both tables. If a
student has no enrollment, they disappear from the result. Ayesha Malik
had no course, so she didn't show up here.

**LEFT JOIN** returns all rows from the left table (students), even if
there's no match. Missing data just shows up as NULL. Ayesha showed up
here, but her course was NULL.

I also noticed the enrollments table had a record with student_id = 6,
which doesn't exist in the students table. This orphan row never showed
up in either join, because both joins started from the students side.

---

## Topic 4: Window Functions

Window functions add a calculated column without squashing rows together
(unlike GROUP BY, which merges rows into one).

- **ROW_NUMBER()** — gives every row a unique number (1, 2, 3...), even
  if values are tied
- **RANK()** — gives the same rank to tied values, but skips the next
  number (like 1, 1, 3 instead of 1, 2, 3)
- **LAG()** — shows the value from the previous row
- **LEAD()** — shows the value from the next row

All of these use `OVER (ORDER BY ...)` to define the order they work on.

**PARTITION BY** splits data into separate mini-groups before ranking.
For example, `PARTITION BY department` gives each department its own
independent ranking instead of one big ranking for everyone.

I tested this by adding two students with the same GPA (a tie), and
that's when I actually saw the difference between ROW_NUMBER and RANK —
ROW_NUMBER kept counting normally, RANK gave both the same number and
skipped ahead.

---

## Topic 5: CTEs (Common Table Expressions)

A CTE is a temporary named result, made using `WITH ... AS (...)`. It
works like a variable — I calculate something once, give it a name, and
then use it like a normal table in the rest of the query.

Example: I made a CTE that filtered only SE department students, then
ran `AVG(gpa)` on top of that CTE to get their average GPA.

CTEs make complex queries easier to read, especially when combining
filters with window functions (like finding each department's topper
using RANK inside a CTE, then filtering `WHERE rank_num = 1` outside).

Important: when using an aggregate function like AVG() in the final
SELECT, I can't also select a regular column like name, unless I group
by it — otherwise SQL doesn't know which row's name to show.

---

## Topic 6: Subqueries

A subquery is a query written inside another query, without giving it a
name first (unlike a CTE).

**In WHERE clause:**
```sql
WHERE gpa > (SELECT AVG(gpa) FROM students)
```
The inner query runs first, gets one number (the average), and the
outer query compares each row against it.

**With IN:**
```sql
WHERE id IN (SELECT student_id FROM enrollments)
```
This finds students who have a matching record in another table —
works similarly to an INNER JOIN.

**With NOT IN:**
Just the opposite — finds students with no matching record.

I used all three patterns: found students above the class average GPA,
found students who are enrolled in a course, and found students who
aren't enrolled in anything.

---

## Overall Week 1 Summary

- SELECT/WHERE = pick and filter data
- GROUP BY/HAVING = summarize data by category
- JOIN = combine two tables
- Window Functions = add rankings/calculations without losing rows
- CTEs = name a query result to reuse it cleanly
- Subqueries = use one query's result inside another