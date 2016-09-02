from model_city import *
from model_applicant import *


class Inputhandler():
    @classmethod
    def check_inputs(cls, all_data):
        result = [[all_data['Name'], 'Correct'], [all_data['City'], 'Correct'], [all_data['Email'], 'Correct'] ]
        for letter in all_data['Name']:
            if not letter.isalpha():
                if letter != ' ':
                    result[0][1] = 'Incorrect'
        if '@' not in all_data['Email'] or '.' not in all_data['Email']:
            result[2][1] = 'Incorrect'
        elif all_data['City'] not in [city.name for city in City.get_all()]:
            result[1][1] = 'Incorrect'
        elif Applicant.check_if_email_is_used(all_data['Email']):
            result[2][1] = 'Already in use'
        return result
