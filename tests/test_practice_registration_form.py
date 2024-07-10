
from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage


def test_demoqa_practice_form():
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()
    vika = users.vika

    # WHEN
    registration_page.fill_first_name(vika.first_name)
    registration_page.fill_last_name(vika.last_name)
    registration_page.fill_user_email(vika.user_email)
    registration_page.fill_gender(vika.gender)
    registration_page.fill_user_number(vika.user_number)

    registration_page.fill_date_of_birth(vika.date_of_birth)

    registration_page.fill_subjects(vika.subjects)
    registration_page.fill_hobbies(vika.hobbies)

    registration_page.upload_picture(vika.picture)

    registration_page.fill_current_address(vika.current_address)
    registration_page.fill_state(vika.state)
    registration_page.fill_city(vika.city)

    registration_page.submit()

    # THEN
    registration_page.should_have_submitting_form()
    registration_page.should_have_registered(vika)

