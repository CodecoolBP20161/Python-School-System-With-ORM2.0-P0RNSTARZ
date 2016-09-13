from basemodel import *
from model_school import *


class InterviewSlot(BaseModel):

    slot_id = PrimaryKeyField()
    date = DateField()
    time = TimeField()
