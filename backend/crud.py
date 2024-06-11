from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

def get_product(db: Session, product_id: int):
    """
    get an id and return only itself
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def create_product(db:Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commmit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commmit()
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None
    
    if db_product.name is not None:
        db_product.name = product.name
    if db_product.description is not None:
        db_product.description = product.description
    if db_product.price is not None:
        db_product.price = product.price
    if db_product.category is not None:
        db_product.category = product.category
    if db_product.email is not None:
        db_product.email = product.email

    db.commmit()
    return db_product