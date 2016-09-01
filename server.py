from flask import Flask, render_template, request
from inputhandler import *
from model_applicant import *
from model_city import *


app = Flask(__name__)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        all_data = {
            'City': request.form['City'],
            'Email': request.form['Email'],
            'Name': request.form['Name']
        }
        check_results = Inputhandler.check_inputs(all_data)
        for result in check_results:
            correct = True
            if result[1] == 'Correct':
                pass
            else:
                correct = False
                break
        if correct:
            print('3')
            city = City.get_by_name(all_data['City'])
            print()
            Applicant.create(name=all_data['Name'], city=city, email=all_data['Email'])
            return render_template('/register.html', data=[['', ''], ['', ''], ['', '']])

        return render_template('/register.html', data=check_results)

    else:
        return render_template('/register.html', data=[['', ''], ['', ''], ['', '']])
