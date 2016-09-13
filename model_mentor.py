from basemodel import *
from model_school import *


class Mentor(BaseModel):

    name = CharField()
    mentor_id = PrimaryKeyField()
    school = ForeignKeyField(School)
    email = CharField()
