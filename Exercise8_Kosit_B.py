UsernameInput = input("Username : ")
PasswordInput = input("Password : ")
if UsernameInput == "Admin" and PasswordInput == "Admin":
    print("Hello Welcome!")
    print("-------Ibrahim Shopping Center--------")
    Price1 = 200
    Price2 = 80
    Price3 = 459
    Price4 = 139
    print("Product :","Price(THB)")
    print("1) ผ้าเช็ดตัว :",Price1)
    print("2) ไม้แขวนเสื้อ :",Price2)
    print("3) โต๊ะ :",Price3)
    print("4) ราวตากผ้า :",Price4)
    userSelect = int(input(">> "))
    if userSelect == 1:
        Product1 = int(input("ต้องการผ้าเช็ดตัวกี่ชิ้น "))
        Product2 = int(input("ต้องการไม้แขวนเสื้อกี่ชิ้น "))
        Product3 = int(input("ต้องการโต๊ะกี่ชิ้น "))
        Product4 = int(input("ต้องการราวตากผ้ากี่ชิ้น "))
    elif userSelect == 2:
        Product2 = int(input("ต้องการไม้แขวนเสื้อกี่ชิ้น "))
        Product1 = int(input("ต้องการผ้าเช็ดตัวกี่ชิ้น "))
        Product3 = int(input("ต้องการโต๊ะกี่ชิ้น "))
        Product4 = int(input("ต้องการราวตากผ้ากี่ชิ้น "))
    elif userSelect == 3:
        Product3 = int(input("ต้องการโต๊ะกี่ชิ้น "))
        Product1 = int(input("ต้องการผ้าเช็ดตัวกี่ชิ้น "))
        Product2 = int(input("ต้องการไม้แขวนเสื้อกี่ชิ้น "))
        Product4 = int(input("ต้องการราวตากผ้ากี่ชิ้น "))
    elif userSelect == 4:
        Product4 = int(input("ต้องการราวตากผ้ากี่ชิ้น "))
        Product1 = int(input("ต้องการผ้าเช็ดตัวกี่ชิ้น "))
        Product2 = int(input("ต้องการไม้แขวนเสื้อกี่ชิ้น "))
        Product3 = int(input("ต้องการโต๊ะกี่ชิ้น "))
    else:
        print("Wrong Choice!!")
    print("Total = ",(Product1*Price1)+(Product2*Price2)+(Product3*Price3)+(Product4*Price4),"THB")
else:
    print("Wrong Password!")




