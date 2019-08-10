#!/usr/bin/python3
""" list all objects state from database """

from sqlalchemy.orm import Session
from sqlalchemy import (create_engine)
from sys import argv
from model_state import Base, State

if __name__ == "__main__":

    usuario = argv[1]
    clave = argv[2]
    basedatos = argv[3]
    motor = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                          (usuario, clave, basedatos), pool_pre_ping=True)
    Base.metadata.create_all(motor)
    sesion = Session(motor)
    estado = sesion.query(State).first()
    if estado is not None:
        print("{}: {}".format(estado.id, estado.name))
    else:
        print("Nothing")
    sesion.close()
