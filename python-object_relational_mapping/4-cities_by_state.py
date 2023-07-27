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

    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name \
                 FROM cities \
                INNER JOIN states \
                   ON cities.state_id = states.id \
                ORDER BY cities.id"
    )

    for city in cursor.fetchall():
        print(city)
