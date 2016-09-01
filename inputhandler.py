from model_city import *


class Inputhandler():
    @classmethod
    def check_inputs(cls, all_data):
        result = [[all_data['Name'], 'Correct'], [all_data['Email'], 'Correct'], [all_data['City'], 'Correct']]
        for letter in all_data['Name']:
            if letter.isalpha() is False:
                if letter != ' ':
                    result[0][1] = 'Incorrect'

        if '@' not in all_data['Email'] or '.' not in all_data['Email']:
            result[1][1] = 'Incorrect'
        if all_data['City'] not in City.get_all():
            result[2][1] = 'Incorrect'
        return result
