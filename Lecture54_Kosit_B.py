def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    while(usernameInput != "Admin" and passwordInput != "Admin"):
        input("Username : ")
        input("Password : ")
    print("Welcome!")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1:
        print(vatCalculator(int(input("totalPrice : "))))
    elif userSelected == 2:
        print(priceCalculator())
    else:
        print("Wrong Choice!")

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculator(price1 + price2)

print(login())
print(showMenu())
print(menuSelect())
