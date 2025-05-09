import allure
import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password",
                         [("wrong_user", "wrong_pass"),
                          ("", "some_pass"),
                          ("student", "")])
@allure.title("Негативные сценарии логина")
def test_login_negative(browser, username, password):
    page = LoginPage(browser)
    page.open()
    page.set_username(username)
    page.set_password(password)
    page.submit()

    assert "login error" in browser.page_source.lower() \
           or "warning" in browser.page_source.lower()
