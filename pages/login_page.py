from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница логина AutomationTestStore"""

    URL = "https://automationteststore.com/index.php?rt=account/login"

    _USERNAME = (By.ID, "loginFrm_loginname")
    _PASSWORD = (By.ID, "loginFrm_password")
    _SUBMIT = (By.CSS_SELECTOR, "button[title='Login']")

    # ––– actions –––
    @allure.step("Открываем страницу логина")
    def open(self):
        self.driver.get(self.URL)

    @allure.step("Вводим имя пользователя: {username}")
    def set_username(self, username: str):
        self.type(self._USERNAME, username)

    @allure.step("Вводим пароль: {password}")
    def set_password(self, password: str):
        self.type(self._PASSWORD, password)

    @allure.step("Нажимаем кнопку Login")
    def submit(self):
        self.click(self._SUBMIT)