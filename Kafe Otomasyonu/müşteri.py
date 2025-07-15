import json
import os
from futils.file_handler import OpenFile
from futils.Read import OpenFile2
from futils.Loop import OpenFile3

class Musteri:
    def __init__(self, name, price, piece, sumOfProductPrice):
        self.name = name
        self.price = price
        self.piece = piece
        self.sumOfProductPrice = sumOfProductPrice

products, shopping_cart, cart_path = OpenFile2()

id_counter = max([int(k) for k in shopping_cart.keys()], default=0) + 1
total_price = 0

OpenFile3(products,shopping_cart,id_counter,cart_path)

OpenFile("shopingCart.json", shopping_cart, None)

for item in shopping_cart.values():
    total_price += item["sumOfProductPrice"]

print("Total Price:", total_price)