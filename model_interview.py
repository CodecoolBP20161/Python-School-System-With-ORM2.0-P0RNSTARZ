from basemodel import *
from model_interviewslot import *


class Interview(BaseModel):

    int_id = PrimaryKeyField()
    applicant = ForeignKeyField(Applicant)
    slot = ForeignKeyField(InterviewSlot)
