class Vehicle:
    licensecode = ""
    serialcode = ""
    face = ""
    def turnOnAir(self):
        print("Turn on : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello Car")

class PickUp(Vehicle):
    def sayHello(self):
        print("Hello PickUp")
class Van(Vehicle):
    def sayHello(self):
        print("Hello Van")

class Estate(Vehicle):
    def sayHello(self):
        print("Hello Estate")

car1 = Car()
car1.sayHello()
car1.turnOnAir()
pickup1 = PickUp()
pickup1.sayHello()
pickup1.turnOnAir()
van1 = Van()
van1.sayHello()
van1.turnOnAir()
estate1 = Estate()
estate1.sayHello()
estate1.turnOnAir()




