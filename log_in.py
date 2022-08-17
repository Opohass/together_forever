Options= ["1","2","3"]
import login_func
print ("hello")
while True:
    print("enter \n1. to login and\n2. to sign up \n3.to exit")
    choice = input("Enter your choice: ")
    while choice not in Options:
        choice = input("Enter your choice: ")

    if choice == "1":
        userName= input("Enter your name: ")
        userpasswd= input("Enter your password: ")
        if login_func.signin(userName,userpasswd):
            print("login successful")
        else: 
            print("login failed")
    elif choice == "2":
        userName= input("Enter your name: ")
        userpasswd= input("Enter your password: ")
        if login_func.signup(userName,userpasswd):
            print("signup successful")
        else: 
            print("signup failed")
    elif choice == "3":
        print("goodbye!")
        break
    else:
        print("what???!!!")
