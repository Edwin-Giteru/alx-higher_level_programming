#!/usr/bin/python3
# a script that takes the name of the state as an argument and list all the cities of the state

import sys
import MySQLdb

if __name__ =="__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",port=3306,user=username,passwd=password,db=database_name)
    # creating a cursor
    cursor = db.cursor()

    # querying the database
    query =  """SELECT cities.id,cities.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""
    
    # Executing the query
    cursor.execute(query, (state_name,))

    #print the data queried
    rows = cursor.fetchall()
    
    city_list =[row[1] for row in rows]
    print(",".join(city_list))

    #closing the database and cursor
    cursor.close()
    db.close()

