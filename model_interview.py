from basemodel import *
from model_interviewslot import *
from model_applicant import *


class Interview(BaseModel):

    int_id = PrimaryKeyField()
    applicant = ForeignKeyField(Applicant)
    slot = ForeignKeyField(InterviewSlot)
