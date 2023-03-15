

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

money = 0

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

water_level = resources["water"]
milk_level = resources["milk"]
coffee_level = resources["coffee"]

def report():
    print(f"Water: {water_level}ml")
    print(f"Milk: {milk_level}ml")
    print(f"Coffee: {coffee_level}g")
    print(f"Money: ${money}")


def place_order():
    global order
    order = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if order == 'latte' or order == 'espresso' or order == 'cappuccino':
        check_for_ingredients()
    elif order == 'report':
        report()


def check_for_ingredients():
    missing_ingredients = []
    if order == 'latte':
        for ingredient in MENU["latte"]["ingredients"]:
            if MENU["latte"]["ingredients"][ingredient] >= resources[ingredient]:
                missing_ingredients.append(ingredient)
        if missing_ingredients:
            print(f"Sorry, there is not enough {', '.join(missing_ingredients)} for a latte.")
            return False
        else:
            return True

    elif order == 'espresso':
        for ingredient in MENU["espresso"]["ingredients"]:
            if MENU["espresso"]["ingredients"][ingredient] >= resources[ingredient]:
                missing_ingredients.append(ingredient)
        if missing_ingredients:
            print(f"Sorry, there is not enough {', '.join(missing_ingredients)} for an espresso.")
            return False
        else:
            return True


    elif order == 'cappuccino':
        for ingredient in MENU["cappuccino"]["ingredients"]:
            if MENU["cappuccino"]["ingredients"][ingredient] >= resources[ingredient]:
                missing_ingredients.append(ingredient)
        if missing_ingredients:
            print(f"Sorry, there is not enough {', '.join(missing_ingredients)} for a cappuccino.")
            return False
        else:
            return True


def money_counter(quarters, dimes, nickles, ):
    global quarters, dimes, nickles, pennies
    print('Please insert coins.')




place_order()

#TODO: 1. Print a report of all of the coffee machine resources
#TODO: 2. Check that resources are sufficient to make drink order
#TODO 3. Process coins
#TODO 4. Check transaction successful
#TODO 5. Make coffee