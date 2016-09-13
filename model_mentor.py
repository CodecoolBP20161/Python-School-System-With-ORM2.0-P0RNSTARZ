from model_slotmentor import *


class Mentor(BaseModel):

    name = CharField()
    mentor_id = PrimaryKeyField()
    school = ForeignKeyField(School)
    email = CharField()
