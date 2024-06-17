from enum import Enum
from abc import ABC, abstractmethod

# Enum to represent vehicle types
class VehicleType(Enum):
    CAR = "car"
    BIKE = "bike"
    TRUCK = "truck"


# Product interface
class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

# Concrete products
class Car(Vehicle):
    def drive(self):
        return "Driving a car"

class Bike(Vehicle):
    def drive(self):
        return "Riding a bike"

class Truck(Vehicle):
    def drive(self):
        return "Driving a truck"

# Factory class
class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == VehicleType.CAR:
            return Car()
        elif vehicle_type == VehicleType.BIKE:
            return Bike()
        elif vehicle_type == VehicleType.TRUCK:
            return Truck()
        else:
            raise ValueError("Invalid vehicle type")

# Client code using the Factory pattern
def main_factory_example():
    vehicle_factory = VehicleFactory()

    car = vehicle_factory.create_vehicle(VehicleType.CAR)
    print(car.drive())

    bike = vehicle_factory.create_vehicle(VehicleType.BIKE)
    print(bike.drive())

    truck = vehicle_factory.create_vehicle(VehicleType.TRUCK)
    print(truck.drive())

if __name__ == "__main__":
    main_factory_example()
