def calculate_total(*numbers) -> int | float:
    """
    Return the sum of any number of numeric values.
    Uses *numbers so the caller is free to pass zero or many arguments.
    """
    # Returning 0 explicitly when nothing is passed keeps behavior clear and predictable
    if not numbers:
        return 0

    # Using a running total so logic is easy to follow and extend if needed
    total = 0
    for value in numbers:
        total += value
    return total


# Tests
print(calculate_total(10, 20, 30))  # Expected: 60
print(calculate_total())            # Expected: 0
