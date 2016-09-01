from basemodel import *
from model_school import *


class City(BaseModel):

    city_id = PrimaryKeyField()
    name = CharField(unique=True)
    closest_school = ForeignKeyField(School)
