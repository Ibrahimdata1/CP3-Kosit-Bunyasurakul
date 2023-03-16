menuList = []
priceList = []
while True:
    menuName = input("Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = int(input("Price: "))
        menuList.append(menuName)
        priceList.append(menuPrice)

def showBill():
    print("-------Welcome to our restaurant-------")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
showBill()
print("Total :",sum(priceList))




