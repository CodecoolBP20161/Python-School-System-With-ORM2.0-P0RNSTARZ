from peewee import *

db = PostgresqlDatabase('billchr', user='billchr')


class BaseModel(Model):
    class Meta:
        database = db
