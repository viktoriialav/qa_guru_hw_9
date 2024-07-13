import os

from selene import browser, have, command

import tests


class RegistrationPage:
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

    def fill_gender(self, item):
        browser.all('[name=gender]').element_by(have.value(item)).element('..').click()

    def fill_user_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, value):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').send_keys(value.year)
        browser.element('.react-datepicker__month-select').all('option')[value.month - 1].click()
        browser.element(f'.react-datepicker__day--0{value.day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value).click().press_enter()

    def fill_hobbies(self, value):
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

    def should_have_registered(self, full_name, user_email, gender, user_number, date_of_birth, subjects, hobbies,
                               picture, current_address, state_and_city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(full_name,
                             user_email,
                             gender,
                             user_number,
                             date_of_birth.strftime('%d %B,%Y'),
                             subjects,
                             hobbies,
                             picture,
                             current_address,
                             state_and_city
                             )
        )
