from peewee import *
import base
from product import Product
from product_price import ProductPrice
from source_url import SourceUrl

if __name__ == '__main__':
    base.psql_db.connect()

    print "Successfully connected to the db..."

    base.psql_db.create_tables([SourceUrl, Product, ProductPrice])

    print "Successfully created the tables  in the db..."
