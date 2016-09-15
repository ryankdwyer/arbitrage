from peewee import *
from base import BaseModel


class Product(BaseModel):
    upc = CharField(unique=true)
    url = ForeignKeyField(SourceUrl, related_name='source')
    description = CharField()
    asin = CharField(unique=true)
    product_number = CharField()
