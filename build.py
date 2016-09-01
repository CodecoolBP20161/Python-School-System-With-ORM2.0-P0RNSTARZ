from basemodel import *
from model_school import *
from model_city import *
from model_applicant import *


db.connect()

db.create_tables([School, City, Applicant], safe=True)
