#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N) from hbtn_0e_0_usa
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
    c.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
