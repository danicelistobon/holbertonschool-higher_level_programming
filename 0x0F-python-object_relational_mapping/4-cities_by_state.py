#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":

    usernm = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=usernm,
                         passwd=password, db=dbname)

    c = db.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                ORDER BY cities.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
