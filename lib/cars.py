class Car:

    def __init__(self, make, model, year):
        # Initializes the Car with make, model, and year.
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """Displays the car's information."""
        print(f"Car Information: {self.year} {self.make} {self.model}")


if __name__ == "__main__":

    my_car = Car(make="Toyota", model="Camry", year=2022)
    
    # Display information about the car
    my_car.display_info()  
