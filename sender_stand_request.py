import configuration
import requests
import data
import Order_information_on_TrackNumber_test as Order
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.MAKING_NEW_ORDER, #Функция для создания нового заказа
                         json=body,
                         headers=data.headers)
def get_order_status():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_STATUS,#Функция запроса заказа по трек номеру
                        params=Order.get_order.text)





