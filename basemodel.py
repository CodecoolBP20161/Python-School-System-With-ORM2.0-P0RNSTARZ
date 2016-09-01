from peewee import *

db = PostgresqlDatabase('csibi', user='csibi')


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db
