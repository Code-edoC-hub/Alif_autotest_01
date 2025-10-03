import requests
import json
import pytest
from uti.main_page import *

@pytest.mark.parametrize('item', ['iphone', 'samsung', 'xiaomi'])
def test_search(item):
    search_body = {
        "query": item
    }

    response = requests.post(url=search_url, json=search_body)
    res_json = response.json()

    items_list = res_json["items"]

    assert len(items_list) > 0, "Ничего не нашлось"
    print(json.dumps(response.json(), indent=1))


# Добавление товаров в Корзину

def test_get_session_id():
    response = requests.get(url=get_cart_url)
 #   print(response.cookies.get_dict()['cart'])
    return response.cookies.get_dict()['cart']


@pytest.fixture
def cookief():
    response = requests.get(url=get_cart_url)
    assert response.status_code == 200
    cookie_value = response.cookies.get_dict()['cart']
    assert isinstance(cookie_value, str), f'Тип куки на самом деле {type(cookie_value)}'
    return cookie_value

def test_add_item(cookief):
    response_active = requests.get("https://gw.alifshop.uz/web/client/events/active")
    header = {
        'Cookie': f'cart={cookief};'
    }

    body = {
        "moderated_offer_id": response_active.json()[0]["offers"][0]["moderated_offer_id"],
        "condition_id": response_active.json()[0]["offers"][0]["condition"]["id"],
        "quantity": 1
    }

    response = requests.post(url=add_cart_url, json=body, headers=header)
    assert response.status_code == 200
    res_json = response.json()
    print(json.dumps(res_json, indent=1))


# Проверка Корзины на добавление товаров


def test_view_cart(cookief):
    header = {
        'Cookie': f'cart={cookief};'
    }
    response_cart = requests.get(url=get_cart_url,headers=header)
    assert response_cart.status_code == 200
    res_cart = response_cart.json()
    assert res_cart["total_items_count"] >= 0
    print( f'Cookie cart={cookief};')
    #print(json.dumps(res_cart, indent=1))




# def test_remove_item(cookief):
#     item_id = 739467
#     product_id = 67215
#
#     headers = {
#         "Cookie": f"cart={cookief};",
#     }
#
#     body = {
#         "auth_id": None,
#         "user_id": "7a93bc8b-b88b-47b6-aea7-348bada485ae",
#         "timestamp": none,
#         "usedFrom": "Online",
#         "event": {
#             "event_type": "delete_from_cart",
#             "properties": [
#                 {"name": "layer", "value": "cart_page"},
#                 {"name": "item_id", "value": item_id},
#                 {"name": "product_id", "value": product_id},
#             ],
#         },
#     }
#
#     resp_event = requests.post(user_events_url, headers=headers, json=body)
#     assert resp_event.status_code == 200, f"Событие не записалось: {resp_event.text}"
#     url_delete = f"{remove_item_url}/{item_id}/duplicate"
#     resp_delete = requests.delete(url_delete, headers=headers)
#     assert resp_delete.status_code == 200, f"Удаление не прошло: {resp_delete.text}"





#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
