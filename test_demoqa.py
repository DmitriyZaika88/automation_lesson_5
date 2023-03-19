from selene import browser, have, be, command
import os
from selenium.webdriver.common.keys import Keys


def test_registration(browser_settings):
    browser.open('https://demoqa.com/automation-practice-form')

    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.element('footer').execute_script('element.remove()')

    browser.element('#firstName').type('Abra')
    browser.element('#lastName').type('Kadabra')
    browser.element('#userEmail').type('abrakadabra@gmail.com')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').type('9211234567')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select>option[value="5"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1997"]').click()
    browser.element('[aria-label="Choose Monday, June 30th, 1997"]').click()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').click()
    browser.element('#subjectsInput').send_keys('Arts')
    browser.element('#subjectsInput').press(Keys.TAB)
    browser.driver.execute_script('window.scrollBy(0, 100)')
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/wings.jpg')
    browser.element('#currentAddress').should(be.blank).type("baker st 221b")
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').click()
    browser.element('#submit').perform(command.js.click)

    # assertions
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('//tbody/tr[1]/td[2]').should(have.text('Abra Kadabra'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('abrakadabra@gmail.com'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('9211234567'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('30 June,1997'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('Arts'))
    browser.element('//tbody/tr[7]/td[2]').should(have.exact_text('Sports'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('wings.jpg'))
    browser.driver.execute_script('window.scrollBy(0, 100)')
    browser.element('//tbody/tr[9]/td[2]').should(have.text('baker st 221b'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Uttar Pradesh Lucknow'))
    browser.element('[id="closeLargeModal"]').perform(command.js.click)
