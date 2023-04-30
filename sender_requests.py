import configuration
import data
import requests

def post_create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                          json = body,
                          headers = data.headers)

responce = post_create_new_order(data.order_body)
track_number = responce.json()['track']

print(track_number)


def get_new_order():  # Запрос заказа
    current_order = data.new_order_track.copy()
    current_order['t'] = track_number
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_NUMBER_TRACK)


delivery_order = get_new_order()



