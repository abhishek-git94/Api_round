# Bajaj Finserv Health - Qualifier 1 (PYTHON)

A production-grade Python application that automates the workflow for Qualifier 1 of the Bajaj Finserv Health hiring assessment. The application registers with the webhook generation API, extracts authentication tokens, dynamically selects the assigned SQL problem based on registration number parity, and submits the finalized SQL query to the verified receipt webhook.

---

## Table of Contents
1. [Overview](#overview)
2. [Project Architecture](#project-architecture)
3. [SQL Question & Solution Walkthrough](#sql-question--solution-walkthrough)
   - [Database Schema](#database-schema)
   - [Problem Statement](#problem-statement)
   - [Detailed SQL Query Logic](#detailed-sql-query-logic)
   - [Local Verification (SQLite Simulation)](#local-verification-sqlite-simulation)
4. [Setup & Installation](#setup--installation)
5. [Configuration & Usage](#configuration--usage)
6. [Pipeline Output Walkthrough](#pipeline-output-walkthrough)

---

## Overview

This application fulfills all instructions from the Bajaj Finserv Health Qualifier 1 coding guidelines:
* **Webhook Generation on Startup:** Dispatches a `POST` request to `https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON` using structured candidate details.
* **Token Extraction & Authorization:** Extracts the dynamic `accessToken` and target `webhook` URL from the generator response.
* **Dynamic Routing by Registration Parity:** Automatically determines if the assigned question is **Question 1 (Odd last digit)** or **Question 2 (Even last digit)** based on the suffix of the registration number.
* **Automated Solution Submission:** Formulates the SQL query and sends the payload to the receipt webhook URL using the retrieved `accessToken` in the `Authorization` header.
* **Standalone Execution:** Runs fully autonomously from start to finish on application launch without requiring any web server, controller, or manual endpoints to trigger it.

---

## Project Architecture

The codebase is organized into modular, clean, and highly maintainable components:

* **[app.py](file:///c:/Users/ap036/Downloads/projects/bhfl_round1_practice/app.py):** The main application entry point that runs the pipeline on startup.
* **[config.py](file:///c:/Users/ap036/Downloads/projects/bhfl_round1_practice/config.py):** Configuration layer managing candidate registration credentials and endpoints (supports quick customization via environment variables).
* **[sql_solutions.py](file:///c:/Users/ap036/Downloads/projects/bhfl_round1_practice/sql_solutions.py):** Encapsulates the SQL query solutions for the assigned tasks.
* **[requirements.txt](file:///c:/Users/ap036/Downloads/projects/bhfl_round1_practice/requirements.txt):** Declares lightweight external dependencies (e.g., `requests`).

---

## SQL Question & Solution Walkthrough

### Database Schema

The problem workspace contains three tables:
1. **`DEPARTMENT`**
   * `DEPARTMENT_ID` (Integer, Primary Key)
   * `DEPARTMENT_NAME` (Text)
2. **`EMPLOYEE`**
   * `EMP_ID` (Integer, Primary Key)
   * `FIRST_NAME` (Text)
   * `LAST_NAME` (Text)
   * `DOB` (Date, e.g., `'1980-05-15'`)
   * `GENDER` (Text)
   * `DEPARTMENT` (Integer, Foreign Key referencing `DEPARTMENT.DEPARTMENT_ID`)
3. **`PAYMENTS`**
   * `PAYMENT_ID` (Integer, Primary Key)
   * `EMP_ID` (Integer, Foreign Key referencing `EMPLOYEE.EMP_ID`)
   * `AMOUNT` (Decimal, Salary Credited)
   * `PAYMENT_TIME` (Timestamp, e.g., `'2025-01-01 13:44:12.824'`)

### Problem Statement (Assigned Question 1 - Odd RegNo Parity)

> *"Find the highest salary that was credited to an employee, but only for transactions that were not made on the 1st day of any month. Along with the salary, you are also required to extract the employee data like name (combine first name and last name into one column), age and department who received this salary."*

#### Output Formats Required:
1. **`SALARY`**: The highest salary credited not on the 1st of the month.
2. **`NAME`**: Concatenated first and last names separated by a single space (e.g., `"Emily Brown"`).
3. **`AGE`**: Calculated current age of the employee (e.g., based on `DOB`).
4. **`DEPARTMENT_NAME`**: Name of the employee's department.

---

### Detailed SQL Query Logic

The SQL query is formulated to be highly standard and run efficiently:

```sql
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
```

#### Why this query is 100% correct:
1. **Table Joins**: 
   * `PAYMENTS` joined to `EMPLOYEE` on `p.EMP_ID = e.EMP_ID`.
   * `EMPLOYEE` joined to `DEPARTMENT` on `e.DEPARTMENT = d.DEPARTMENT_ID`.
2. **Day Filtering**: `DAY(p.PAYMENT_TIME) <> 1` (or `EXTRACT(DAY FROM p.PAYMENT_TIME) <> 1`) filters out all transactions occurring on the first day of any month.
3. **Age Calculation**: `TIMESTAMPDIFF(YEAR, e.DOB, CURDATE())` provides a precise calculation of current age, checking whether their birthday has passed in the current year.
4. **Name Formatting**: `CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME)` cleanly combines first and last names with a separating space.
5. **Highest Salary Extraction**: `ORDER BY p.AMOUNT DESC LIMIT 1` selects the highest single transaction meeting the date criteria.

---

### Local Verification (SQLite Simulation)

We set up an in-memory SQLite sandbox mimicking the exact tables and values in the assignment. The results of the data trace are:

* **Excluded (Paid on 1st of month)**:
  * Payment ID 1 (Sarah Johnson): `65784.00` on 2025-01-01
  * Payment ID 3 (John Williams): `69437.00` on 2025-01-01
  * Payment ID 5 (Sarah Johnson): `66273.00` on 2025-02-01
  * Payment ID 6 (David Jones): `71475.00` on 2025-01-01
  * Payment ID 9 (Emily Brown): `71876.00` on 2025-02-01
  * Payment ID 14 (John Williams): `67982.00` on 2025-03-01

* **Valid Transactions (Not paid on 1st of month)**:
  * Payment ID 2 (Emily Brown): `62736.00` on 2025-01-06
  * Payment ID 4 (Michael Smith): `67183.00` on 2025-01-02
  * Payment ID 7 (John Williams): `70837.00` on 2025-02-03
  * Payment ID 8 (Olivia Davis): `69628.00` on 2025-01-02
  * Payment ID 10 (Michael Smith): `70098.00` on 2025-02-03
  * Payment ID 11 (Olivia Davis): `67827.00` on 2025-02-02
  * Payment ID 12 (David Jones): `69871.00` on 2025-02-05
  * Payment ID 13 (Sarah Johnson): `72984.00` on 2025-03-05
  * Payment ID 15 (Olivia Davis): `70198.00` on 2025-03-02
  * Payment ID 16 (Emily Brown): **`74998.00`** on 2025-03-02 (Highest!)

**Correct Output Record**:
* **SALARY**: `74998.00`
* **NAME**: `"Emily Brown"`
* **AGE**: `33` (at time of transaction) or `34` (current age in 2026)
* **DEPARTMENT_NAME**: `"Sales"`

---

## Setup & Installation

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 3. Install Dependencies
Install the required HTTP library:
```bash
pip install -r requirements.txt
```

---

## Configuration & Usage

### Running with Default Parameters
By default, the application runs using `John Doe`, `REG12347` (Odd -> Question 1), and `john@example.com`. 
Simply run:
```bash
python app.py
```

### Running with Custom Parameters
You can execute the script with your own credentials **without modifying any source code** by using standard environment variables:

#### On Windows (PowerShell):
```powershell
$env:CANDIDATE_NAME="Jane Smith"
$env:CANDIDATE_REG_NO="REG98764"
$env:CANDIDATE_EMAIL="jane@example.com"
python app.py
```

#### On Linux / macOS:
```bash
CANDIDATE_NAME="Jane Smith" CANDIDATE_REG_NO="REG98764" CANDIDATE_EMAIL="jane@example.com" python app.py
```

*Note: In the case of `REG98764`, the last digit `4` is even, so the application will automatically routing and select Question 2.*

---

## Pipeline Output Walkthrough

When running, the application outputs a detailed step-by-step trace:

```text
============================================================
       BAJAJ FINSERV HEALTH | QUALIFIER 1 | PYTHON
============================================================

[Step 1/4] Preparing candidate details for webhook generation:
{
  "name": "John Doe",
  "regNo": "REG12347",
  "email": "john@example.com"
}

[Step 2/4] Sending POST request to https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON...
[+] Successfully received Webhook URL and Access Token!
    - Webhook URL: https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON
    - Access Token: eyJhbGciOiJIUzI1NiJ9...3jIzsE5QqqJK5Au7kSEo

[Step 3/4] Determining assigned question based on registration number 'REG12347':
    - Last digit of registration number: 7
    - Parity: Odd (Question 1)
    - Assigned Question: [Question 1] (Odd)

Selected SQL Query:
--------------------------------------------------
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
--------------------------------------------------

[Step 4/4] Submitting solution to webhook URL: https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON...

============================================================
                   SUBMISSION SUCCESSFUL
============================================================
Status Code: 200
Response Body:
{
  "success": true,
  "message": "Webhook processed successfully"
}
============================================================
```
