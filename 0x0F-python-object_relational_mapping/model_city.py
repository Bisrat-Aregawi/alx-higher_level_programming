#!/usr/bin/python3
"""Module defines a class for `cities` table."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base


class City(Base):
    """City class representing a table by the name `cities`."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey("states.id"))
