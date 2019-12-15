#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":

    usernm = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    stname = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=usernm,
                         passwd=password, db=dbname)

    c = db.cursor()
    c.execute("SELECT cities.name FROM cities INNER JOIN states \
                ON cities.state_id = states.id WHERE states.name=%s \
                ORDER BY cities.id ASC", (stname,))
    rows = c.fetchall()
    l = []
    for row in rows:
        l.append(row[0])
    print(", ".join(l))
