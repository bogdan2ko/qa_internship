import allure, pytest
from pages.login_page import LoginPage

invalid_data = [
    ("wrong_user", "wrong_pass"),
    ("",           "some_pass"),
    ("student",    "")
]

@pytest.mark.parametrize("username,password", invalid_data)
@allure.title("Негативные сценарии логина")
def test_login_negative(browser, username, password):
    page = LoginPage(browser)
    page.open()

    page.set_username(username)
    page.set_password(password)
    page.submit()

    assert page.has_error(), "Ожидали сообщение об ошибке, но не нашли"

