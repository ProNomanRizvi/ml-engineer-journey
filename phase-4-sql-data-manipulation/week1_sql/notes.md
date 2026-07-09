# Phase 4 - Week 1: SQL Basics Notes

## Topic 1: SELECT and WHERE

SELECT is how we pick data from a table. We can either grab everything using
`SELECT *`, or pick only the columns we need, like `SELECT name, gpa`.

WHERE is used to filter rows based on a condition. For example,
`WHERE age > 21` only shows students older than 21.

We can also combine conditions using AND. For example,
`WHERE gpa >= 3.7 AND department = 'SE'` only shows students who match
both conditions at the same time.

Basically:
- SELECT decides which columns show up
- WHERE decides which rows show up

---

## Topic 2: GROUP BY, ORDER BY, HAVING

ORDER BY sorts the result. By default it sorts smallest to largest (ASC),
but adding DESC sorts it largest to smallest.

GROUP BY combines rows that share the same value into one group. For example,
grouping students by department puts all CS students together and all SE
students together.

Once we group rows, we usually want to calculate something for each group.
That's where aggregate functions come in:
- COUNT() - counts how many rows are in each group
- AVG() - calculates the average value in each group
- SUM(), MAX(), MIN() - work similarly

HAVING is like WHERE, but it filters groups instead of individual rows.
For example, `HAVING AVG(gpa) > 3.5` only keeps departments whose average
GPA is above 3.5.

Important difference:
- WHERE filters rows BEFORE grouping happens
- HAVING filters groups AFTER grouping happens

---

## Topic 3: JOINs (INNER JOIN and LEFT JOIN)

Real data usually lives in more than one table. JOIN is how we combine data
from two related tables into a single result.

To make writing queries shorter, we give tables a nickname (alias). For
example, `students AS s` lets us write `s.name` instead of `students.name`.

**INNER JOIN**
Only returns rows where there is a match in both tables. If a student has
no matching entry in the enrollments table, that student disappears from
the result completely.

Example: Ayesha Malik has no enrollment record, so she did not show up in
the INNER JOIN result.

**LEFT JOIN**
Returns ALL rows from the left table (students), even if there is no match
in the right table (enrollments). If there's no match, the missing columns
just show up as NULL.

Example: Ayesha Malik showed up in the LEFT JOIN result, but her course
columns were empty (NULL), because she isn't enrolled in anything.

**Orphan record observation**
The enrollments table had a row with student_id = 6, but no student with
id = 6 exists in the students table. This orphan row did not appear in
either INNER JOIN or LEFT JOIN, because both joins started from the
students table (the "left side"). If we had started the join from the
enrollments table instead, this orphan record would have shown up with
NULL student info.

**Quick Summary**
- INNER JOIN = only matched rows from both tables
- LEFT JOIN = all rows from the left table, matched or not
- The table we choose as the "starting point" (left side) affects which
  unmatched rows show up