
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, wheels, persons):
        self.wheels = wheels
        self.persons = persons

    @abstractmethod
    def CalculateToll(self):
        pass


class TwoWheeler(Vehicle):
    def CalculateToll(self):
        toll = 20
        if (self.persons > 2):
            toll = toll + (self.persons - 2) * 10
        return toll


class ThreeWheeler(Vehicle):
    def CalculateToll(self):
        toll = 30
        if (self.persons > 3):
            toll = toll + (self.persons - 3) * 20
        return toll


class FourWheeler(Vehicle):
    def CalculateToll(self):
        toll = 40
        if (self.persons > 4):
            toll = toll + (self.persons - 4) * 40
        return toll


class HeavyVehicle(Vehicle):
    def CalculateToll(self):
        toll = 60
        if (self.persons > 6):
            toll = toll + (self.persons - 6) * 100
        return toll


# Main Module

while True:
    print("\n----- TOLL TAX MENU -----")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if (choice == 5):
        print("Thank you for using Toll System")
        break

    persons = int(input("Enter number of persons: "))

    if (choice == 1):
        v = TwoWheeler(2, persons)

    elif (choice == 2):
        v = ThreeWheeler(3, persons)

    elif (choice == 3):
        v = FourWheeler(4, persons)

    elif (choice == 4):
        wheels = int(input("Enter number of wheels: "))
        if (wheels <= 4):
            print("Heavy vehicle must have more than 4 wheels")
            continue
        v = HeavyVehicle(wheels, persons)

    else:
        print("Invalid choice")
        continue

    print("Total Toll = Rs.", v.CalculateToll())
