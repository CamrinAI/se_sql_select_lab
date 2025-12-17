# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')

# STEP 2
# Replace None with your code
# Select employeeNumber and lastName from all employees
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees;
    """,
    conn,
)

# STEP 3
# Replace None with your code
# Same data as step 2, but with columns reversed
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees;
    """,
    conn,
)

# STEP 4
# Replace None with your code
# Alias employeeNumber as ID (order same as step 3)
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees;
    """,
    conn,
)

# STEP 5
# Replace None with your code
# Add role column via CASE expression
df_executive = pd.read_sql(
    """
    SELECT
        jobTitle,
        CASE
            WHEN jobTitle IN ('President', 'VP Sales', 'VP Marketing') THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees;
    """,
    conn,
)

# STEP 6
# Replace None with your code
# Length of last names
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees;
    """,
    conn,
)

# STEP 7
# Replace None with your code
# First two letters of each job title
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
    """,
    conn,
)

# STEP 8
# Replace None with your code
# Sum of rounded total prices per order line from orderdetails
sum_total_price = pd.read_sql(
    """
    SELECT ROUND(priceEach * quantityOrdered) AS total_price
    FROM orderdetails;
    """,
    conn,
).sum()

# STEP 9
# Replace None with your code
# Original orderDate followed by day/month/year
df_day_month_year = pd.read_sql(
    """
    SELECT
        orderDate,
        strftime('%d', orderDate) AS day,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year
    FROM orders;
    """,
    conn,
)