import configuration
import requests
import data
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.MAKING_NEW_ORDER, #Функция для создания нового заказа
                         json=body,
                         headers=data.headers)

def get_order_status():
    get_order = create_new_order(data.order_body)
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_STATUS,#Функция запроса заказа по трек номеру
                        params=get_order.text)





