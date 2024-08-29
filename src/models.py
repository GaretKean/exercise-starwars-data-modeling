import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

    character_favorites = relationship("CharacterFavorites", back_populates="user")
    planet_favorites = relationship("PlanetFavorites", back_populates="user")

class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    character_favorites = relationship("CharacterFavorites", back_populates="character")

class Planets(Base):
    __tablename__ = "planets"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    planet_favorites = relationship("PlanetFavorites", back_populates="planet")

class CharacterFavorites(Base):
    __tablename__ = "character_favorites"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)

    user = relationship("User", back_populates="character_favorites")
    character = relationship("Characters", back_populates="character_favorites")

class PlanetFavorites(Base):
    __tablename__ = "planet_favorites"
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)

    user = relationship("User", back_populates="planet_favorites")
    planet = relationship("Planets", back_populates="planet_favorites")


    # 


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
