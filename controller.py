import mysql.connector
import matplotlib.pyplot as pt

# ===================SQL Connectivity=================

# SQL Connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="student_management",
    port="3306",
    autocommit=True,
)

cursor = connection.cursor(buffered=True)

# Them hoc sinh
def add_student(full_name, birthday, email, sex, address):
    cmd = f"insert into Students(full_name, birthday, email, sex, address) values('{full_name}','{birthday}','{email}','{sex}','{address}');"
    cursor.execute(cmd)
    if cursor.rowcount == 0:
        return False
    return True