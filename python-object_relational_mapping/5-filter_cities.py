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
    cursor.execute("SELECT cities.name FROM states \
        INNER JOIN cities ON cities.state_id = states.id \
        WHERE states.name = %s", (sys.argv[4],))

    str = ""
    for city in cursor.fetchall():
        print(str, end="")
        str = ", "
        print("{}".format(city[0]), end="")
    print("")
