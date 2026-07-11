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

-- Task 6: CTE to calculate average GPA of SE department students

WITH se_dept AS (
    SELECT name, department, gpa
    FROM students
    WHERE department = 'SE'
)

SELECT AVG(gpa) AS se_avg_gpa
FROM se_dept;

-- Task 7: CTE to find the top student in each department

WITH toppers AS (
    SELECT name, department, gpa,
        RANK() OVER(PARTITION BY department ORDER BY gpa DESC) AS rank_num
    FROM students
)
SELECT * 
FROM toppers
WHERE rank_num = 1
ORDER BY gpa DESC;