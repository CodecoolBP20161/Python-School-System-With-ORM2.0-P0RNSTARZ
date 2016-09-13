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
    email = CharField()
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
    def get_applicant(cls, application_code):
        return cls.select().where(cls.application_number == application_code).get()

    @classmethod
    def find_missing_interview(cls):
        return cls.select().where(cls.status == 'New')

    @classmethod
    def find_interview(cls, number):
        app = cls.select().join(InterviewSlot).join(Mentor).where(cls.application_number == number).get()
        slot = InterviewSlot.select().join(cls).where(cls.application_number == number).get()
        men = Mentor.select().join(InterviewSlot, JOIN.RIGHT_OUTER).join(cls).where(cls.application_number == number).get()
        return [app.school_id, slot.time, slot.hour, men.name]

    @classmethod
    def find_mentors(cls, number):
        mentors = Mentor.select().join(City, on=City.closest_school == Mentor.school).join(cls, on=City.name == Applicant.city).where(cls.application_number == number)
        return [mentor.name for mentor in mentors]

    def get_mentors(self):
        mentors = Mentor.select().join(
            City, on=City.closest_school == Mentor.school
        ).join(
            self.__class__, on=City.name == self.__class__.city
        ).where(self.__class__.application_number == self.application_number)
        return [mentor.name for mentor in mentors]

