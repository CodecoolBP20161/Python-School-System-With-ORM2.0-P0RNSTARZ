import smtplib
from messages import *


class EmailManager():

    def send_email(self, student, message_to_student, message_to_us):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('codecoolrobot@gmail.com', 'codecoolrobot1')
        try:
            message = message_to_student % (student.name, student.application_number, student.school.name)
            server.sendmail("codecoolrobot@gmail.com", student.email, message)
        except:
            message = message_to_us % (student.name)
            server.sendmail("codecoolrobot@gmail.com", "codecoolrobot@gmail.com", message)
