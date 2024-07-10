from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    gender: str
    user_number: str
    date_of_birth: date
    subjects: tuple[str, ...]
    hobbies: tuple[str, ...]
    picture: str
    current_address: str
    state: str
    city: str


vika = User(
    first_name='Viktoriia',
    last_name='Lav',
    user_email='newuser@gmail.com',
    gender='Female',
    user_number='8800222334',
    date_of_birth=date(1993, 5, 17),
    subjects=('Chemistry',),
    hobbies=('Sports', 'Reading'),
    picture='photo.png',
    current_address='144 Broadway, suit 12',
    state='NCR',
    city='Gurgaon',
)

