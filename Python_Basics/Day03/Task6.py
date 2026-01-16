# Task 6: Find First Multiple of 7

for num in range(1, 51):        # numbers 1 to 50
    if num % 7 == 0:            # divisible by 7
        print("First multiple of 7 is:", num)
        break                   # stop 
