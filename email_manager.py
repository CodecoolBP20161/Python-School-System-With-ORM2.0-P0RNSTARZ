import smtplib
from messages import *


class EmailManager():

    def send_email(self, student, message_to_student):

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('codecoolrobot@gmail.com', 'codecoolrobot1')
        server.sendmail("codecoolrobot@gmail.com", student, message_to_student)

message_to_student = '''Dear %s,\nYour application_number is %s.\nYou can use it to log in, and check your interviews.'''
message_to_us = '''cso'''
