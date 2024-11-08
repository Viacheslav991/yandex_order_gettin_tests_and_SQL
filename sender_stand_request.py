import configuration
import requests
import data

def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.MAKING_NEW_ORDER, #Функция для создания нового заказа
                         json=body,
                         headers=data.headers)
def get_order_by_track(track):
    params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_STATUS,
                        params=params)





