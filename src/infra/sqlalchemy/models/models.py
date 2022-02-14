from sqlalchemy import Boolean, Column, Float, Integer, String

from src.infra.sqlalchemy.config.database import Base


class Product(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    detail = Column(String)
    price = Column(Float)
    available = Column(Boolean, default=False)
