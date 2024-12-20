Menu = {
    "espresso": {
        "ingredients":{
            "water": 50,
            "coffee": 10,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resources_sufficient(ordered_ingredients):
    is_enough = True
    for items in ordered_ingredients:

        if ordered_ingredients[items] >= resources[items]:
            print(f"Sorry there is not enough {items}")
            is_enough = False
        return is_enough
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quaters?")) * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name} ☕")
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = Menu[choice]
        print(drink)
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])




