from tabulate import tabulate
import time
class Shop:
    print("Menu".center(56, "-"))
    menu = {
        "1": {"id": 1, "food_name": "Sandwich", "food_price": 10, "prep_time": 10},
        "2": {"id": 2, "food_name": "Salad", "food_price": 8, "prep_time": 8},
        "3": {"id": 3, "food_name": "Soup", "food_price": 6, "prep_time": 15},
        "4": {"id": 4, "food_name": "Coffee", "food_price": 5, "prep_time": 5},
        "5": {"id": 5, "food_name": "tea", "food_price": 5, "prep_time": 5}}
    print(tabulate(menu.values(), tablefmt="rounded_outline",
                   headers={"id": "#", "food_name": "items", "food_price": "price($)",
                            "prep_time": "Preparation time(min)"}))
    name = input("Enter your name : ")
    print(name.title(), "Welcome to MA restaurant")


class Person(Shop):
    cart = {}
    quantity = 0
    total_price = 0

    def add_items(self):
        item = input("What do you want to buy : ")
        quantity = int(input("how many do you want : "))
        name = self.menu[item]["food_name"]
        price = self.menu[item]["food_price"]
        P_time = self.menu[item]["prep_time"]
        t_price = price * quantity
        self.cart.update({item: {"name": name, "quantity": quantity, "price": t_price,
                                 "time": P_time * quantity}})


def Time():
    s = time.time()
    local_time = time.ctime(s)

    def convert():
        return time.strftime("%H:%M:%S", time.gmtime(t))

    t = 0
    for x in p2.cart.values():
        y = x.get("time")
        t += y
    if t > 60:
        t *= 60.00012
        f = convert()
    else:
        f = f"{t} min"
    print(local_time, "  your order will be ready in ", f)


def total_price():
    s = 0
    for x in p2.cart.values():
        q = x.get("price")
        s += q
    return s


def tax():
    p = float(total_price()) * 0.03 + float(total_price())
    print("tax :", float(total_price()) * 0.03)
    print("Total price : ", p, "$")


class Receipt(Person):
    def Discount(self):
        for x in self.cart.keys():
            if x == "1" and self.cart[x]["quantity"] >= 5:
                self.cart[x]["price"] = self.cart[x]["price"] * 0.90
            elif x == "2" and "3" in self.cart.keys():
                self.cart[x]["price"] = self.cart[x]["price"] * 0.90
            elif x == "3" and ("1" and "2") in self.cart.keys():
                self.cart[x]["price"] = self.cart[x]["price"] * 0.80

    def shop_more(self):
        while True:
            choice = int(input("Enter your choice 1 for more order 2 for done "))
            if choice == 1:
                self.add_items()
            elif choice == 2:
                break
            else:
                print("Invalid choice")


p1 = Person()
p1.add_items()
p2 = Receipt()
p2.shop_more()
p2.Discount()
print("Thanks for Order".center(56, "-"))
print(tabulate(p2.cart.values(), tablefmt="rounded_outline", headers={"name": "name", "quantity": "quantity", "price": "price($)", "time": "preparation time(min)"}))
tax()
Time()
