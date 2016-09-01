from basemodel import *


class School(BaseModel):

    school_id = PrimaryKeyField()
    name = CharField()
