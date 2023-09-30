import requests
import config
import data

def post_new_order():
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
           json=data.order_body,
           headers=data.headers)


def get_order_info(track_number):
    return requests.get(config.URL_SERVICE + config.GET_ORDER_INFO,
           params={"t": track_number})