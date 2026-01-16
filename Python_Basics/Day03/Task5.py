# Task 5: Password Attempt System

correct_password = "python123"   
attempts = 0

while attempts < 3:
    entered = input("Enter password: ")

    if entered == correct_password:
        print("Access Granted")
        break          # stop the loop if password is correct
    else:
        print("Wrong password, try again.")
        attempts += 1  # increase attempt count

# if loop finished without a correct password
if attempts == 3:
    print("Account Locked")
