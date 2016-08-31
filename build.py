from applicant import *
from city import *

db.connect()
# db.drop_tables([], safe=True)  # for testing
db.create_tables([School, City, Applicant], safe=True)
