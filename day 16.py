

from py_16_1 import Menu,MenuItem
from py_16_2 import CoffeeMaker
from py_16_3 import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
coffee_maker.report()
money_machine.report()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)


