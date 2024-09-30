#!/usr/bin/python3
# a script that takes in arguments and displays all the values in the state table in a database

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",port=3306,user =username,passwd=password,db=database_name)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    cursor.execute(query,(state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    
    cursor.close()
    db.close()
