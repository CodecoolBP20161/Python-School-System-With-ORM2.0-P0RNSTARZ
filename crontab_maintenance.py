from model_applicant import *


# adds uniqe applicaton codes to those who doesnt have
Applicant.generate_uniqe(Applicant.find_missing_attr(Applicant.application_number))

# finds the closest school based on the city where the applicant lives (for everyone)
Applicant.find_school(Applicant.find_missing_attr(Applicant.city))

# finds the closest school based on the city where the applicant lives (for everyone)
Applicant.modify_status(Applicant.find_new_applicants())
