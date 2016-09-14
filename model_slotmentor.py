from basemodel import *
from model_interviewslot import *
from model_applicant import *
from model_mentor import *
from model_interview import *


class SlotMentor(BaseModel):

    SM_id = PrimaryKeyField()
    mentor = ForeignKeyField(Mentor)
    slot = ForeignKeyField(InterviewSlot)
    applicant = ForeignKeyField(Applicant, null=True)

    @classmethod
    def assign_to_applicant(cls, applicant):

        '''
        select a.slot_id, a.mentor_id, b.mentor_id, b.slot_id from slotmentor as a
        join mentor as ma on a.mentor_id = ma.mentor_id
        join slotmentor as b on a.slot_id = b.slot_id and a.mentor_id != b.mentor_id
        join mentor as mb on b.mentor_id = mb.mentor_id
        where ma.school_id = mb.school_id
        '''

        SecondMentor = Mentor.alias()
        SecondSlotMentor = SlotMentor.alias()
        first_sm = cls.select(
            ).join(
            Mentor, on=SlotMentor.mentor == Mentor.mentor_id
            ).join(
            SecondSlotMentor, on=((SlotMentor.slot == SecondSlotMentor.slot) & (SlotMentor.mentor != SecondSlotMentor.mentor))
            ).join(
            SecondMentor, on=(SecondSlotMentor.mentor == SecondMentor.mentor_id)
            ).where(
            Mentor.school == applicant.school).order_by(fn.Random()).limit(1).get()
        Interview.create(
            applicant=applicant,
            slot=first_sm.slot
            )
        first_sm.applicant = applicant
        first_sm.save()
        second_sm = cls.select(
            ).join(
            Mentor, on=SlotMentor.mentor == Mentor.mentor_id
            ).where(
            SlotMentor.slot == first_sm.slot, SlotMentor.mentor != first_sm.mentor, Mentor.school == first_sm.mentor.school).order_by(fn.Random()).limit(1).get()
        second_sm.applicant = applicant
        second_sm.save()
