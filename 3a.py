class Vehicle():
    def __int__(self):
        self.tyres = 4
    def sound(self):
        print("vehicle sound")

class Bike(Vehicle):
    def __init__(self):
        self.tyres = 2
    def sound(self):
        print("brrrrrroooommmm !! sound")

class Car(Vehicle):
    def __init__(self):
        self.tyres = 4
    def sound(self):
        print("vrrrrrroooommmm !! sound")

class PedalBike(Bike):
    def __init__(self):
        self.tyres = 3
    def sound(self):
        print("PEDAL brrrrrroooommmm !! sound")

class MotorBike(Bike):
    def __init__(self):
        self.tyres = 5
    def sound(self):
        print("MOTOR brrrrrroooommmm !! sound")

suzuki = MotorBike()
print(suzuki.tyres)
suzuki.sound()
