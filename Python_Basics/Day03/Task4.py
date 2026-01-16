# Task 4: Number Analyzer

for num in range(1, 21):      # from 1 to 20
    if num == 13:
        continue              # skip 13

    if num % 2 == 0:
        print(num, "Even")
    else:
        print(num, "Odd")
