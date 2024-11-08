#Данильченко Вячеслав, когорта 23А - дипломный проект. Инженер по тестированию плюс, автотест Яндекс Самокат

import sender_stand_request
import data

def test_order_gettin_status_code():
    get_order = sender_stand_request.create_new_order(data.order_body)
    return get_order
    order_get_result = sender_stand_request.get_order_status()
    assert order_get_result.status_code == 200 #проверяет,что по треку заказа можно получить данные о заказе (код ответа 200).






