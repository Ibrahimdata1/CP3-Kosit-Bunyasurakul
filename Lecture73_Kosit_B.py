menuList = []
systemMenu = {"ข้าวหมกไก่":45,"ข้าวหน้าไก่":40,"ข้าวหมกแพะ":65}
def showBill():
    print("-------Welcome to our restaurant-------")
    total = 0
    for number in range(len(menuList)):
        print("เมนู",menuList[number][0],"ราคา",menuList[number][1])
        total += menuList[number][1]
    print("Total Price: ",total,"Baht")



while True:
    menuName = input("Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

showBill()