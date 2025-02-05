-- Write query to get count of assignments in each grade
SELECT grade, COUNT(*) AS count
FROM assignments
WHERE grade IS NOT NULL
GROUP BY grade;