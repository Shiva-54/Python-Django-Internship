# Task 3: Movie Eligibility
# Conditions:
# - Age >= 18 and ID card = yes -> Entry Allowed
# - Else -> Entry Denied

# Input from user
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
has_id = input("Do you have ID card? (yes/no): ").lower()

# Check eligibility
if user_age >= 18 and has_id == "yes":
    print(f"{user_name}, Entry Allowed")
else:
    print(f"{user_name}, Entry Denied")
