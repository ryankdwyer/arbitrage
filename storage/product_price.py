from peewee import *
from base import BaseModel
from product import Product


class ProductPrice(BaseModel):
    asin = ForeignKeyField(Product, related_name='product_info')
    time = BigIntegerField()
    price = FloatField()
