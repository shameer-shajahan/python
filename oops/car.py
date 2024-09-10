

class Car:

    name:str

    number:int

    company:str

    def __init__(self,name,number,company):

        self.name=name

        self.number=number

        self.company=company

    def display_car(self):

        print(self.name,self.number,self.company) 

car1=Car("swift",8716,"suzuki") 

car2=Car("m4",8717,"bmw")  

car3=Car("nexon",8718,"tata")  

car1.display_car()

# print(car1)