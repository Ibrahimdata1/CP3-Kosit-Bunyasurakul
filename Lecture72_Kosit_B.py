menuList = []
def showBill():
    print("-------Welcome to our restaurant-------")
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])



while True:
    menuName = input("Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append([menuName,menuPrice])

showBill()