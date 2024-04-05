#!/usr/bin/python3
import sqlite3
import os

# Ask user for their username.
username = input("Enter your username: ")

# Ask user for their password.
password = input("Enter your password: ")

# Ask user for their ID.
id = input("Enter your id: ")

# Open SQLite3 db.
conn = sqlite3.connect("grades.db")

# Create query.
query = f"SELECT grade FROM grades WHERE user = \'{username}\' AND pass = \'{password}\' AND id = {id};"
print(query)

# Invoke query.
print("Your average grade is: ", end = "", flush=True)
os.system(f"sqlite3 grades.db \"{query}\"")
