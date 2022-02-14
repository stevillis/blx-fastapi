from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import create_database, get_db
from src.infra.sqlalchemy.respositories.product import RepositoryProduct
from src.schemas import schemas

create_database()

app = FastAPI()


@app.get('/products')
def fetch_products(db: Session = Depends(get_db)):
    products = RepositoryProduct(db).fetch_all()
    return products


@app.post('/products')
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    product_created = RepositoryProduct(db).create(product)
    return product_created
