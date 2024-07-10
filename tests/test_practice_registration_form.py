from selene import browser, have, command
import os

import tests


def test_demoqa_practice_form():
    # GIVEN
    browser.open('/automation-practice-form')
    browser.all('[id^=google_ads][id$=container__]').with_(timeout=10).wait_until(
        have.size_greater_than_or_equal(3)
    )
    browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    # WHEN
    browser.element('#firstName').type('Viktoriia')
    browser.element('#lastName').type('Lav')
    browser.element('#userEmail').type('newuser@gmail.com')
    browser.all('[name=gender]').element_by(have.value('Female')).element('..').click()
    browser.element('#userNumber').type('8800222334')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').send_keys('1993')
    browser.element('.react-datepicker__month-select').all('option')[4].click()
    browser.element(f'.react-datepicker__day--0{17}:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').type('Chemistry').click().press_enter()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Sports')).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.exact_text('Reading')).click()

    browser.element('#currentAddress').with_(set_value_by_js=True).set_value('144 Broadway, suit 12')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Gurgaon')).click()

    browser.element('#uploadPicture').send_keys(os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), 'resources/photo.png')
    ))

    browser.element('#submit').click()

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts('Viktoriia Lav',
                                                                     'newuser@gmail.com',
                                                                     'Female',
                                                                     '8800222334',
                                                                     '17 May,1993',
                                                                     'Chemistry',
                                                                     'Sports, Reading',
                                                                     'photo.png',
                                                                     '144 Broadway, suit 12',
                                                                     'NCR Gurgaon'))

