from basemodel import *
from model_school import *
from model_city import *
from model_applicant import *
from model_mentor import *
from model_interview import *
from model_interviewslot import *
from model_slotmentor import *


db.connect()

db.drop_tables([School, City, Applicant, Mentor, Interview, InterviewSlot, SlotMentor], safe=True)
db.create_tables([School, City, Applicant, Mentor, Interview, InterviewSlot, SlotMentor], safe=True)
