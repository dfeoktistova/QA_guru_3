from fixtures import open_home_page
from selene import browser, be, have


def test_search_positive(open_home_page):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_search_negative(open_home_page):
    request = 'isHunx;leUkjxhksenn&g%76237529jRR'
    browser.element('[name="q"]').should(be.blank).type(request).press_enter()
    browser.element('[id="botstuff"]').should(have.text(f'Your search - {request} - did not match any documents'))
