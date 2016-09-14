from basemodel import *
from model_school import *
from model_applicant import *

class InterviewSlot(BaseModel):

    slot_id = PrimaryKeyField()
    date = DateField()
    time = TimeField()
