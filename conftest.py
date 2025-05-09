# conftest.py
import os
import pytest
import allure
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import InvalidSessionIdException


# ────────────────── .env (UI credentials) ────────────────────
load_dotenv()
USERNAME = os.getenv("ATS_USER")
PASSWORD = os.getenv("ATS_PASS")


# ────────────────── CLI flag: --headed ───────────────────────
def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        help="Run browser with UI instead of headless",
    )


# ────────────────── helpers for driver creation ──────────────
def _create_local(headed: bool):
    opts = Options()
    if not headed:
        opts.add_argument("--headless=new")  # Chrome ≥109
    opts.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)


def _create_remote(headed: bool, host: str, port: str):
    opts = Options()
    if not headed:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1920,1080")

    grid_url = f"http://{host}:{port}/wd/hub"
    return webdriver.Remote(command_executor=grid_url, options=opts)


# ────────────────── browser fixture (works everywhere) ──────
@pytest.fixture(scope="function")
def browser(request):
    headed = request.config.getoption("--headed")

    # If SELENIUM_HOST is defined (e.g. inside docker-compose), use Remote
    selenium_host = os.getenv("SELENIUM_HOST")  # "chrome" in compose
    selenium_port = os.getenv("SELENIUM_PORT", "4444")

    if selenium_host:  # Remote grid mode
        driver = _create_remote(headed, selenium_host, selenium_port)
    else:  # Local Chrome
        driver = _create_local(headed)

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# ────────────────── attach screenshot on failure ────────────
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach PNG screenshot to Allure if a UI test fails."""
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        drv = item.funcargs.get("browser")
        if drv:
            try:
                png = drv.get_screenshot_as_png()
                allure.attach(
                    png, name="failure", attachment_type=allure.attachment_type.PNG
                )
            except InvalidSessionIdException:
                # session already closed – skip
                pass
