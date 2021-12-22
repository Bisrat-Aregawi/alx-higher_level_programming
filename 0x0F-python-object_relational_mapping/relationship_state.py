#!/usr/bin/python3
"""Module defines class for `states` table."""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class State(Base):
    """State class mapped to `states` table."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
