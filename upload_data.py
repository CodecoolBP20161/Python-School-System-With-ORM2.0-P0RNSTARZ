from model_school import *
from model_city import *
from model_applicant import *
from model_mentor import *
from model_interview import *
from model_interviewslot import *
from model_slotmentor import *
import random
from datetime import date, time

list_of_cities = [
    'New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia', 'Phoenix', 'San Antonio', 'San Diego', 'Dallas',
    'San Jose', 'Austin', 'Jacksonville', 'San Francisco', 'Indianapolis', 'Columbus', 'Fort Worth', 'Charlotte',
    'Seattle', 'Denver', 'El Paso', 'Detroit', 'Washington', 'Boston', 'Memphis', 'Nashville', 'Portland',
    'Oklahoma City', 'Las Vegas', 'Baltimore', 'Louisville', 'Milwaukee', 'Albuquerque', 'Tucson', 'Fresno',
    'Sacramento', 'Kansas City', 'Long Beach', 'Mesa', 'Atlanta', 'Colorado Springs', 'Virginia Beach',
    'Raleigh', 'Omaha', 'Miami', 'Oakland', 'Minneapolis', 'Tulsa', 'Wichita', 'New Orleans', 'Arlington', 'Cleveland',
    'Bakersfield', 'Tampa', 'Aurora', 'Honolulu', 'Anaheim', 'Santa Ana', 'Corpus Christi', 'Riverside', 'St. Louis',
    'Lexington', 'Stockton', 'Pittsburgh', 'Saint Paul', 'Anchorage', 'Cincinnati', 'Henderson', 'Greensboro', 'Plano',
    'Newark', 'Toledo', 'Lincoln', 'Orlando', 'Chula Vista', 'Jersey City', 'Chandler', 'Fort Wayne', 'Buffalo',
    'Durham', 'St. Petersburg', 'Irvine', 'Laredo', 'Lubbock', 'Madison', 'Gilbert', 'Norfolk', 'Reno', 'Winston–Salem',
    'Glendale', 'Hialeah', 'Garland', 'Scottsdale', 'Irving', 'Chesapeake', 'North Las Vegas', 'Fremont', 'Baton Rouge',
    'Richmond', 'Boise', 'San Bernardino', 'Spokane', 'Birmingham', 'Modesto', 'Des Moines', 'Rochester', 'Tacoma',
    'Fontana', 'Oxnard', 'Moreno Valley', 'Fayetteville', 'Huntington Beach', 'Yonkers',
    'Montgomery', 'Amarillo', 'Little Rock', 'Akron', 'Shreveport', 'Augusta', 'Grand Rapids', 'Mobile',
    'Salt Lake City', 'Huntsville', 'Tallahassee', 'Grand Prairie', 'Overland Park', 'Knoxville', 'Worcester',
    'Brownsville', 'Newport News', 'Santa Clarita', 'Port St. Lucie', 'Providence', 'Fort Lauderdale', 'Chattanooga',
    'Tempe', 'Oceanside', 'Garden Grove', 'Rancho Cucamonga', 'Cape Coral', 'Santa Rosa', 'Vancouver', 'Sioux Falls',
    'Peoria', 'Ontario', 'Jackson', 'Elk Grove', 'Springfield', 'Pembroke Pines', 'Salem', 'Corona', 'Eugene',
    'McKinney', 'Fort Collins', 'Lancaster', 'Cary', 'Palmdale', 'Hayward', 'Salinas', 'Frisco', 'Springfield',
    'Pasadena', 'Macon', 'Alexandria', 'Pomona', 'Lakewood', 'Sunnyvale', 'Escondido', 'Kansas City', 'Hollywood',
    'Clarksville', 'Torrance', 'Rockford', 'Joliet', 'Paterson', 'Bridgeport', 'Naperville', 'Savannah', 'Mesquite',
    'Syracuse', 'Pasadena', 'Orange', 'Fullerton', 'Killeen', 'Dayton', 'McAllen', 'Bellevue', 'Miramar', 'Hampton',
    'West Valley City', 'Warren', 'Olathe', 'Columbia', 'Thornton', 'Carrollton', 'Midland', 'Charleston', 'Waco',
    'Sterling Heights', 'Denton', 'Cedar Rapids', 'New Haven', 'Roseville', 'Gainesville', 'Visalia', 'Coral Springs',
    'Thousand Oaks', 'Elizabeth', 'Stamford', 'Concord', 'Surprise', 'Lafayette', 'Topeka', 'Kent', 'Simi Valley',
    'Santa Clara', 'Murfreesboro', 'Hartford', 'Athens', 'Victorville', 'Abilene', 'Vallejo', 'Berkeley', 'Norman',
    'Allentown', 'Evansville', 'Columbia', 'Odessa', 'Fargo', 'Beaumont', 'Independence', 'Ann Arbor', 'El Monte',
    'Springfield', 'Round Rock', 'Wilmington', 'Arvada', 'Provo', 'Peoria', 'Lansing', 'Downey', 'Carlsbad',
    'Costa Mesa', 'Miami Gardens', 'Westminster', 'Clearwater', 'Fairfield', 'Rochester', 'Elgin', 'Temecula',
    'West Jordan', 'Inglewood', 'Richardson', 'Lowell', 'Gresham', 'Antioch', 'Cambridge', 'High Point', 'Billings',
    'Manchester', 'Murrieta', 'Centennial', 'Richmond', 'Ventura', 'Pueblo', 'Pearland', 'Waterbury', 'West Covina',
    'North Charleston', 'Everett', 'College Station', 'Palm Bay', 'Pompano Beach', 'Boulder', 'Norwalk',
    'West Palm Beach', 'Broken Arrow', 'Daly City', 'Sandy Springs', 'Burbank', 'Green Bay', 'Santa Maria',
    'Wichita Falls', 'Lakeland', 'Clovis', 'Lewisville', 'Tyler', 'El Cajon', 'San Mateo', 'Rialto', 'Edison',
    'Davenport', 'Hillsboro', 'Woodbridge', 'Las Cruces', 'South Bend', 'Vista', 'Greeley', 'Davie', 'San Angelo',
    'Jurupa Valley', 'Renton'
    ]
list_of_cities = list(set(list_of_cities))
list_of_schools = ['SF', 'NYC', 'WDC', 'LA']

schools = []

for school in list_of_schools:
    x = School.create(name=school)
    schools.append(x)

for city in list_of_cities:
    City.create(name=city, closest_school=random.choice(schools))

surnames = ['Smith', 'Anderson', 'Clark', 'Wright', 'Mitchell', 'Johnson', 'Thomas', 'Rodriguez', 'Lopez', 'Perez',
            'Williams', 'Jackson', 'Lewis', 'Hill', 'Roberts', 'Jones', 'White', 'Lee', 'Scott', 'Turner', 'Brown',
            'Harris', 'Walker', 'Green', 'Phillips', 'Davis', 'Martin', 'Hall', 'Adams', 'Campbell', 'Miller',
            'Thompson',  'Allen', 'Baker', 'Parker', 'Wilson', 'Garcia', 'Young', 'Gonzalez', 'Evans', 'Moore',
            'Martinez', 'Hernandez', 'Nelson', 'Edwards', 'Taylor', 'Robinson', 'King', 'Carter', 'Collins']

first_names = ['James', 'Christopher', 'Ronald', 'Mary', 'Lisa', 'Michelle', 'John', 'Daniel', 'Anthony',
               'Patricia', 'Nancy', 'Laura',
               'Robert', 'Paul', 'Kevin', 'Linda', 'Karen', 'Sara', 'Michael',
               'Mark', 'Jason', 'Barbara', 'Betty', 'Kimberly', 'William', 'Donald', 'Jeff', 'Elizabeth',
               'Helen', 'Debora', 'David',
               'George', 'Jennifer', 'Sandra', 'Richard', 'Kenneth', 'Maria',
               'Donn', 'Charles', 'Steven', 'Susan', 'Caro', 'Josephine', 'Edward',
               'Margaret', 'Ruth', 'Thomas', 'Brian', 'Dorothy', 'Sharon']

# Creating lots of random mentors to work with
mentors = []
for x in range(28):
    if x <= 7:
        school = schools[0]
    elif x <= 14:
        school = schools[1]
    elif x <= 21:
        school = schools[2]
    else:
        school = schools[3]
    surname = random.choice(surnames)
    first_name = random.choice(first_names)
    email = str(surname[:3] + first_name[:3])
    new_mentor = Mentor.create(
        name=surname + ' ' + first_name,
        school=school,
        email='%s@gmail.com' % email
    )
    mentors.append(new_mentor)

hour = 9
day = 10
interview_slots = []
# Creating interview time slots
while hour != 14 and day != 14:
    new_slot = InterviewSlot.create(
        date=date(2016, 10, day),
        time=time(hour, 0)
    )
    interview_slots.append(new_slot)
    hour += 1
    if hour == 14:
        day += 1
        hour = 9

# assigning the mentors to each date
for mentor in mentors:
    for slot in interview_slots:
        SlotMentor.create(
            mentor=mentor,
            slot=slot
            )
