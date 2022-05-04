MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water_used = 0
milk_used = 0
coffee_used = 0
cost_of_coffee = 0


def resource_used_in_coffee(coffee):
    selection_of_coffee = MENU[coffee]
    ingredients = selection_of_coffee["ingredients"]
    global water_used, milk_used, coffee_used, cost_of_coffee
    water_used = ingredients["water"]
    milk_used = ingredients["milk"]
    coffee_used = ingredients["coffee"]
    cost_of_coffee = selection_of_coffee["cost"]
    return water_used, milk_used, coffee_used, cost_of_coffee


def remaining_resources():
    resources["water"] -= water_used
    resources["milk"] -= milk_used
    resources["coffee"] -= coffee_used
    return resources["water"], resources["milk"], resources["coffee"]


def resource_checker():
    resource_available = True
    if resources["water"] < water_used:
        resource_available = False
        print(f'''“Sorry there is not enough water"''')
    elif resources["milk"] < milk_used:
        resource_available = False
        print(f'''“Sorry there is not enough milk"''')
    elif resources["coffee"] < coffee_used:
        resource_available = False
        print(f'''“Sorry there is not enough coffee"''')
    return resource_available


should_continue = True
report = f'''water: {resources["water"]}\nmilk: {resources["milk"]}\ncoffee: {resources["coffee"]}'''
money = 0
while should_continue:

    # TODO 1. print welcome message and ask for the option
    order = input('''What would you like? (espresso/latte/cappuccino):''')

    if order == "off":
        should_continue = False
    elif order == "report":
        print(report)
    else:
        resource_used_in_coffee(order)
        have_resources = resource_checker()
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies: "))
        value_of_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        if value_of_coins < cost_of_coffee:
            print('''“Sorry that's not enough money. Money refunded.”''')
        elif value_of_coins >= cost_of_coffee:
            change = value_of_coins - cost_of_coffee
            print(f" Here is your {change} change")

        remaining_resources()
        if have_resources and value_of_coins >= cost_of_coffee:
            print(f'''“Here is your {order}. Enjoy!”''')
            money += cost_of_coffee
            print(money)
            report = f'''water: {resources["water"]}\nmilk: {resources["milk"]}\ncoffee: {resources["coffee"]}\nmoney: {money}'''
