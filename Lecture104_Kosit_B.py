class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Add to",self.name,self.lastname,"'s cart")

customer1 = Customer()
customer1.name = "IBrahim"
customer1.lastname = "Dasdasdasdsa"
customer1.addCart()

customer2 = Customer()
customer2.name = "Zafeenah"
customer2.lastname = "binkazan"
customer2.addCart()

customer3 = Customer()
customer3.name = "AMadad"
customer3.lastname = "deadadadade"
customer3.addCart()

customer4 = Customer()
customer4.name = "blonasd"
customer4.lastname = "sdasdasd"
customer4.addCart()