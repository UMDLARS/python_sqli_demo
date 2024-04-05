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
# https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders
params = (username, password, id)
result = conn.execute("SELECT grade FROM grades WHERE user = ? AND pass = ? AND id = ?", params)

# Print user's grade.
print(result.fetchall())
