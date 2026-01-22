class SuperHero:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def user_power(self):
        print(f"Power: {self.power}")

    def intro(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")

    def save_day(self):
        print(f"{self.name} has saved the day")

    def power_level(self):
        print(f"Power level: {len(self.power)}")


class FlyingSuperHero(SuperHero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed

    def user_power(self):
        print(f'{self.name} flying at as speed of {self.speed} km/h')

    def calc_distance(self, flight_time):
        distance = self.speed * flight_time
        print(distance)


batman = SuperHero("Batman", "Strength")
batman.intro()
batman.power_level()

superman = FlyingSuperHero("Clark Kent", "Everything", 250)
superman.intro()
superman.user_power()
superman.calc_distance(30)
