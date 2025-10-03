# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# def get_env(base_url,active_items_url,get_item,search_url,get_cart_url,add_cart_url,remove_item_url,user_events_url):
#     base_url = os.getenv("base_url")
#     active_items_url = os.getenv("active_items_url")
#     get_item =  os.getenv("get_item")
#     search_url = os.getenv("search_url")
#     get_cart_url = os.getenv("get_cart_url")
#     add_cart_url = os.getenv("add_cart_url")
#     remove_item_url =os.getenv("remove_item_url")
#     user_events_url = os.getenv("user_events_url")
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
ACTIVE_ITEMS_URL = os.getenv("ACTIVE_ITEMS_URL")
GET_ITEM_URL = os.getenv("GET_ITEM_URL")
SEARCH_URL = os.getenv("SEARCH_URL")
GET_CART_URL = os.getenv("GET_CART_URL")
ADD_CART_URL = os.getenv("ADD_CART_URL")
REMOVE_ITEM_URL = os.getenv("REMOVE_ITEM_URL")
USER_EVENTS_URL = os.getenv("USER_EVENTS_URL")








