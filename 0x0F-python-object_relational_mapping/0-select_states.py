#listing all states from a database
#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost",port = 3306,user =username,passwd=password,db=database_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute SQL query to retrieve all states sorted by id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the executed query
    rows = cursor.fetchall()

    # Print the results row by row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()

