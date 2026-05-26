# Complete Answers & Solutions for Bajaj Finserv Health Technical Assessment
# Candidate: Abhishek Pal (0827AL231009)

# -----------------------------------------------------------------------------
# SECTION 1: PYTHON & DATA WRANGLING
# -----------------------------------------------------------------------------

# Q1. What is the difference between total sales of Electronics in North region and Furniture in South region (considering only Delivered orders)?
# Calculation: Electronics North ($367,800) - Furniture South ($36,000) = $331,800
q1 = 331800  # DataType: int

# Q2. How many orders were placed by customer_id 'C001' in the entire dataset?
# Answer: 4 (Orders 1001, 1003, 1021, 1036)
q2 = 4  # DataType: int

# Q3. Which product has the highest price_per_unit in the Electronics category?
# Answer: "Laptop" (Price: $55,000 for Order 1014)
q3 = "Laptop"  # DataType: str

# Q4. What is the average quantity of products ordered in the month of May 2024?
# Calculation: Total Quantity of 9 orders is 16 (16 / 9 = 1.7777...) -> rounded to 2 decimals is 1.78
q4 = 1.78  # DataType: float

# Q5. Contiguous subarray whose sum equals k
# Test Case Output for range(7) array [1, 0, 0, 0, 0, 0, 1] with k = 2 is 7
q5 = 7  # DataType: int


# -----------------------------------------------------------------------------
# SECTION 2: SQL & DATA CLEANING
# -----------------------------------------------------------------------------

# Q6. Which department has the highest average VALID marks?
# Cleaned Valid Averages: CSE (81.67), ECE (86.75), IT (86.50), ME (89.00)
# Answer: "ME"
q6 = "ME"  # DataType: str

# Q7. Find the name of the student with the SECOND highest valid mark (Tie-breaker: lower student_id wins)
# Valid mark rankings: 1st (Kevin: 95), 2nd (Charlie: 92, student_id: 3), 3rd (Hannah: 92, student_id: 8)
# Answer: "Charlie"
q7 = "Charlie"  # DataType: str

# Q8. What is the result of the SQL query calculating highest average age where valid_age = True?
# SELECT department FROM students WHERE valid_age = TRUE GROUP BY department ORDER BY AVG(age) DESC, department ASC LIMIT 1;
# Cleaned Averages: IT (27.00), ME (23.67), ECE (22.00), CSE (21.75)
# Answer: "IT"
q8 = "IT"  # DataType: str

# Q9. How many rows will raise conversion errors on df['marks'] = df['marks'].astype(int)?
# Raw Conversion Errors: 5 (Charlie '92*', David 'AB', Eva '-', Laura None, Mike '85abc')
# Added with the first 4 digits of enrollment number '0827AL231009' (827): 827 + 5 = 832.0
q9 = 832.0  # DataType: float

# Q10. How many students satisfy ALL conditions (valid marks, valid age, valid date, dept standardized to CSE)?
# Satisfied by exactly 2 students: Alice (ID: 1) and Oscar (ID: 15)
# Answer: "2"
q10 = "2"  # DataType: str
