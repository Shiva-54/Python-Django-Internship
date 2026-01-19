def process_order(item: str, quantity: int = 1, **options) -> None:
    """
    Calculate and print the final bill for an order.
    Uses default arguments, keyword options, and conditional pricing logic.
    """
    # Base prices are kept in a dict so adding new items stays simple and centralized
    base_prices = {
        "pizza": 200,
        "burger": 120
    }

    normalized_item = item.lower().strip()

    # Validate item to avoid calculating a bill for something not on the menu
    if normalized_item not in base_prices:
        print("Item not available")
        return

    # Start with base price multiplied by quantity so quantity logic stays explicit
    base_price = base_prices[normalized_item]
    total = base_price * quantity

    # Options use kwargs so the caller can flexibly specify extra features
    extra_cheese = options.get("extra_cheese", False)
    home_delivery = options.get("home_delivery", False)

    # Add-on for cheese is separate so pricing rules are easy to adjust later
    if extra_cheese:
        total += 50

    # Delivery fee separated so it can be toggled independently of other options
    if home_delivery:
        total += 30

    print(f"Final bill for {quantity} {normalized_item}(s): ₹{total}")


# Example tests:
process_order("pizza", 2, extra_cheese=True, home_delivery=True)
process_order("burger", home_delivery=True)
process_order("pizza")
process_order("pasta", quantity=1)
