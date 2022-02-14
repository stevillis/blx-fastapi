from sqlalchemy.orm import Session

from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class RepositoryProduct:
    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        db_product = models.Product(
            name=product.name,
            detail=product.detail,
            price=product.price,
            available=product.available
        )
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def fetch_all(self):
        products = self.db.query(models.Product).all()
        return products

    def fetch_one(self):
        pass

    def remove(self):
        pass
