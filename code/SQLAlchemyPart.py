#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy import create_engine

# echo=True indicates that engine should print debugging information
# including all sql statements it issues
engine = create_engine('sqlite:///:memory:', echo=True)
print(engine, sqlalchemy.__version__)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Text, Boolean





#creating a table
class Countries(Base):
    __tablename__ = 'countries'
    user_id = Column(Integer, primary_key = True)
    country1 = Column(String, nullable=False)
    country2 = Column(String, nullable=False)
    country3 = Column(String, nullable=True)
    country4 = Column(String, nullable=True)
    country5 = Column(String, nullable=True)
    country6 = Column(String, nullable=True)
    country7 = Column(String, nullable=True)
    country8 = Column(String, nullable=True)
    country9 = Column(String, nullable=True)
    country10 = Column(String, nullable=True)
    inbound = Column(String, nullable=False)
    outbound = Column(String, nullable=False)
    passengers = Column(Integer, nullable=False)
    budget = Column(Integer, nullable=False)
    currency1 = Column(Integer, nullable=False)
    currency2 = Column(Integer, nullable=False)
    currency3 = Column(Integer, nullable=True)
    currency4 = Column(Integer, nullable=True)
    currency5 = Column(Integer, nullable=True)
    currency6 = Column(Integer, nullable=True)
    currency7 = Column(Integer, nullable=True)
    currency8 = Column(Integer, nullable=True)
    currency9 = Column(Integer, nullable=True)
    currency10 = Column(Integer, nullable=True)

Base.metadata.create_all(engine)

#adding an element
countries_inputed = ["US", "Brazil", "UK", "Spain", "Portugal", "Italy", None, None, None, None ]
currency_API = [1, 0.5, 2, 4.5, 6, 0.4, None, None, None, None]

session = SessionMaker(autoflush=False)

ct1 = Countries()
ct2 = Countries()
ct3 = Countries()
ct4 = Countries()
ct5 = Countries()
ct6 = Countries()
ct7 = Countries()
ct8 = Countries()
ct9 = Countries()
ct10 = Countries()

ct1.country1 = countries_inputed[0]
ct1.country2 = countries_inputed[1]
ct1.country3 = countries_inputed[2]
ct1.country4 = countries_inputed[3]
ct1.country5 = countries_inputed[4]
ct1.country6 = countries_inputed[5]
ct1.country7 = countries_inputed[6]
ct1.country8 = countries_inputed[7]
ct1.country9 = countries_inputed[8]
ct1.country10 = countries_inputed[9]

ct1.currency1 = currency_API[0]
ct2.currency1 = currency_API[1]
ct3.currency1 = currency_API[2]
ct4.currency1 = currency_API[3]
ct5.currency1 = currency_API[4]
ct6.currency1 = currency_API[5]
ct7.currency1 = currency_API[6]
ct8.currency1 = currency_API[7]
ct9.currency1 = currency_API[8]
ct10.currency1 = currency_API[9]

session.add(ct1)
session.add(ct2)
session.add(ct3)
session.add(ct4)
session.add(ct5)
session.add(ct6)
session.add(ct7)
session.add(ct8)
session.add(ct9)
session.add(ct10)

session.commit()
*/


