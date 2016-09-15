from peewee import *
import base
import product
import product_price
import source_url

if __name__ == '__main__':
    base.psql_db.connect()

    print "Successfully connected to the db..."

    base.psql_db.create_tables(SourceUrl, Product, ProductPrice)

    print "Successfully created the tables  in the db..."
