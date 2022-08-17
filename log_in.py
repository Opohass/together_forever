Options= ["1","2","3"]
import login_func
import clintTest
print ("hello")
print("enter \n1. to login and\n2. to sign up \n3.to exit")

choise = input("Enter your choise: ")
while True:
    while choise not in Options:
        choise = input("Enter your choise: ")

    if choise == "1":
        userName= input("Enter your name: ")
        userpasswd= input("Enter your password: ")
        if clintTest.chek_login(userName,userpasswd):
            print("login successful")
        else: 
            print("login failed")
    elif choise == "2":
        userName= input("Enter your name: ")
        userpasswd= input("Enter your password: ")
        if clintTest.add_login(userName,userpasswd):
            print("signup successful")
        else: 
            print("signup failed")
    elif choise == "3":
        print("goodbye!")
        break
    else:
        print("what???!!!")
    choise= None
