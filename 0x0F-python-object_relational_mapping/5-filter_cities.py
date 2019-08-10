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
    cities = []

    db = MySQLdb.connect(host=hosting, port=3306, user=usuario,
                         passwd=contrase, db=basedatos)
    conex = db.cursor()
    sql = """SELECT c.name
    FROM cities c, states s
    WHERE c.state_id=s.id
    AND s.name = %s
    ORDER BY c.id ASC"""
    conex.execute(sql, (estado,))
    filas = conex.fetchall()
    for fila in filas:
        cities.append(fila[0])
    print(', '.join(cities))
    conex.close()
    db.close()
