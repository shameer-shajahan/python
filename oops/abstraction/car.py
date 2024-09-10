
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelearte(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Swift(Car):

    def start(self):
         print("start method is start")
         
    def accelearte(self):
         print("accelerate method is start")

    def stop(self):
         print("stop method is start")

Car1=Swift()

Car1.start()
