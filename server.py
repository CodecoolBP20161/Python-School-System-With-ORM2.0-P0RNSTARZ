from flask import Flask, render_template, request
from inputhandler import *

app = Flask(__name__)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.methods == 'POST':
        all_data = request.form
        check_results = Inputhandler.check_inputs(all_data)
        for result in check_results:
            correct = True
            if result[1] == 'Correct':
                pass
            else:
                correct = False
                break
        if correct:
            return render_template('/register.html')

        return render_template('/register.html', data=check_results)

    else:
        return render_template('/register.html')
