from dataclasses import dataclass
from datetime import date
from enum import Enum


class Hobby(Enum):
    sports = 'Sports'
    reading = 'Reading'
    music = 'Music'


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


@dataclass
class User:
    first_name: str
    last_name: str
    user_email: str
    # gender: Gender
    gender: str
    user_number: str
    date_of_birth: date
    subjects: tuple[str, ...]
    # hobbies: tuple[Hobby, ...]
    hobbies: tuple[str, ...]
    picture: str
    current_address: str
    state: str
    city: str


vika = User(
    first_name='Viktoriia',
    last_name='Lav',
    user_email='newuser@gmail.com',
    # gender=Gender.female,
    gender='Female',
    user_number='8800222334',
    date_of_birth=date(1993, 5, 17),
    subjects=('Chemistry',),
    # hobbies=(Hobby.sports, Hobby.reading),
    hobbies=('Sports', 'Reading'),
    picture='photo.png',
    current_address='144 Broadway, suit 12',
    state='NCR',
    city='Gurgaon',
)
