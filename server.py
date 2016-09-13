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
        if not check_results:
            city = City.get_by_name(all_data['City'])
            Applicant.create(name=all_data['Name'], city=city, email=all_data['Email'])
            return redirect(url_for...)
    else:
        check_results = False
    return render_template('/register.html', data=check_results)


@app.route('/', methods=['GET'])
def welcome():
    return render_template("welcome.html")


@app.route('/applicant/login', methods=['GET, POST'])
def login():
    pass


@app.route('/applicant/profile', methods=['GET, POST'])
def status_of_application():
    pass


@app.route('/applicant/interview', methods=['GET, POST'])
def status_of_interviews():
    pass


@app.route('/about_us', methods=['GET, POST'])
def route_to_about_us():
    return render_template("about_us.html")
