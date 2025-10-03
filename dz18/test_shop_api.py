#
# #���������, ��� ����� ������ "automation" ����� 10
# from os import name
# def test_strle():
#     str_1 = "automation"
#     counter_char= len(str_1)
#     assert counter_char == 10
# #���������, ��� ������������ ����� �� [5, 9, 2, 7] ����� 9
# def test_maxi():
#     massa = [5, 9, 2, 7]
#     maxi = massa[0]
#     for i in massa:
#         if i>maxi:
#             maxi=i
#     assert maxi == 9
#
# #���������, ��� ������� {"name": "QA", "level": 1} �������� ���� "name"
# def test_mappa():
#     mapa = {"name": "QA", "level": 1}
#     assert "name" in mapa
#
# some_value = 'animal'
#
# def test_value_type():
#     assert isinstance(some_value, int), f"No no no {type(some_value)}"
from pkgutil import resolve_name

##########################################################################################################################################################################################################


# import requests
# import json
#
# base_url = "https://gw.alifshop.uz"
#
# active_items_url = f"{base_url}/web/client/events/active"
# get_item = f"{base_url}/web/client/moderated-offers"
#
#
# def url_generator(slug):
#     return f'{get_item}/{slug}'
#
#
# def test_active_items():
#     global item_slug
#     response = requests.get(url=active_items_url)
#     assert response.status_code == 200
#     response = response.json()
#     item_slug = response[0]['offers'][0]['slug']
#
#
# def test_get_item():
#     url = url_generator(item_slug)
#     response = requests.get(url=url)
#     print(response.json())
# test_alifshop.py



import requests
import pytest

url = "https://gw.alifshop.uz/web/client/filters/categories/noutbuki-i-kompjyuteri/brands"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0",
    "Accept": "*/*",
    "Accept-Language": "ru",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Referer": "https://alifshop.uz/",
    "service-token": "service-token-alifshop",
    "Authorization": "",
    "Origin": "https://alifshop.uz",
    "Connection": "keep-alive",
    # при необходимости оставь только важные cookie, сейчас все скопированы
    "Cookie": "_gcl_aw=...; _gcl_gs=...; _gcl_au=...; _ga=...; cart=...",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
}


def test_get_brands():
    response = requests.get(url, headers=headers)

    # Проверка на 200
    assert response.status_code == 200

    # Вывод тела ответа (pytest покажет это в консоли)
    print("\nТело ответа:", response.text)



# Описание
# У вас есть несколько JSON-ответов с разных роутов сервиса Alif Shop:
# 	•	/events/active — список активных предложений
# 	•	/delivery-time-estimation/duplicate — информация о доставке товара
# 	•	/moderated-offers/{slug} — подробная информация о товаре
# 	•	/{id}/reviews — отзывы о товаре
# 	•	/offers/v2 — список популярных товаров
# Ваша задача — написать набор тестов на Python (pytest + requests) для проверки корректности данных

def test_task_one():
    base_url = "https://gw.alifshop.uz/web/client"
    response_active = requests.get(f"{base_url}/events/active")
    assert response_active.status_code == 200
    assert isinstance(response_active, list)
    response_active = response_active.json()
    slug = response_active[0]["offers"][0]["slug"]
    assert isinstance(response_active[0]["offers"][0]["price"], int)
    check_one = response_active[0]["offers"]
    for iter in check_one:
        assert "id" in iter, f"В оффере  нет поля id"
        assert "name" in iter, f"В оффере нет поля name"
        assert "price" in iter, f"В оффере нет поля price"
        assert "partner" in iter, f"В оффере нет поля partner"
        assert iter["old_price"] >= iter["price"]
    moder = response_active[0]["offers"][0]["moderated_offer_id"]

    response_duplicate = requests.get(f"{base_url}/catalog/moderated-offers/{moder}/delivery-time-estimation/duplicate")
    assert response_duplicate.status_code == 200
    assert "moderated_offer_id" in response_duplicate.json(),f"Нет поля moderated_offer_id"
    assert "delivery_time" in response_duplicate.json(), f"Нет поля delivery_time"
    assert "days_to_deliver" in response_duplicate.json(), f"Нет поля days_to_deliver"
    assert response_duplicate["days_to_deliver"] >= 0, "Days error"


    response_slug = requests.get(f"{base_url}/moderated-offers/{slug}")
    assert response_slug.status_code == 200
    item = response_slug.json()["moderated_offer"]
    assert "name" in item, f"Нет name slug"
    assert item["price"] >0, f"Price <0"
    assert item["discount"] <0, f"Discount >0"
    if item["discount"] < 0:
        assert item["old_price"] < item["price"], f"discout error "
    assert len( item["images"]) >0, f"No images"
    id = item["id"]



    response_review = requests.get(f"{base_url}/{id}/reviews")
    assert response_review.status_code == 200
    assert isinstance(response_review, list)
    assert len( response_review) >0, f"No reviews"


    body={"user_id":"7a93bc8b-b88b-47b6-aea7-348bada485ae","from_app":"WebAndMobile","from_layer":"offer_page","product_ids":[50638],"limit":15}
    response_v2 = requests.post(url=f"{base_url}/recommend/offers/v2",json=body)
    assert response_v2.status_code == 200
    for item in response_v2.json()["offers"]:
        assert "name" in item, f"No Name"
        assert "rating" in item, f"No Rating"
        for item_two in item["conditions"]:
            assert "duration" in item_two, f"No Duration"
            assert "commission" in item_two, f"No commission"
            assert item_two["commission"] != item_two["duration"], f"No same"






