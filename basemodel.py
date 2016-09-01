from peewee import *

db = PostgresqlDatabase('TothBalint', user='balint')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db
