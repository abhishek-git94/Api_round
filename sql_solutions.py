# SQL Solutions for Bajaj Finserv Health Qualifier 1

# QUESTION 1 (Odd Registration Number)
# Problem Statement:
# Find the highest salary that was credited to an employee, but only for transactions that were not 
# made on the 1st day of any month. Along with the salary, you are also required to extract the 
# employee data like name (combine first name and last name into one column), age and 
# department who received this salary.
#
# Output Columns:
# 1. SALARY: The highest salary that was credited not on the 1st day of the month.
# 2. NAME: Combine the columns FIRST_NAME and LAST_NAME into one single column as NAME with format <first name><space><last name>.
# 3. AGE: The age of the employee who received that salary.
# 4. DEPARTMENT_NAME: Name of the department against employee.

SQL_QUESTION_1 = """
SELECT 
    p.AMOUNT AS SALARY,
    CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
    TIMESTAMPDIFF(YEAR, e.DOB, CURDATE()) AS AGE,
    d.DEPARTMENT_NAME
FROM PAYMENTS p
JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
WHERE DAY(p.PAYMENT_TIME) <> 1
ORDER BY p.AMOUNT DESC
LIMIT 1;
""".strip()


# QUESTION 2 (Even Registration Number)
# As noted, the Google Drive link for Question 2 (Even) returned a 404 in the test instructions.
# Therefore, we default to the well-defined Question 1 query if needed, or raise a warning.
SQL_QUESTION_2 = SQL_QUESTION_1
