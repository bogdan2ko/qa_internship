# tests/api/test_users.py
import requests
from pydantic import BaseModel
import allure

class User(BaseModel):
    id: int
    name: str
    username: str
    email: str

@allure.title("Fetch users and validate response with Pydantic")
def test_get_users():
    r = requests.get("https://jsonplaceholder.typicode.com/users")

    assert r.status_code == 200, f"Unexpected status: {r.status_code}"

    for item in r.json():
        User.model_validate(item)
