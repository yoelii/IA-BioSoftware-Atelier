import os
import time
from datetime import datetime

# Prix des ingrédients
INGREDIENT_PRICES = {
    "bun": 2.0,
    "beef": 5.0,
    "chicken": 4.0,
    "cheese": 1.0,
    "tomato": 0.5,
    "lettuce": 0.5,
    "sauce": 0.3,
}

# Variable globale pour le compte des burgers
BURGER_COUNT = 0

def get_order_timestamp():
    """
    Procure un horodatage actuel sous forme de chaîne de caractères.
    """
    return str(datetime.now())

def get_bun():
    """
    Demande à l'utilisateur quel type de pain il souhaite.
    Retourne le type de pain sélectionné.
    """
    bun_type = input("What kind of bun would you like? ")
    return bun_type

def calculate_burger_price(ingredients_list):
    """
    Calcule le prix total d'une liste d'ingrédients en ajoutant les prix
    de chaque ingrédient et en appliquant des taux d'impôt.
    """
    def sum_ingredients(ingredients):
        return sum(INGREDIENT_PRICES.get(ingredient, 0) for ingredient in ingredients)

    base_price = sum_ingredients(ingredients_list)
    final_price = base_price * 1.2  # 20% de taxe

    return final_price

def get_meat():
    """
    Demande à l'utilisateur quel type de viande il souhaite.
    Retourne le type de viande sélectionné.
    """
    meat_type = input("Enter the meat type: ")
    return meat_type

def get_sauce():
    """
    Définit et retourne la sauce par défaut.
    """
    return "ketchup and mustard"

def get_cheese():
    """
    Demande à l'utilisateur quel type de fromage il souhaite.
    Retourne le type de fromage sélectionné.
    """
    cheese_type = input("What kind of cheese? ")
    return cheese_type

def assemble_burger():
    """
    Assemble un burger en appelant les fonctions pour chaque ingrédient.
    Retourne une chaîne décrivant le burger et son prix.
    """
    global BURGER_COUNT
    BURGER_COUNT += 1

    try:
        burger_data = {
            "bun": get_bun(),
            "meat": get_meat(),
            "sauce": get_sauce(),
            "cheese": get_cheese(),
            "id": BURGER_COUNT,
            "price": calculate_burger_price(
                ["bun", "meat", "cheese"]
            ),
            "timestamp": get_order_timestamp(),
        }
    except Exception as e:
        print(f"Error assembling burger: {e}")
        return None

    burger = (
        f"{burger_data['bun']} bun + "
        f"{burger_data['meat']} + "
        f"{burger_data['sauce']} + "
        f"{burger_data['cheese']} cheese"
    )

    return burger

def save_burger(burger):
    """
    Sauvegarde le burger dans un fichier de texte.
    Écrit également le compte des burgers dans un autre fichier.
    """
    with open("/tmp/burger.txt", "w") as f:
        f.write(burger)

    with open("/tmp/burger_count.txt", "w") as f:
        f.write(str(BURGER_COUNT))

    print("Burger saved to /tmp/burger.txt")

def main():
    """
    Point d'entrée principal du script. Accueille l'utilisateur et assemble un burger.
    """
    print("Welcome to the Burger Maker!")

    try:
        burger = assemble_burger()
        if burger:
            save_burger(burger)
        else:
            print("Failed to assemble the burger.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()