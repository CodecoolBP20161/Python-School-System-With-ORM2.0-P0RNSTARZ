from school import *
from random import *
from string import *


class Applicant(BaseModel):

    applicant_id = PrimaryKeyField()
    application_number = CharField(unique=True, null=True)
    name = CharField()  # given
    city = CharField()  # given
    status = CharField(default='New')
    email = CharField()  # given
    school = ForeignKeyField(School, null=True)

    @classmethod
    def find_missing_app_num(cls):
        return cls.select().where(cls.application_number >> None)

    @classmethod
    def generate_unique(cls, list_of_applicants):
        for applicant in list_of_applicants:
            list_of_letters = string.ascii_uppercase
            list_of_numbers = list(range(10))
            list_of_chars = []
            for character in range(6):
                list_of_chars.append(random.choice(random.choice([list_of_numbers, list_of_letters])))
                return list_of_chars

            unique_code = ''.join(list_of_chars)
            applicant.application_number = unique_code
            applicant.save()
