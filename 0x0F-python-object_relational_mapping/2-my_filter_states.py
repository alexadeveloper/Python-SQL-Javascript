#!/usr/bin/python3
"""
lists all states from the database
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    usuario = argv[1]
    contrase = argv[2]
    basedatos = argv[3]
    estado = argv[4]
    hosting = "localhost"
    puerto = 3306

    db = MySQLdb.connect(host=hosting, port=3306, user=usuario,
                         passwd=contrase, db=basedatos)
    conex = db.cursor()
    sql = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(estado)
    conex.execute(sql)
    filas = conex.fetchall()
    for fila in filas:
        if fila[1][0] == 'N':
            print(fila)
    conex.close()
    db.close()
