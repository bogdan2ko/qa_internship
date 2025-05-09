from selenium.webdriver.common.by import By
import allure

from pages.base_page import BasePage, TimeoutException


class LoginPage(BasePage):
    """Страница логина AutomationTestStore."""
    URL = "https://automationteststore.com/index.php?rt=account/login"

    _USERNAME = (By.ID, "loginFrm_loginname")
    _PASSWORD = (By.ID, "loginFrm_password")
    # универсальный: любой submit‑input внутри формы
    # замените текущий _SUBMIT на:
    _SUBMIT = (By.CSS_SELECTOR, "#loginFrm button.btn-orange[title='Login']")



    _LOGOUT = (
    By.XPATH,
    "//a[text()='Logout' or text()='Logoff']"
)

    _ERROR    = (By.CSS_SELECTOR, ".alert")

    # -------- actions --------
    @allure.step("Открываем страницу логина")
    def open(self):
        self.driver.get(self.URL)
        self._visible(self._USERNAME)          # ждём поля username

    @allure.step("Вводим имя пользователя: {username}")
    def set_username(self, username: str):
        self.type(self._USERNAME, username)

    @allure.step("Вводим пароль")
    def set_password(self, password: str):
        self.type(self._PASSWORD, password)

    @allure.step("Нажимаем кнопку Login")
    def submit(self):
        self.click(self._SUBMIT)

    # -------- helpers --------
    def is_logged_in(self) -> bool:
        try:
            self._visible(self._LOGOUT)
            return True
        except TimeoutException:
            return False

    def has_error(self) -> bool:
        try:
            self._visible(self._ERROR)
            return True
        except TimeoutException:
            return False
