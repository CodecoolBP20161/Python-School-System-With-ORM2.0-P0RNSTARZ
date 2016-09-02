from model_applicant import *


class Inputhandler():
    @classmethod
    def check_inputs(cls, all_data):
        results = [[all_data['Name'], 'Correct'], [all_data['City'], 'Correct'], [all_data['Email'], 'Correct'], [True, 'Correct']]
        for letter in all_data['Name']:
            if not letter.isalpha():
                if letter != ' ':
                    results[0][1] = 'Incorrect'
        if '@' not in all_data['Email'] or '.' not in all_data['Email']:
            results[2][1] = 'Incorrect'
        elif all_data['City'] not in [city.name for city in City.get_all()]:
            results[1][1] = 'Incorrect'
        elif Applicant.check_if_email_is_used(all_data['Email']):
            results[2][1] = 'Already in use'
        for result in results:
            if result[1] == 'Correct':
                pass
            else:
                results[3][0] = False
                break
        return results
