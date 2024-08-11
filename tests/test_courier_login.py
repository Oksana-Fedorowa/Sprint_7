import requests
import allure
import pytest
from data import Data
from helpers import create_random_login, create_random_password, create_random_firstname


class TestCourierLogin:

    @allure.title('Проверка успешной авторизации курьера с валидными данными')
    @allure.description('Happy path. Проверяются код и тело ответа.')
    def test_courier_login_success(self, create_courier):
        login_payload = {
            "login": create_courier['login'],
            "password": create_courier['password']
        }

        response = requests.post(Data.URL_COURIER_LOGIN, json=login_payload)
        assert response.status_code == 200 and 'id' in response.text

    @allure.title('Проверка ошибки при авторизации с отсутствующим обязательным полем')
    @allure.description('Проверяется ошибка при отсутствии обязательных полей.')
    @pytest.mark.parametrize('missing_field', [
        {'login': '', 'password': create_random_password()},
        {'login': create_random_login(), 'password': ''},
    ])
    def test_courier_login_missing_field(self, missing_field):
        response = requests.post(Data.URL_COURIER_LOGIN, json=missing_field)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Проверка ошибки при авторизации с неправильным логином или паролем')
    @allure.description('Проверяется ошибка при вводе неправильного логина или пароля.')
    @pytest.mark.parametrize('login_password', [
        {'login': create_random_login(), 'password': create_random_password()},
        {'login': create_random_login(), 'password': 'wrongpassword'},
        {'login': 'wronglogin', 'password': create_random_password()}
    ])
    def test_courier_login_invalid_credentials(self, login_password):
        response = requests.post(Data.URL_COURIER_LOGIN, json=login_password)
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}

    @allure.title('Проверка ошибки при попытке авторизации несуществующего пользователя')
    @allure.description('Проверяется ошибка при попытке авторизации под несуществующим пользователем.')
    def test_courier_login_nonexistent_user(self):
        login_payload = {
            "login": create_random_login(),
            "password": create_random_password()
        }

        response = requests.post(Data.URL_COURIER_LOGIN, json=login_payload)
        assert response.status_code == 404 and response.json() == {'code': 404, 'message': 'Учетная запись не найдена'}
