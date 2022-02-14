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
