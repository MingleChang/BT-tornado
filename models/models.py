#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text, String, Integer, SmallInteger, Date, DateTime, TIMESTAMP, Table, create_engine
from sqlalchemy import ForeignKey
# from sqlalchemy.orm import scoped_session,sessionmaker,relationship,backref
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

def init_db(engine):
    Base.metadata.create_all(bind=engine)

def update_db(engine):
    pass
    
def drop_db(engine):
    Base.metadata.drop_all(bind=engine)
    
class File(Base):
    __tablename__='file'

    fileid=Column(String(50), primary_key=True)
    title=Column(String(200))
    content=Column(Text)
    path=Column(String(500))
    create=Column(DateTime,default=datetime.datetime.utcnow())

