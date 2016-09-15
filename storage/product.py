from peewee import *
from base import BaseModel
from source_url import SourceUrl


class Product(BaseModel):
    upc = CharField(unique=True)
    source_url = ForeignKeyField(SourceUrl)
    description = CharField()
    asin = CharField(unique=True)
    product_number = CharField()
