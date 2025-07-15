import json
import os
def OpenFile2():
    with open("menu.json", "r", encoding="utf-8") as menu_file:
        menu = json.load(menu_file)

    products = menu.get("products", {})
    cart_path = "shopingCart.json"

    if os.path.exists(cart_path):
        with open(cart_path, "r", encoding="utf-8") as cart_file:
            try:
                shopping_cart = json.load(cart_file)
            except json.JSONDecodeError:
                shopping_cart = {}
    else:
        shopping_cart = {}

    return products, shopping_cart, cart_path