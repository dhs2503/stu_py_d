class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year  # Fixed the typo here (removed the space)
    
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # This will output: 2020 Toyota Corolla

print("This program is Written and Executed by DHAANI SANGWAN(0221BCA060)")