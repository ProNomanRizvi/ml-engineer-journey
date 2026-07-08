-- ============================================
-- Topic: SELECT & WHERE Basics
-- ============================================

-- Task 01: Extract ALL Students Data
SELECT * FROM students;

-- Task 02: Extract Two Columns [Name, gpa]
SELECT name, gpa FROM students;

-- Task 03: AGE > 21
SELECT *
FROM students
WHERE age > 21;

-- Task 04: "SE" Department Students
SELECT *
FROM students
WHERE department = 'SE';

-- Task 05: GPA >= 3.7 AND Department is "SE".
SELECT *
FROM students
WHERE gpa >= 3.7 AND department = 'SE';

