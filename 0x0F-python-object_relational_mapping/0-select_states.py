#!/usr/bin/python3
"""
lists all states from the database
"""
import MySQLdb
from sys import import argv

if __name__ == '__main__':

    usuario = argv[1]
    contrase = argv[2]
    basedatos = argv[3]
    hosting = "localhost"
    puerto = 3306

    db = MySQLdb.connect(host=hosting, port=3306, user= usuario,
                         passwd=contrase, db=basedatos)
    conex = db.cursor()
    sqlquery = "SELECT * FROM states ORDER BY id ASC"
    conex.execute(sqlquery)
    filas = conex.fetchall()
    for row in rows:
        print(row)
    conex.close()
    db.close()
