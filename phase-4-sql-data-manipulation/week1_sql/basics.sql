-- ============================================
-- Topic 1: SELECT & WHERE Basics
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

-- ============================================
-- Topic 2: GROUP BY, ORDER BY, HAVING
-- ============================================

-- Task 06: All students in DESC Order according to their GPA
SELECT * 
FROM students
ORDER BY gpa DESC;

-- Task 07: Get Total Count of Every Department
SELECT department, COUNT(*)
FROM students
GROUP BY department;

-- Task 08: Get Average GPA of Every Department 
SELECT department, AVG(gpa)
FROM students
GROUP BY department;

-- Task 09: Only Departments Average GPA > 3.5 
SELECT department, AVG(gpa)
FROM students
GROUP BY department
HAVING AVG(gpa) > 3.5;

-- Task 10: Average GPA of Every Department in DESC Order
SELECT department, AVG(gpa)
FROM students
GROUP BY department
ORDER BY AVG(gpa) DESC;