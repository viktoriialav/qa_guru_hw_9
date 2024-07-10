import os

from selene import browser, have, command

import tests
from demoqa_tests.data.users import User


class RegistrationPage:
    def __init__(self):
        pass

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_user_email(self, value):
        browser.element('#userEmail').type(value)

    def fill_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, value):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(value.year)
        browser.element('.react-datepicker__month-select').all('option')[value.month - 1].click()
        browser.element(f'.react-datepicker__day--0{value.day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subjects(self, values):
        for value in values:
            browser.element('#subjectsInput').type(value).click().press_enter()

    def fill_hobbies(self, values):
        for value in values:
            browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text(value)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').send_keys(os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), f'resources/{value}')
        ))

    def fill_current_address(self, value):
        browser.element('#currentAddress').with_(set_value_by_js=True).set_value(value)

    def fill_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def fill_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.exact_text(value)).click()

    def submit(self):
        browser.element('#submit').click()

    def should_have_submitting_form(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def should_have_registered(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(f'{user.first_name} {user.last_name}',
                             user.user_email,
                             user.gender,
                             user.user_number,
                             f'{user.date_of_birth.day} {user.date_of_birth.strftime("%B")},{user.date_of_birth.year}',
                             ', '.join(user.subjects),
                             ', '.join(user.hobbies),
                             user.picture,
                             user.current_address,
                             f'{user.state} {user.city}'
                             )
        )
