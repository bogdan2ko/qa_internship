import allure
from pages.login_page import LoginPage
from conftest import USERNAME, PASSWORD

@allure.title("Позитивный логин")
def test_login_positive(browser):
    page = LoginPage(browser)
    page.open()

    page.set_username(USERNAME)
    page.set_password(PASSWORD)
    page.submit()

    assert page.is_logged_in(), "В системе не появилась ссылка Logout – логин неуспешен"
