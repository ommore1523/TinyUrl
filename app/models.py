from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import config

Base = declarative_base()

class TinyUrl(Base):
    __tablename__ = 'tinyurl'

    id = Column(Integer, primary_key=True, autoincrement=True)
    long_url = Column(String(2000), nullable=False)
    short_url = Column(String(2000), nullable=False, unique=True)
    created_date = Column(DateTime, nullable=False, default=datetime.utcnow)


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# Create the table
Base.metadata.create_all(engine)