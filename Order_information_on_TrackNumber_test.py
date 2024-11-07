#Данильченко Вячеслав, когорта 23А - дипломный проект. Инженер по тестированию плюс, автотест Яндекс Самокат

import sender_stand_request

def test_order_gettin_status_code():
    order_get_result = sender_stand_request.get_order_status()
    assert order_get_result.status_code == 200 #проверяет,что по треку заказа можно получить данные о заказе (код ответа 200).






