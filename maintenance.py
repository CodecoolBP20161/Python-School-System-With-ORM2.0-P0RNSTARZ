from applicant import *
from city import *


# adds unique applicaton codes to those who doesn't have
Applicant.generate_unique(Applicant.find_missing_app_num())

# finds the closest school based on the city where the applicant lives (for everyone)
Applicant.find_school(Applicant.find_missing_city())
