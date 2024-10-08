#!/usr/bin/python3

# a script that takes an argument and displays all values in the state table in the database

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",port=3306,user=username,passwd=password,db=database_name)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(state_name)

    cursor.execute(query)
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)


    cursor.close()
    db.close()
