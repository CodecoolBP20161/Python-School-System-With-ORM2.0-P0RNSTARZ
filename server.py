from flask import Flask, render_template
import requests
from inputhandler import *

app = Flask(__name__)


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if requests.methods = 'POST':
        all_data = requests.form
        all_info = check_inputs(all_data)
        return render_template('/register.html', data=all_info)

    else:
        return render_template('/register.html')
