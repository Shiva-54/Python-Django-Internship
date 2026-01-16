#Get user input
username=input("Enter username:")
password=input("Enter password:")

if username=="admin" and password=="python123":
    print("Login successful")# when username and password both are correct
elif username!="admin":
    print("User Not Found") #when username and password both are wrong
else: #username is correct but password is wrong
    print("Wrong Passwprd")