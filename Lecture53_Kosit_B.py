def vatCalculate ():
    totalPrice = int(input("totalPrice : "))
    result = totalPrice + (totalPrice*7/100)
    return "Vat",result
print(vatCalculate())
