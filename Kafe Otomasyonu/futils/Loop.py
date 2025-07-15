import json

def OpenFile3(products,shopping_cart,id_counter,cart_path):
    loop0 = True
    while loop0:
        requests = input("Sir, what do you want: ").strip().lower()
        while True:
            pieceAsking = input("How many do you want: ").strip()
            if pieceAsking.isdigit():
                break
            else:
                print("Please, enter a valid number.")
                continue

        found = False
        for key, values in products.items():
            product_name = values["name"].strip().lower()
            if product_name == requests:
                shopping_cart[str(id_counter)] = {
                    "name": values["name"].strip(),
                    "price": int(values["price"]),
                    "piece": int(pieceAsking),
                    "sumOfProductPrice": int(pieceAsking) * int(values["price"])
                }
                print(f"{requests} added to shopping cart.")
                id_counter += 1
                found = True
                break

        if not found:
            print(f"Product '{requests}' not found!")
            continue

        addingQuestion = input("Do you want to keep adding (y/n): ").lower()

        if addingQuestion in ("y", "yes"):
            continue
        loop1 = True
        while loop1:
            if addingQuestion in ("n", "no"):
                extractQuestion = input("Do you want to extract any item from shopping cart (y/n): ").lower()
                loop0 = False
                loop1 = False

                if extractQuestion in ("y", "yes"):
                    print(json.dumps(shopping_cart, indent=4))
                    extractor_id = input("Enter the ID of the product you want to remove: ").strip()
                    if extractor_id in shopping_cart:
                        del shopping_cart[extractor_id]
                        print(f"Product with ID {extractor_id} removed from cart.")
                        break
                    boolean = True
                    while boolean == True:
                        for key in shopping_cart.keys():

                            if extractQuestion == shopping_cart[key]:
                                boolean = True
                                break
                            else:
                                boolean = False
                        if boolean == False:
                            print("Product with ID not in shopping cart.")


                    with open(cart_path, "w", encoding="utf-8") as f:
                        json.dump(shopping_cart, f, indent=4)

                elif extractQuestion in ("n", "no"):
                    break
                else:
                    print("Please, enter a valid word.")
                    continue
            else:
                print("Wrong entry. Please enter y or n.")
                continue