"""Базовый класс Page Object с явными ожиданиями и удобными методами."""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ––– helpers –––
    def _wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self._wait_visible(locator).click()

    def type(self, locator, value: str, clear: bool = True):
        elem = self._wait_visible(locator)
        if clear:
            elem.clear()
        elem.send_keys(value)