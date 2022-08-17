


Options= ["1","2"]
import login_func
print ("hello")
print("enter 1. to login and,2. to sign up")

choise = input("Enter your choise: ")
while choise not in Options:
    choise = input("Enter your choise: ")

if choise == "1":
    userName= input("Enter your name: ")
    userpasswd= input("Enter your password: ")
    if login_func.signin(userName,userpasswd):
        print("login successful")
    else: 
        print("login failed")
elif choise == "2":
    userName= input("Enter your name: ")
    userpasswd= input("Enter your password: ")
    if login_func.signup(userName,userpasswd):
        print("login successful")
    else: 
        print("login failed")
else:
    print("what???!!!")
