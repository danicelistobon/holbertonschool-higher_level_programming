#!/usr/bin/python3
"""Takes in arguments and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument, but this time,
    write one that is safe from MySQL injections!
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
    c.execute("SELECT * FROM states WHERE name=%s \
                ORDER BY states.id ASC", (stname,))
    rows = c.fetchall()
    for row in rows:
        print(row)
