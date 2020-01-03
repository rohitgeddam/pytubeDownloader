from sqlalchemy import Column,String,Integer

from databaseConnection import Base

class Downloaded(Base):
    __tablename__ = "downloaded"

    id =Column(Integer,primary_key = True)
    title = Column(String(100))
    

    def __init__(self,title):
        self.title = title