from selene import browser, have, command
from selenium.webdriver import Keys

from demoqa_tests import resource
from demoqa_tests.data.users import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.user_email = browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.user_number = browser.element('#userNumber')

        self.date_of_birth = browser.element('#dateOfBirthInput')

        self.subjects = browser.element('#subjectsInput')
        self.hobbies = browser.all('[for^=hobbies-checkbox]')

        self.current_address = browser.element('#currentAddress')
        self.menu_state = browser.element('#state')
        self.all_states = browser.all('[id^=react-select][id*=option]')
        self.menu_city = browser.element('#city')
        self.all_cities = browser.all('[id^=react-select][id*=option]')

        self.picture = browser.element('#uploadPicture')

        self.submit = browser.element('#submit')

        self.submitting_table = browser.element('#example-modal-sizes-title-lg')
        self.submitting_table_results = browser.element('.table').all('td').even

    def open(self):
        browser.open('/automation-practice-form')
        browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
            have.size_greater_than_or_equal(3)
        )
        browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def register(self, user: User):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.user_email.type(user.user_email)
        self.gender.element_by(have.value(user.gender.value)).element('..').click()
        self.user_number.type(user.user_number)

        self.date_of_birth.send_keys(Keys.CONTROL, 'a').type(user.date_of_birth.strftime('%m.%d.%Y')).press_enter()

        for subject in user.subjects:
            self.subjects.type(subject).press_enter()

        for hobby in user.hobbies:
            self.hobbies.element_by(have.text(hobby.value)).click()

        self.current_address.set_value(user.current_address)
        self.menu_state.click()
        self.all_states.element_by(have.exact_text(user.state)).click()
        self.menu_city.click()
        self.all_cities.element_by(have.exact_text(user.city)).click()
        self.picture.send_keys(resource.path(user.picture))

        self.submit.click()

    def should_have_registered(self, user: User):
        self.submitting_table.should(have.text('Thanks for submitting the form'))
        self.submitting_table_results.should(
            have.exact_texts(f'{user.first_name} {user.last_name}',
                             user.user_email,
                             user.gender.value,
                             user.user_number,
                             user.date_of_birth.strftime('%d %B,%Y'),
                             ', '.join(user.subjects),
                             ', '.join(list(map(lambda x: x.value, user.hobbies))),
                             user.picture,
                             user.current_address,
                             f'{user.state} {user.city}'
                             )
        )
