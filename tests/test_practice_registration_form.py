from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data import users


def test_demoqa_practice_form():
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.register(users.vika)

    # THEN
    registration_page.should_have_registered(users.vika)
