from http.client import responses
import pytest
import requests
import json
import allure
from uti.main_page.api import get_active_items, get_cart, add_to_cart ,free_cart ,minus_tovar
from uti.alu import alu_message, alu_assert

@allure.parent_suite('Main')
@allure.suite('Checking')
@allure.title('get_active_items')
@pytest.mark.order(1)
def test_get_active_items():
    global offer_id, slug, condition_id, moderated_offer_id
    response = get_active_items()
    alu_message(response=response)
    alu_assert(response=response)

    first_item = response.json()[0]["offers"][0]
    offer_id = first_item["moderated_offer_id"]
    slug = first_item["slug"]
    condition_id = first_item["condition"]["id"]
    moderated_offer_id = first_item["moderated_offer_id"]



@allure.parent_suite('Main')
@allure.suite('Checking')
@allure.title('get_session_id')
@pytest.mark.order(2)
def test_get_session_id():
    global cookie
    response = get_cart()
    alu_message(response=response)
    alu_assert(response=response)
    cookie = response.cookies.get_dict()['cart']
    assert isinstance(cookie, str), f'Тип куки на самом деле {type(cookie)}'


@allure.parent_suite('Main')
@allure.suite('Checking')
@allure.title('add_item')
@pytest.mark.order(3)
def test_add_item():
    response = get_cart(cookie=cookie)
    alu_message(response=response)
    alu_assert(response=response)
    response = response.json()
    add_to_cart(cookie=cookie, offer_id=offer_id, condition_id=condition_id, quantity=1)


@allure.parent_suite('Main')
@allure.suite('Checking')
@allure.title('cart_check')
@pytest.mark.order(4)
def test_cart_check():
    response = get_cart(cookie=cookie)
    alu_message(response=response)
    alu_assert(response=response)
  #  print(json.dumps(response.json(), indent=4))
  #   assert response.status_code == 200
  #   assert response.json()["moderated_cart_items"][0]["moderated_offer_id"] == offer_id
  #   assert response.json()["moderated_cart_items"][0]["slug"] == slug
  #  assert response.json()["moderated_cart_items"][0]["item_id"] == condition_id # loan_condition


@allure.parent_suite('Main')
@allure.suite('Checking')
@allure.title('minus_tovar')
@pytest.mark.order(5)
def test_minus_tovar():
    response = minus_tovar(cookie=cookie, offer_id=offer_id, condition_id=condition_id)
    alu_message(response=response)
    alu_assert(response=response)
    #print(json.dumps(response.json(), indent=4))
    # assert response.status_code == 200
    # assert response.json()["total_items_count"] == 1
    # assert response.json()["moderated_cart_items"][0]["quantity"] ==1


@allure.parent_suite('Main')
@allure.suite('Checking')
@allure.title('free_cart')
@pytest.mark.order(6)
def test_free_cart():
    response = free_cart(cookie=cookie,moderated_offer_id=moderated_offer_id)
    alu_message(response=response)
    alu_assert(response=response)
    # assert response.status_code == 200
    # response = response.json()
    # assert response["total_items_count"] == 0
   # print(json.dumps(response.json(), indent=4))