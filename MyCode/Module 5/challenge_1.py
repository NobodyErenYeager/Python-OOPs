class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class ElectricVehicle:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def charge(self):
        print(self.battery_capacity)
    
    def get_range(self):
        return self.battery_capacity * 5
    

class GasolineVehicle:
    def __init__(self, fuel_capacity):
        self.fuel_capacity = fuel_capacity

    def refuel(self):
        print(self.fuel_capacity)
    
    def get_range(self):
        return self.fuel_capacity * 20
    

class HybridCar(Vehicle, ElectricVehicle, GasolineVehicle):
    def __init__(self, make, model, year, battery_capacity, fuel_capacity):
        Vehicle.__init__(self, make, model, year)
        ElectricVehicle.__init__(self, battery_capacity)
        GasolineVehicle.__init__(self, fuel_capacity)

    def info(self):
        print("/// INFO ///")
        print(self.make)
        print(self.model)
        print(self.year)
        print(self.battery_capacity)
        print(self.fuel_capacity)
        print("//////")

    def get_range(self):
        battery = ElectricVehicle.get_range(self)
        fuel = GasolineVehicle.get_range(self)
        print(battery + fuel)


prius = HybridCar("Toyota", "Prius", 2022, 5.5, 40)
prius.info()
prius.charge()
prius.refuel()
prius.get_range()
