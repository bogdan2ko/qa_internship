from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ── новый/вернувшийся helper ────────────────────────────────────────────
    def _visible(self, locator):
        """Ждём, что элемент отрендерился и не скрыт CSS‑ом."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def _present(self, locator):
        return self.driver.find_element(*locator)

    def _clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self._present(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )
        try:
            self._clickable(locator).click()
        except TimeoutException:
            self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator, value: str):
        el = self._clickable(locator)
        el.clear()
        el.send_keys(value)
