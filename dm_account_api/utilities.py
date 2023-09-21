import allure
import requests
from pydantic import BaseModel


def validation_request_json(json: str | BaseModel):
    with allure.step("Проверить схему ответа"):
        if isinstance(json, dict):
            return json
        return json.model_dump(by_alias=True, exclude_none=True, mode='json')


def validate_status_code(response: requests.Response, status_code: int):
    with allure.step("Проверить статус код"):
        assert response.status_code == status_code, \
            f'Статус код ответа должен быть равен {status_code}, но он равен {response.status_code}'
