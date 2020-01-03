from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 

engine = create_engine("mysql+pymysql://root:root@localhost/youPyDownloader",echo=True)
Session = sessionmaker(bind = engine)

session = Session()

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()