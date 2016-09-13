from model_applicant import *


class Interview(BaseModel):

    int_id = PrimaryKeyField()
    applicant = ForeignKeyField(Applicant)
    slot = ForeignKeyField(InterviewSlot)
