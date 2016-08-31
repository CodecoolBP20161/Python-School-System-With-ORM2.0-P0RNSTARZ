from school import *


class City(BaseModel):

    name = CharField(unique=True)
    city_id = PrimaryKeyField()
    closest_school = ForeignKeyField(School)
