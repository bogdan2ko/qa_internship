# QA Internship – UI & API Automation Demo


> Demonstrates practical use of Selenium WebDriver, Pytest, Pydantic and Allure.

---

## Tech Stack

| Area          | Tools |
|---------------|-------|
| Language      | **Python 3.11** |
| UI automation | **Selenium** (webdriver‑manager, Page Object) |
| API tests     | **requests + Pydantic v2** |
| Test runner   | **Pytest 8** |
| Reporting     | **Allure 2** |
| CI            | **GitHub Actions** (Ubuntu, headless Chrome) |
| Extras        | python‑dotenv, allure‑pytest |

---

## Test Coverage

| Module | Test case | Status |
|--------|-----------|--------|
| UI     | **Positive login** (valid credentials) | ✅ passed |
| UI     | **Negative logins** (wrong pass / empty fields) × 3 | ✅ passed |
| API    | GET `/users` from JSONPlaceholder → schema validation with Pydantic | ✅ passed |

Result in Allure: **4 / 4 passed • 0 failed • 0 broken**.

---

## Quick Start (local)

```bash
# 1 · clone & venv
git clone https://github.com/<your‑nick>/qa‑internship.git
cd qa‑internship
python -m venv venv && venv\Scripts\activate          # macOS / Linux: source venv/bin/activate
pip install -r requirements.txt

# 2 · environment variables
cp .env.example .env          # Windows: copy .env.example .env
# put your AutomationTestStore creds: ATS_USER / ATS_PASS

# 3 · run tests
pytest -s tests/ui            # UI suite (headless by default)
pytest -s tests/api           # API suite

# 4 · Allure report
pytest -s --alluredir=allure-results
allure serve allure-results




