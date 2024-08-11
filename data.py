class Data:
    URL_BASIK = 'https://qa-scooter.praktikum-services.ru/'
    URL_COURIER_CREATE = f'{URL_BASIK}api/v1/courier/'
    URL_COURIER_LOGIN = f'{URL_BASIK}api/v1/courier/login'
    URL_ORDERS_CREATE = f'{URL_BASIK}api/v1/orders'

class OrderData:
    order_data_grey_1 = {
        'firstName': 'Дайнерис',
        'lastName': 'Таргариен',
        'address': 'Драконий камень, 1',
        'metroStation': 8,
        'phone': '+79124567890',
        'rentTime': 5,
        'deliveryDate': '2024-08-15',
        'comment': 'Пламя и кровь ',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Джон',
        'lastName': 'Сноу',
        'address': 'Винтерфелл, 1',
        'metroStation': 10,
        'phone': '+79125678901',
        'rentTime': 3,
        'deliveryDate': '2024-08-16',
        'comment': 'Зима близко',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Арья',
        'lastName': 'Старк',
        'address': 'Винтерфелл,2',
        'metroStation': 15,
        'phone': '+7111456789',
        'rentTime': 1,
        'deliveryDate': '2024-08-17',
        'comment': 'У девочки нет имени',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Тирион',
        'lastName': 'Ланнистер',
        'address': 'Утес Кастерли, 1',
        'metroStation': 20,
        'phone': '+76666666666',
        'rentTime': 2,
        'deliveryDate': '2024-08-16',
        'comment': 'Ланнистеры всегда платят свои долги',
        'color': []
    }

