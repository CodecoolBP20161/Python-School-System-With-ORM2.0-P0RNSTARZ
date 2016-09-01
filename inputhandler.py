from upload_data import list_of_cities


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
        if all_data['City'] not in list_of_cities:
            result[2][1] = 'Incorrect'
        return result
