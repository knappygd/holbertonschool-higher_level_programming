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
        "SELECT * FROM cities \
        JOIN states \
        ON cities.state_id = states.id \
        ORDER BY cities.id")

    cities = []
    for city in cursor.fetchall():
        if city[4] == query:
            cities.append(city[2])
    for city in range(len(cities)):
        if city != len(cities) - 1:
            print(cities[city], end=", ")
        else:
            print(cities[city])
