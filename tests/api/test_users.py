"""API‑тест с валидацией ответа через Pydantic"""
import requests
import allure

from src.baseclasses.response import Response
from src.pydantic_schemas.user import UserData

@allure.title("Получаем список пользователей (Reqres) и валидируем схему")
def test_get_users():
    r = requests.get("https://reqres.in/api/users", params={"page": 2})

    response = Response(r)

    # Проверяем статус‑код и валидируем JSON через Pydantic‑схему
    response.validate_status_code(200).validate(UserData)

    # parsed_object будет содержать последний валидный объект из списка
    user = response.get_parsed_object()
    assert user.id > 0
    assert "@" in user.email