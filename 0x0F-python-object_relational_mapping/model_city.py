#!/usr/bin/python3
""" Model Cities """

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """ Class Cities """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=True, ForeignKey(State.id))
