class Car:
    def __init__(self,brand,model,year,owner=None):
        self.brand=brand
        self.model=model
        self.year=year
        self.__owner=owner
    
    def start_engine(self):
        print(f"The engine of {self.brand} {self.model} is starting.")

    def show_info(self):
        print(f"Car info: {self.year} {self.brand} {self.model}")
    
    def set_owner(self,owner):
        if not self.__owner:
            self.__owner=owner
        else:
            print(f"The car already has a owner: {self.__owner}. Cannot change")

    def get_owner(self):
        return self.__owner

car1=Car("Toyota","Camry",2020)
car2=Car("Honda","Civic",2021)

car1.set_owner("MAdhumitha")
car2.set_owner("Vidya")
car2.set_owner("lakshmi")
print("Owner of car1:", car1.get_owner())
print("Owner of car2:", car2.get_owner())

car1.start_engine()
car1.show_info()

car2.start_engine()
car2.show_info()

cars=[car1,car2]
for car in cars:
    car.start_engine()
    car.show_info()