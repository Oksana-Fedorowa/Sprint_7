import requests
import allure
import pytest
from data import Data


class TestOrdersListGet:

    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяются код и структура ответа при запросе списка заказов.')
    def test_orders_list_get_success(self):
        response = requests.get(Data.URL_ORDERS_CREATE)
        response_json = response.json()

        assert (
                response.status_code == 200 and
                'orders' in response_json and
                isinstance(response_json['orders'], list) and
                all('id' in order for order in response_json['orders']) and
                'pageInfo' in response_json and
                'availableStations' in response_json
        )
