def traffic_action(color: str) -> None:
    """
    Print the appropriate driving action for a given traffic light color.
    Keeps the mapping simple so it matches common traffic rules.
    """
    normalized = color.lower().strip()  # Normalize to handle extra spaces and case

    # Using straightforward if-elif to keep three clear, mutually exclusive options
    if normalized == "red":
        # Red always means vehicles must stop for safety
        print("Stop 🚫")
    elif normalized == "yellow":
        # Yellow warns drivers to get ready to move or stop, depending on context
        print("Ready ⚠️")
    elif normalized == "green":
        # Green gives drivers permission to move ahead
        print("Go ✅")
    else:
        # Any other input is treated as invalid to avoid unsafe assumptions
        print("Invalid signal")


# Quick manual checks
if __name__ == "__main__":
    traffic_action("red")
    traffic_action("yellow")
    traffic_action("green")
    traffic_action("blue")
