#!/usr/bin/python3
# a script that list all cities from a database

import sys
import MySQLdb

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost",port = 3306,user = username,passwd=password,db = database_name)

    # creating a cursor to help navigate through the database
    cursor = db.cursor()
    
    # Quering the database and listing all the cities in a database
    query = "SELECT * FROM cities ORDER BY id ASC "

    # Executing the query
    cursor.execute(query)

    rows = cursor.fetchall()

    # Printing all the rows queried

    for row in rows:
        print(row)

    # closing the cursor and the database

    cursor.close()
    db.close()

