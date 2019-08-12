#!/usr/bin/python3
""" list all objects state from database """

from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from sys import argv
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    usuario = argv[1]
    clave = argv[2]
    basedatos = argv[3]
    motor = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                          (usuario, clave, basedatos), pool_pre_ping=True)
    Base.metadata.create_all(motor)
    sesion = Session(motor)
    consulta = sesion.query(City, State).filter(City.state_id == State.id)\
                                        .order_by(City.id.asc()).all()
    for ciudades, estados in consulta:
        print("{}: ({}) {}".format(estados.name, ciudades.id, ciudades.name))
    sesion.close()
