# smart_menu.py
# PART 1


def food_menu(choice: str) -> None:
    """
    Decide and print the price of a menu item based on user's choice.
    Uses match-case for clear, scalable decision logic.
    """
    # Using match-case to keep each menu option separate and easy to extend later
    match choice.lower():  # Lowercasing so input is user-friendly (case-insensitive)
        case "pizza":
            # Pizza is priced higher as it typically has more ingredients and prep effort
            print("Price of pizza: ₹250")
        case "burger":
            # Burger is mid-range to reflect simpler preparation than pizza
            print("Price of burger: ₹150")
        case "coffee":
            # Coffee is the cheapest as it uses fewer ingredients and quick preparation
            print("Price of coffee: ₹100")
        case _:
            # Default branch handles any item that is not on the menu
            print("Item not available")


# Simple manual tests (you can remove or comment these out in production)
if __name__ == "__main__":
    food_menu("pizza")
    food_menu("burger")
    food_menu("coffee")
    food_menu("sandwich")
