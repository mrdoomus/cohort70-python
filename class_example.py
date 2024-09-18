class Car:
    def __init__(self, color, price, km, model):
        self.color = color   
        self.price = price  
        self.km = km    
        self.model = model

    def display_info(self):
        print(f"This car is a {self.color} {self.model} with {self.km}km at a price of ${self.price}.")

    def forward(self):
        print("The car is moving forward")

    def stop(self):
        print("The car has stopped")
    
    def backwards(self):
        print("The car is moving backwards")


my_car = Car("Red", 23000, 1200, "Audi")

my_car.display_info()
my_car.forward()
my_car.backwards()
my_car.stop()

my_car_2 = Car("Gray Machine", 15000, 57000, "Mazda")
my_car_2.display_info()

