import requests
from pydantic import BaseModel
import allure


class User(BaseModel):
    id: int
    username: str
    email: str


@allure.title("Fetch users and validate response with Pydantic")
def test_get_users():
    r = requests.get("https://jsonplaceholder.typicode.com/users")

    # basic contract
    assert r.status_code == 200

    # schema & typing for each item
    for item in r.json():
        User.model_validate(item)
