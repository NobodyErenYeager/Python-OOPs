class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    

class CanFly:
    # def __init__(self, name):
    #     self.test = name

    def fly(self):
        print(f"{self.name} is flying")


class Bird(Animal, CanFly):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def sleep(self):
        print(f"The {self.color} bird is sleeping")


my_bird = Bird("Canary", "black")
my_bird.eat()
my_bird.fly()
my_bird.sleep()
print(Bird.mro())


class Pen:
    def __init__(self, name):
        self.name = name

    def write(self):
        print(f"{self.name} pen is writing")


class Fountain:
    def refill(self):
        print(f"{self.name} pen is being refilled with {self.color} ink")


class CartridgePen(Pen, Fountain):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def info(self):
        print(f"Name: {self.name}")
        print(f"Color: {self.color}")


my_pen = CartridgePen("Reynolds", "blue")
my_pen.info()
my_pen.write()
my_pen.refill()

