from abc import ABC ,abstractmethod

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class car(vehicle):

    def start(self):
        print(f" the car is start with key ")

    def __init__(self, name):
        self.name = name

class bike(vehicle):

    def start(self):
        print("The bike start with kick and self_button ")

class truck(vehicle):
    def start(self):
        print("the truck is heavyy engine start when engine is hot")


toyota = car("corolla")
bullet = bike()
tata = truck()

toyota.start()
print(toyota.name)
bullet.start()
tata.start()