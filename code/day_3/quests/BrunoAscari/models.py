from sqlalchemy import Boolean,Column,ForeignKey,Integer,String
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "Users"

id = Column(Integer, primary_key=True, index=True)
name = Column(String, index= True)
email = Column(String, index= True)
description = Column(String, index= True)