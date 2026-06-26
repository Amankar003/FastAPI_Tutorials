from sqlalchemy import Column, Integer, String, VARCHAR
from database import Base

class book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(VARCHAR(225))
    author = Column(VARCHAR(225))
    published_date = Column(VARCHAR(225))


    
    