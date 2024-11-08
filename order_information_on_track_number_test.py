#Данильченко Вячеслав, когорта 23А - дипломный проект. Инженер по тестированию плюс, автотест Яндекс Самокат

import sender_stand_request
import data

def test_get_order_by_track_success():
    create_order_response = sender_stand_request.create_new_order(data.order_body)
    track = create_order_response.json()["track"]
    get_order_response = sender_stand_request.get_order_by_track(track)
    assert get_order_response.status_code == 200 #проверяет,что по треку заказа можно получить данные о заказе (код ответа 200).






