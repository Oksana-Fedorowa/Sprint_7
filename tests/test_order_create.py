import requests
import allure
import pytest
from data import OrderData, Data

class TestOrderCreate:

    @allure.title('Проверка создания заказа с разными параметрами цвета')
    @allure.description('Согласно требованиям, система должна позволять указать в заказе один цвет самоката, выбрать '
                        'сразу оба или не указывать совсем. В тест по очереди передаются наборы данных с разными '
                        'параметрами: серый, черный, оба цвета, цвет не указан. Проверяются код и тело ответа.')
    @pytest.mark.parametrize('order_data', [
        OrderData.order_data_grey_1,
        OrderData.order_data_black_2,
        OrderData.order_data_two_colors_3,
        OrderData.order_data_no_colors_4
    ])
    def test_order_create_color_parametrize_success(self, order_data):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(Data.URL_ORDERS_CREATE, json=order_data, headers=headers, timeout=5)
        response_json = response.json()
        assert response.status_code == 201 and 'track' in response_json