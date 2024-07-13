from datetime import date

from demoqa_tests.pages.registration_page import RegistrationPage


def test_demoqa_practice_form():
    # GIVEN
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Viktoriia')
    registration_page.fill_last_name('Lav')
    registration_page.fill_user_email('newuser@gmail.com')
    registration_page.fill_gender('Female')
    registration_page.fill_user_number('8800222334')

    registration_page.fill_date_of_birth(date(1993, 5, 17))

    registration_page.fill_subjects('Chemistry')
    registration_page.fill_hobbies('Sports')
    registration_page.fill_hobbies('Reading')

    registration_page.upload_picture('photo.png')

    registration_page.fill_current_address('144 Broadway, suit 12')
    registration_page.fill_state('NCR')
    registration_page.fill_city('Gurgaon')

    registration_page.submit()

    # THEN
    registration_page.should_have_submitting_form()
    registration_page.should_have_registered('Viktoriia Lav',
                                             'newuser@gmail.com',
                                             'Female',
                                             '8800222334',
                                             date(1993, 5, 17),
                                             'Chemistry',
                                             'Sports, Reading',
                                             'photo.png',
                                             '144 Broadway, suit 12',
                                             'NCR Gurgaon')

