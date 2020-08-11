#!/usr/bin/python3
"""SQL Injection"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    username = argv[1]
    password_ = argv[2]
    db_name = argv[3]
    name_searched = argv[4]

    db_conex = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password_,
                               db=db_name)
    cur = db_conex.cursor()
    query = """SELECT states.id, name FROM states WHERE name= %(name)s COLLATE
    latin1_general_cs ORDER BY states.id ASC;"""
    arg = {"name": argv[4]}
    cur.execute(query, arg)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db_conex.close()
