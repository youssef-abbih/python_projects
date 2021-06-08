from data import MENU, resources

PROMPT = "What would you like? (espresso/latte/cappuccino): "

is_on = True
profit = 0

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True
while is_on:

    choice = input(PROMPT)
    if choice == 'off':
        is_on = False
    elif choice == 'repport':
        print(f"""
        Water: {resources["water"]}
        Milk: {resources['milk']}
        Coffee: {resources['coffee']}
        Money: {profit}
        """)
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredient'])
