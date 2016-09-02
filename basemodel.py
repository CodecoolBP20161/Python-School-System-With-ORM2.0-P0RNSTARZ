from peewee import *
from config import *

# you can add your database and username in the 'config.json' file
db = PostgresqlDatabase(Config.load('database'), user=Config.load('user'))


class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = db
