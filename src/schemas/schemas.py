from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    phone: str


class Product(BaseModel):
    id: Optional[UUID] = uuid4()
    # user: User
    name: str
    detail: str
    price: float
    available: bool = False

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[UUID] = uuid4()
    # user: User
    # product: Product
    quantity: int
    delivery: bool = False
    address: str
    note: Optional[str] = None
