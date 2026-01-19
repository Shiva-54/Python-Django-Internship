def greet_user(name: str, role: str = "student") -> None:
    """
    Greet the user differently based on the given role.
    Uses a default role so the function stays simple to call.
    """
    # Using role-based branching so behavior can grow with more roles later
    if role == "student":
        print("Welcome student")
    elif role == "admin":
        print("Welcome admin")
    else:
        # Handles any unexpected role to keep output predictable
        print("Welcome user")


# Function calls as required:

# 1) Called with only the name (role uses default: 'student')
greet_user("Aman")

# 2) Called with name + role using a keyword argument
greet_user(name="Riya", role="admin")
