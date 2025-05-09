"""Универсальный wrapper над requests.Response
   Позволяет цепочечной записью проверять статус‑код и валидировать тело через Pydantic."""
from typing import Type
from pydantic import BaseModel


class Response:
    """Обёртка для requests.Response c Pydantic‑валидацией"""

    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get("data")
        self.status_code = response.status_code
        self.parsed_object = None  # сохранится последний распарсенный объект

    def validate(self, schema: Type[BaseModel]):
        """Валидирует self.response_json против переданной Pydantic‑модели"""
        if isinstance(self.response_json, list):
            # Если API вернуло массив — валидируем каждый элемент
            for item in self.response_json:
                self.parsed_object = schema.model_validate(item)
        else:
            self.parsed_object = schema.model_validate(self.response_json)
        return self

    def validate_status_code(self, expected_status_code):
        if isinstance(expected_status_code, list):
            assert self.status_code in expected_status_code, self
        else:
            assert self.status_code == expected_status_code, self
        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        return (
            f"\n Status Code: {self.status_code},"
            f"\n Request URL: {self.response.url},"
            f"\n Respone body: {self.response_json},"
        )