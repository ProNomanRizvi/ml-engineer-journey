-- ============================================
-- Topic: Window Functions
-- ============================================

-- Task 1: Use Row Number

SELECT name, gpa,
    ROW_NUMBER() OVER(ORDER BY gpa DESC) AS gpa_rank
FROM students;

-- Task 2: Use Rank
SELECT name, gpa,
    RANK() OVER(ORDER BY gpa DESC) AS gpa_rank
FROM students;

-- Task 3: Use LAG
SELECT name, gpa,
    LAG(gpa) OVER(ORDER BY gpa DESC) AS pre_gpa
FROM students;

-- Task 4: Use LEAD
SELECT name, gpa,
    LEAD(gpa) OVER(ORDER BY gpa DESC) AS next_gpa
FROM students;

-- Task 5: Use PARTITION BY
SELECT name, department, gpa,
    RANK() OVER(PARTITION BY department ORDER BY gpa DESC) AS dept_rank
FROM students;

-- ============================================
-- Topic: CTEs (Common Table Expressions)
-- ============================================