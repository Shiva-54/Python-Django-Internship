#  Task 4: Operator Story

print("=== Task 4: Operator Story ===")

# Ask the user for two numbers
first = float(input("Hey friend! Enter your first number: "))
second = float(input("Nice! Now enter your second number: "))

print("Cool, let’s play with these numbers!")

# Show results using arithmetic operators
print("Addition:       ", first, "+", second, "=", first + second)
print("Subtraction:    ", first, "-", second, "=", first - second)
print("Multiplication: ", first, "*", second, "=", first * second)
if second != 0:
    print("Division:       ", first, "/", second, "=", first / second)
else:
    print("Division:       Cannot divide by zero, that's illegal in math!")

# Compare the two numbers
print("Now let’s compare them:")
if first > second:
    print(first, "is bigger than", second)
elif first < second:
    print(second, "is bigger than", first)
else:
    print("Both numbers are equal!")

# Logical decision using if-else
print("Logical decision time:")
if (first + second) > 100:
    print("Wow! Their sum is greater than 100. That’s a big combo!")
else:
    print("Their sum is 100 or less. A small but mighty pair!")