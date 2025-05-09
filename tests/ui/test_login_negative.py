# tests/ui/test_login_negative.py
import pytest
import allure
from pages.login_page import LoginPage
from conftest import USERNAME, PASSWORD

invalid_cases = [
    pytest.param(USERNAME, "wrong_pass", id="wrong password"),
    pytest.param("", PASSWORD, id="empty username"),
    pytest.param(USERNAME, "", id="empty password"),
]


@allure.title("Негативные сценарии логина")
@pytest.mark.parametrize("username,password", invalid_cases)
def test_login_negative(browser, username, password):
    page = LoginPage(browser)
    page.open()

    page.set_username(username)
    page.set_password(password)
    page.submit()

    # главное условие: ссылка Logout/Logoff не появилась
    assert not page.is_logged_in(), "Должны остаться без авторизации"
