from peewee import *
from base import BaseModel


class SourceUrl(BaseModel):
    url = CharField(unique=true)
    last_fetch = TimeField(default=0)
    response_code = CharField(default='200')
    source = CharField()
