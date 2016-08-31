from base_model import *


class School(BaseModel):

    name = CharField(unique=True)
    school_id = PrimaryKeyField()
