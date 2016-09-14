from flask import Flask, render_template, request, session, redirect, url_for, g
from model_mentor import *
from model_applicant import *
from model_school import *
from model_city import *
from model_interviewslot import *
from model_interview import *
from model_slotmentor import *


app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'pornislife'


@app.before_request
def login_user():
    g.user = None
    if 'application_number' in session:
        g.user = session['application_number']


@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        all_data = {
            'City': request.form['City'],
            'Email': request.form['Email'],
            'Name': request.form['Name']
        }
        if not Applicant.check_if_email_is_used(request.form['Email']):
            city = City.get_by_name(all_data['City'])
            Applicant.create(name=all_data['Name'], city=city, email=all_data['Email'])
            Applicant.generate_unique(Applicant.find_missing_attr(Applicant.application_number))
            Applicant.find_school(Applicant.find_missing_attr(Applicant.school))
            Applicant.modify_status(Applicant.find_new_applicants())
            user = Applicant.select().where(Applicant.email == all_data['Email']).get()
            SlotMentor.assign_to_applicant(user)
            return redirect(url_for('welcome', code=307))
    else:
        all_data = False
    return render_template('/register.html', data=all_data)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'GET':
        return render_template("welcome.html", after_successfull=False)
    return render_template("welcome.html", after_successfull=True)


@app.route('/applicant/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = Applicant.get_applicant(request.form['password'])
        if user.email == request.form['email']:
            session['application_number'] = user.application_number
            return redirect((url_for('status_of_application')))
        else:
            data = [request.form['email'], request.form['password']]
    else:
        data = False
    return render_template('login.html', data=data)


@app.route('/applicant/profile', methods=['GET', 'POST'])
def status_of_application():
    if g.user:
        title = "Profile"
        all_data = Applicant.get_applicant(session['application_number'])
        return render_template('profile.html', all_data=all_data, title=title)
    else:
        return redirect(url_for('welcome'))


@app.route('/applicant/interview', methods=['GET'])
def status_of_interviews():
    if g.user:
        title = "Interview"
        applicant = Applicant.select().where(Applicant.application_number == session['application_number']).get()
        interview = Interview.select().where(Interview.applicant == applicant).get()
        time = interview.slot.time
        date = interview.slot.date
        school = Applicant.select().where(Applicant.application_number == session['application_number']).get().school.name
        sms = SlotMentor.select().where(SlotMentor.applicant == applicant)
        mentors = []
        for sm in sms:
            mentors.append(sm.mentor.name)
        return render_template('interview.html', time=time, date=date, school=school, mentors=mentors, title=title)
    else:
        return redirect(url_for('welcome'))


@app.route('/about_us', methods=['GET'])
def route_to_about_us():
    if g.user:
        return render_template("about.html")
    else:
        return redirect(url_for('welcome'))


@app.route('/logout', methods=['POST'])
def logout():
    session.pop('application_number', None)
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run(debug=True)
