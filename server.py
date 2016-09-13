from flask import Flask, render_template, request, session, redirect, url_for, g
from model_mentor import *


app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'pornislife'

@app.before_request
def login_user():
    g.user = None
    if 'user' in session:
        g.user = session['application_number']


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        all_data = {
            'City': request.form['City'],
            'Email': request.form['Email'],
            'Name': request.form['Name']
        }
        if not Applicant.check_if_email_is_used():
            city = City.get_by_name(all_data['City'])
            Applicant.create(name=all_data['Name'], city=city, email=all_data['Email'])

            return redirect(url_for(welcome, code=307))
    return render_template('/register.html', data=all_data )


@app.route('/', methods=['GET', 'POST'])
def welcome():
    successful = True
    if request.method == 'GET':
        successful = False
    return render_template("welcome.html", after_successfull=successful)


@app.route('/applicant/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Applicant.get_applicant(request.form['password'])
        if user.email == request.form['email']:
            session['application_number'] = user.application_number
            return redirect((url_for(status_of_application)))
    return render_template(url_for(login))


@app.route('/applicant/profile', methods=['GET', 'POST'])
def status_of_application():
    all_data = Applicant.get_applicant(session['application_number'])
    return render_template('profile.html', all_data=all_data)


@app.route('/applicant/interview', methods=['GET', 'POST'])
def status_of_interviews():
    all_data = Interview.select(date, time, Mentor.name, Mentor.school).join(Mentor).where(Applicant.application_number == session['application_number'])
    return render_template('profile.html', all_data=all_data)


@app.route('/about_us', methods=['GET', 'POST'])
def route_to_about_us():
    return render_template("about_us.html")


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('application_number', None)
    redirect(url_for(welcome))


