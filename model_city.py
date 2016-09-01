from basemodel import *
from model_school import *


class City(BaseModel):

    city_id = PrimaryKeyField()
    name = CharField(unique=True)
    closest_school = ForeignKeyField(School)

    @classmethod
    def get_all(cls):
        return cls.select()

    @classmethod
    def get_by_name(cls, name):
        return cls.select().where(cls.name == name).get()
