import requests
import pytest
from data import Data
from helpers import create_random_login, create_random_password, create_random_firstname

@pytest.fixture
def create_courier():
    login = create_random_login()
    password = create_random_password()
    first_name = create_random_firstname()

    # Создание курьера
    create_payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    create_response = requests.post(Data.URL_COURIER_CREATE, json=create_payload)
    if create_response.status_code == 201:
        assert create_response.json() == {'ok': True}
    else:
        # Если курьер уже существует, можно удалить его и попробовать создать заново
        if create_response.status_code == 409:
            # Удаление существующего курьера с таким логином
            existing_courier = requests.get(f"{Data.URL_COURIER_CREATE}{login}")
            if existing_courier.status_code == 200:
                requests.delete(f"{Data.URL_COURIER_CREATE}{existing_courier.json()['id']}")
            create_response = requests.post(Data.URL_COURIER_CREATE, json=create_payload)
            assert create_response.status_code == 201
            assert create_response.json() == {'ok': True}

    # Логин
    login_payload = {
        "login": login,
        "password": password
    }

    login_response = requests.post(Data.URL_COURIER_LOGIN, json=login_payload)
    assert login_response.status_code == 200
    assert 'id' in login_response.json()

    courier_id = login_response.json()['id']

    yield {
        'id': courier_id,
        'login': login,
        'password': password
    }

    # Удаление курьера
    requests.delete(f'{Data.URL_COURIER_CREATE}{courier_id}')

