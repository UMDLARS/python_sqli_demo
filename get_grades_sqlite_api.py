import sqlite3

# Ask user for their username.
username = input("Enter your username: ")

# Ask user for their password.
password = input("Enter your password: ")

# Ask user for their ID.
id = input("Enter your id: ")

# Open SQLite3 db.
conn = sqlite3.connect("grades.db")

# Create & invoke query.
query = f"SELECT grade FROM grades WHERE user = \"{username}\" AND pass = \"{password}\" AND id = {id};"
print(query)
result = conn.execute(query)

# Print user's grade.
print(result.fetchall())
