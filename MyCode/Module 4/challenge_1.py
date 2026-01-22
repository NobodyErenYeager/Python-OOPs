class Animal:
    def __init__(self, region, animal_type, color, lethal):
        self.region = region
        self.animal_type = animal_type
        self.color = color
        self.lethal = lethal

    def animal_bio(self):
        print(f"Region: {self.region}")
        print(f"Animal Type: {self.animal_type}")
        print(f"Color: {self.color}")
        print(f"Lethal: {self.lethal}")


class Clinic(Animal):
    def animal_info(self):
        print(f'This is a {self.animal_type} from {self.region}')

    def search(self, animals):
        for animal in animals:
            if self.region == animal.region:
                print(animal.animal_type)


animals = []

count = int(input("Enter total animals: "))

for _ in range(count):
    region = input("Enter the animal region: ")
    animal_type = input("Enter the animal species: ")
    color = input("Enter the color of the species: ")
    lethal = bool(input("Is it lethal (True/False): "))
    animals.append(Animal(region, animal_type, color, lethal))

clinic = Clinic("Asia", "tiger", "orange", True)
clinic.animal_info()
clinic.search(animals)