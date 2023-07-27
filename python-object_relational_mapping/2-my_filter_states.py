#!/usr/bin/python3
"""Lists all states starting with N."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.Connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        host="localhost"
    )

    query = sys.argv[4]

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states")

    for state in cursor.fetchall():
        if state[1] == query:
            print(state)
