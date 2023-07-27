#!/usr/bin/python3
# Lists all states in the database.
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.Connect(
        user=sys.argv[1],
        pwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")

    for state in cursor.fetchall():
        print(state)
