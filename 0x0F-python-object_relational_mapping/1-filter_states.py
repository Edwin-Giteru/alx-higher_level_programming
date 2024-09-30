#!/usr/bin/python3
# listing all states with a name starting with N in a database
import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # connecting to MySQL server where port number is 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
    cursor = db.cursor()

    # Executing an SQL query to select states starting with letter N
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetching all rows from the executed query
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

