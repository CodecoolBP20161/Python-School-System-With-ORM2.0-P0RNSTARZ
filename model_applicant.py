from model_mentor import *
from email_manager import *
from model_city import *
from model_interviewslot import *
import string
import random


class Applicant(BaseModel):

    applicant_id = PrimaryKeyField()
    application_number = CharField(unique=True, null=True)
    name = CharField()
    city = ForeignKeyField(City)
    status = CharField(default='New')
    email = CharField(unique=True)
    school = ForeignKeyField(School, null=True)

    @classmethod
    def find_missing_attr(cls, attribute):
        return cls.select().where(attribute >> None)

    @classmethod
    def code_check(cls, code):
        return cls.select().where(cls.application_number == code).exists()

    @classmethod
    def generate_unique(cls, list_of_students):
        for student in list_of_students:
            unique_not_found = True
            while unique_not_found:
                unique_code = ''.join([random.choice(string.ascii_uppercase) for x in range(6)])
                unique_not_found = cls.code_check(unique_code)
            student.application_number = unique_code
            student.save()

    @classmethod
    def find_school(cls, list_of_students):
        for student in list_of_students:
            student.school = student.city.closest_school
            student.save()

    @classmethod
    def find_new_applicants(cls):
        return cls.select().where(cls.status == 'New', cls.school >> None, cls.application_number >> None)

    @classmethod
    def modify_status(cls, list_of_students):
        manager = EmailManager()
        for student in list_of_students:
            student.status = 'Waiting for interview'
            student.save()
            manager.send_email(student)

    @classmethod
    def check_if_email_is_used(cls, email):
        return cls.select().where(cls.email == email).exists()

    @classmethod
    def get_applicant(cls, email):
        return cls.select().where(cls.email == email).get()

    @classmethod
    def find_missing_interview(cls):
        return cls.select().where(cls.status == 'New')

    def get_mentors(self):
        mentors = Mentor.select().join(
            City, on=City.closest_school == Mentor.school
        ).join(
            self.__class__, on=City.name == self.__class__.city
        ).where(self.__class__.application_number == self.application_number)
        return [mentor for mentor in mentors]

    def appoint_interview(self):
        query = SlotMentor.select()
        query = SlotMentor.select().join(
            Mentor).switch(SlotMentor).where(Mentor.school == instance.school.name, SlotMentor.applicant >> None)
        the_list = []
        for obj in query:
            the_list.append([obj.SM_id, obj.slot, obj.mentor])
        all_data = random.choice(the_list)
        mslot1 = all_data[0]
        islot = all_data[1]
        men1 = all_data[2]
        query2 = SlotMentor.select().join(
            Mentor).where(
            Mentor.school == instance.school.name,
            SlotMentor.slot == islot, SlotMentor.mentor != men1, SlotMentor.applicant >> None)
        the_list2 = []
        for obj in query2:
            the_list2.append([obj.SM_id, obj.slot, obj.mentor])
        all_data2 = random.choice(the_list2)
        men2 = all_data2[2]
        mslot2 = all_data2[0]
        Interview.create(
            applicant=instance,
            slot=InterviewSlot.get(InterviewSlot.slot_id == islot.slot_id)
            )
        self.status = "In progress"
        self.save()
        menslot1 = SlotMentor.get(SlotMentor.SM_id == mslot1)
        menslot1.applicant = instance
        menslot1.save()
        menslot2 = SlotMentor.get(SlotMentor.SM_id == mslot2)
        menslot2.applicant = instance
        menslot2.save()
