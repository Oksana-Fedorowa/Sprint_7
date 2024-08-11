import requests
import allure
import pytest
from data import Data
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierCreate:
    @allure.title('Проверка успешного создания аккаунта курьера с уникальными валидными данными')
    @allure.description('Happy path. Проверяются код и тело ответа.')
    def test_create_courier_success(self, create_courier):
        login = create_random_login()
        password = create_random_password()
        first_name = create_random_firstname()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(Data.URL_COURIER_CREATE, json=payload)
        assert response.status_code == 201 and response.json() == {'ok': True}

    @allure.title('Проверка получения ошибки при повторном использовании логина для создания курьера')
    @allure.description('Проверяются код и тело ответа.')
    def test_create_courier_account_login_taken_conflict(self, create_courier):
        payload = {
            "login": create_courier['login'],
            "password": create_courier['password'],
            "firstName": create_random_firstname()
        }

        response = requests.post(Data.URL_COURIER_CREATE, json=payload)
        assert response.status_code == 409 and response.json() == {'code': 409,
                                                                   'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Проверка получения ошибки при создании курьера с незаполненными обязательными полями')
    @allure.description(
        'В тест по очереди передаются наборы данных с пустым логином или паролем. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('empty_credentials', [
        {'login': '', 'password': create_random_password(), 'firstName': create_random_firstname()},
        {'login': create_random_login(), 'password': '', 'firstName': create_random_firstname()}
    ])
    def test_create_courier_account_with_empty_required_fields(self, empty_credentials):
        response = requests.post(Data.URL_COURIER_CREATE, json=empty_credentials)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}


