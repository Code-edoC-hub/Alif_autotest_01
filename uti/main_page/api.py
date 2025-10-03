import requests
from env import (
    BASE_URL, ACTIVE_ITEMS_URL, GET_ITEM_URL,
    SEARCH_URL, GET_CART_URL, ADD_CART_URL,
    REMOVE_ITEM_URL, USER_EVENTS_URL
)

def get_active_items():
    return requests.get(url=f"{BASE_URL}{ACTIVE_ITEMS_URL}")

def get_item(item_slug: str):
    return requests.get(url=f"{BASE_URL}{GET_ITEM_URL}/{item_slug}")

def search_items(item_name: str):
    body = {"query": item_name}
    return requests.post(url=f"{BASE_URL}{SEARCH_URL}", json=body)

def get_cart(cookie=None):
    headers = {'Cookie': f"cart={cookie};"} if cookie else None
    return requests.get(url=f"{BASE_URL}{GET_CART_URL}", headers=headers)

def add_to_cart(cookie: str, offer_id: str, condition_id: int, quantity=1):
    headers = {'Cookie': f"cart={cookie};"}
    body = {
        "moderated_offer_id": offer_id,
        "condition_id": condition_id,
        "quantity": quantity
    }
    return requests.post(url=f"{BASE_URL}{ADD_CART_URL}", json=body, headers=headers)

def minus_tovar(cookie, offer_id, condition_id: int):
    headers = {'Cookie': f"cart={cookie};"}
    body = {
        "moderated_offer_id": offer_id,
        "condition_id": condition_id,
        "quantity": 1
    }
    return requests.patch(f"{BASE_URL}/web/client/cart/moderated-items/quantity", json=body, headers=headers)

def free_cart(cookie, moderated_offer_id: str):
    headers = {'Cookie': f"cart={cookie};"}
    return requests.delete(url=f"{BASE_URL}{ADD_CART_URL}/{moderated_offer_id}", headers=headers)
