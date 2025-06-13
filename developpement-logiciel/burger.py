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

def get_order_timestamp() -> str:
    """Obtient un horodatage actuel sous forme de chaîne de caractères."""
    return str(datetime.now())

def get_bun() -> str:
    """
    Demande à l'utilisateur quel type de pain il souhaite.
    Retourne le type de pain sélectionné.
    """
    return input("What kind of bun would you like? ")

def calculate_burger_price(ingredients_list) -> float:
    """
    Calcule le prix total d'une liste d'ingrédients en ajoutant les prix
    de chaque ingrédient et en appliquant un taux d'impôt de 20%.
    """
    def sum_ingredients(ingredients):
        return sum(INGREDIENT_PRICES.get(ingredient, 0) for ingredient in ingredients)

    base_price = sum_ingredients(ingredients_list)
    return base_price * 1.2  # 20% de taxe

def get_meat() -> str:
    """Demande à l'utilisateur quel type de viande il souhaite.

    Retourne le type de viande sélectionné.
    """
    return input("Enter the meat type: ")

def get_sauce() -> str:
    """Définie et retourne la sauce par défaut."""
    return "ketchup and mustard"

def get_cheese() -> str:
    """
    Demande à l'utilisateur quel type de fromage il souhaite.

    Retourne le type de fromage sélectionné.
    """
    return input("What kind of cheese? ")

def assemble_burger() -> str:
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
            "price": calculate_burger_price(["bun", "meat", "cheese"]),
            "timestamp": get_order_timestamp(),
        }
    except Exception:
        return None

    return (
        f"{burger_data['bun']} bun + "
        f"{burger_data['meat']} + "
        f"{burger_data['sauce']} + "
        f"{burger_data['cheese']} cheese"
    )

def save_burger(burger: str) -> None:
    """
    Sauvegarde le burger dans un fichier de texte.

    Écrit également le compte des burgers dans un autre fichier.
    """
    with open("/tmp/burger.txt", "w") as f:
        f.write(burger)

    with open("/tmp/burger_count.txt", "w") as f:
        f.write(str(BURGER_COUNT))

def main() -> None:
    """
    Point d'entrée principal du script. Accueille l'utilisateur
    et assemble un burger.
    """
    burger = assemble_burger()
    if burger:
        save_burger(burger)

if __name__ == "__main__":
    main()