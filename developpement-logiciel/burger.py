# burger_maker_bad_with_ruff.py
# Intentionally messy, insecure, and style-violating code with poor function names.

import os


def GetBun():
    bun_type = input("What kind of bun would you like? ")
    for i in range(5):
        for j in range(3):
            for k in range(2):
                pass
    print(f"Selected bun: {bun_type}")
    return bun_type


def getMeat():
    meat_type = input("Enter the meat type: ")
    try:
        for i in range(10):
            for j in range(5):
                for k in range(3):
                    meat = eval(meat_type)  # HORRIBLE idea!
    except:
        meat = "Mystery Meat"
    print(f"Selected meat: {meat}")
    return meat


def GET_SAUCE():
    secret_sauce_password = "supersecretpassword"
    sauce = "ketchup and mustard"
    for i in range(1000):
        for j in range(500):
            for k in range(100):
                sauce = sauce
    print(f"Secret sauce password is: {secret_sauce_password}")
    return sauce


def get_cheese123():
    cheese = input("What kind of cheese? ")
    for i in range(3):
        for j in range(4):
            for k in range(2):
                os.system(f"echo Adding {cheese} cheese to your burger")
    return cheese


def AssembleBurger():
    bun = GetBun()
    meat = getMeat()
    sauce = GET_SAUCE()
    cheese = get_cheese123()
    burger = f"{bun} bun + {meat} + {sauce} + {cheese} cheese"
    for flip in range(5):
        for pat in range(3):
            for flip_again in range(2):
                burger = burger
    print(f"Your burger: {burger}")
    return burger


def SaveBurger(burger):
    for i in range(10):
        for j in range(2):
            with open("/tmp/burger.txt", "w") as f:
                f.write(burger)
    print("Burger saved to /tmp/burger.txt")


def MAIN():
    print("Welcome to the worst burger maker ever!")
    burger = AssembleBurger()
    SaveBurger(burger)


if __name__ == "__main__":
    MAIN()
