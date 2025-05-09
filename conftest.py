import os
import pytest
from dotenv import load_dotenv
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ── .env ────────────────────────────────────────────────────────────────────────
load_dotenv()                       # подхватываем переменные из .env
USERNAME = os.getenv("ATS_USER")
PASSWORD = os.getenv("ATS_PASS")


# ── CLI‑параметры ──────────────────────────────────────────────────────────────
def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run browser with UI instead of headless",
    )


# ── browser fixture ────────────────────────────────────────────────────────────
@pytest.fixture(scope="function")
def browser(request):
    headed = request.config.getoption("--headed")

    options = webdriver.ChromeOptions()
    if not headed:
        options.add_argument("--headless=new")           # или "--headless", если Chrome < 109
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)

    yield driver
    driver.quit()




from selenium.common.exceptions import InvalidSessionIdException
import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("browser")
        if drv:
            try:
                png = drv.get_screenshot_as_png()
                allure.attach(png, name="failure",
                              attachment_type=allure.attachment_type.PNG)
            except InvalidSessionIdException:
                # сессия уже закрыта – просто пропускаем
                pass


