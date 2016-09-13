from basemodel import *
from model_interviewslot import *
from model_applicant import *
from model_mentor import *


class SlotMentor(BaseModel):

    SM_id = PrimaryKeyField()
    mentor = ForeignKeyField(Mentor)
    slot = ForeignKeyField(InterviewSlot)
    applicant = ForeignKeyField(Applicant, null=True)
