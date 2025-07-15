import json

def OpenFile(fileName, shopping_cart, cart_file):
    with open(fileName, "w", encoding="utf-8") as cart_file:
        json.dump(shopping_cart, cart_file, indent=4, ensure_ascii=False)