#!/usr/bin/python3
"""Module defines class for `cities` table."""

import sqlalchemy
from sqlalchemy import ForeignKey
from relationship_state import Base
from sqlalchemy import Column, Integer, String


class City(Base):
    """City class mapped to `cities` table."""

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey("states.id"))
