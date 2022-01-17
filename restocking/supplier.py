from urllib import response
import requests
from requests.models import Response

from api.models import Product

token = '290899a9b41a2a33dfc0914ba23277e5869a4f01'
head = {'Authorization': 'Token {}'.format(token)}

def getUser():
    response = requests.get(
        'https://rethink-supplier.herokuapp.com/user/',
        headers=head
    )
    return response

def getProductsList():
    response = requests.get(
        'https://rethink-supplier.herokuapp.com/product/',
        headers=head
    )
    return response.json()

def getProduct(EAN_13: str):
    products = getProductsList()
    for product in products:
        if product['EAN_13'] == EAN_13:
            return product
    return None


def place_orders(num: int):
    for i in range(1, num):
        requests.post(
            'https://rethink-supplier.herokuapp.com/send_order/',
            headers=head,
            data={"order_id": i}
        )
    

def add_to_orderline(order_dict: dict):
    requests.post(
        'https://rethink-supplier.herokuapp.com/orderline/',
        headers=head,
        data=order_dict
    )

def handle_deliveries():
    deliveries = requests.get(
        'https://rethink-supplier.herokuapp.com/delivery/',
        headers=head
    ).json()
    for delivery in deliveries:
        print(delivery)

    
