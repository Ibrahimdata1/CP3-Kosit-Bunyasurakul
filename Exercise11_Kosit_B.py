number = int(input("Enter number of rows : "))
for x in range(number):
    for y in range(number-x-1):
        print(end=" ")
    for y in range((2*x)+1):
        print("*",end="")
    print()

