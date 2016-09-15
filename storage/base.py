from peewee import *

psql_db = PostgresqlDatabase('arbitrage')

class BaseModel(Model):
        '''
        A base model for all models
        '''
        class Meta:
            database = psql_db
