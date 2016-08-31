from base_model import *
from school import *
from city import *
from applicant import *

bp1 = School.create(
    name='BP1'
)

bp2 = School.create(
    name='BP2'
)

miskolc1 = School.create(
    name='Miskolc1'
)

City.create(
    name='Horcsoghalom',
    closest_school=miskolc1
)

City.create(
    name='Karancspuszta',
    closest_school=miskolc1
)

City.create(
    name='Budapest',
    closest_school=bp1
)

nintendo = Applicant.create(
    name='Lakatos Nintendo',
    city='Karancspuszta',
    email='sukargyerek@gmail.com'
)
