""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

class Vehicle:

    def __int__(self , brand , model , year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"Brand: {self.brand} , model: {self.model} , year: {self.year}"


class Car(Vehicle):

    def __int__(self , brand , model , year , number_of_doors):
        super().__int__(self , brand , model , year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Brand: {self.brand} , model: {self.model} , year: {self.year} , doors: {self.number_of_door}"
    
myCar = Car("Toyota" , "Prius" , 2022 , 5)
print(myCar.get_info())
