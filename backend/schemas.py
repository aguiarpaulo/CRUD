from pydantic import BaseModel, PositiveFloat, EmailStr, validator, Field
from enum import Enum
from datetime import datetime
from typing import Optional

class CategoryBase(Enum):
    category1 = "Type1"
    category2 = "Type2"
    category3 = "Type3"
    category4 = "Type4"
    category5 = "Type5"

class ProductBase(BaseModel):
    name: str
    descriptin: Optional[str] = None
    price: PositiveFloat
    category: str
    email: EmailStr

    @validator('category')
    def check_category(cls, v):
        if v in [item.value for item in CategoryBase]:
            return v
        raise ValueError('Invalid Category')
    
class ProductCreate(ProductBase):
    pass

class ProductReponse(ProductBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

    @validator('category', pre=True, always=True)
    def check_category(cls, v):
        if v is None:
            return v
        if v in [item.value for item in CategoryBase]:
            return v
        raise ValueError("Invalid Category")