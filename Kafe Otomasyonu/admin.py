import json
import os

class admin:
    def __init__(self,name,price,id):
        self.name=name
        self.price=price
        self.id=id

if os.path.exists("menu.json"):
    with open("menu.json", "r") as f:
        try:
            print("Reading products data")
            products = json.load(f)
        except json.JSONDecodeError as exp:
            print(f"The error is {exp}")
            products = {}

if "products" not in products:
    products["products"] = {}

loop = True

while loop:
    selection = input("Select action (a append, r remove, c change, q quit): ")

    if selection == "a":
        loop1 = True
        while loop1:
            addID = int(input("Add new product ID to menu: "))

            if isinstance(addID,int):
                loop1 = False
            else:
                print("ID must be integer!")
                addID = input("Add new product ID to menu: ")



        addName = input("Add new product name to menu: ").lower()
        addPrice = input("Add new product price to menu: ")

        products["products"][addID] = {"name":addName,"price":addPrice}

        with open("menu.json","w") as f:
            json.dump(products,f,ensure_ascii=False,indent=2)

        print("Product added")
        break


    elif selection == "r":

        removeName = input("Remove product name from menu: ").lower()

        key_to_remove = None

        for key, value in products.get("products", {}).items():

            if value["name"].lower() == removeName:
                key_to_remove = key

                break

        if key_to_remove is not None:

            del products["products"][key_to_remove]

            with open("menu.json", "w") as f:

                json.dump(products, f, indent=4)

            print(f"Product '{removeName}' removed.")

        else:

            print(f"Product '{removeName}' not found.")



    elif selection == "c":

        loop2 = True
        while loop2:
            wichProduct = input("Which product do you want to change? Write ID: ").lower()

            if products["products"][wichProduct]:
                product = products["products"][wichProduct]
                print(f"Current info {product}")

                new_id = input("New Product ID: ")
                new_name = input("New Product name: ").lower()
                new_price = input("New Product price: ")

                if new_id == wichProduct:
                    products["products"][wichProduct] = {"name":new_name, "price":new_price}
                else:
                    del products["products"][wichProduct]

                products["products"][new_id] = {"name": new_name, "price": new_price}

                with open("menu.json","w") as f:
                    json.dump(products,f,indent=4)

                print("Product has been changed properly.")
                loop2 = False
            else:
                print("ID must be integer!")
                wichProduct = input("Which product do you want to change? Write ID: : ")



    elif selection == "q":
        loop = False

    else:
        print("Wrong selection")