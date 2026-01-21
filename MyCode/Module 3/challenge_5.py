import random


class Guest:
    def __init__(self, first_name, last_name, rank, age):
        self.first_name = first_name
        self.last_name = last_name
        self.rank = rank
        self.age = age


class GuestList:
    guest_list = []

    def __init__(self):
        pass

    def add_guests(self, guest):
        self.guest_list.append(guest)

    def guest_info(self):
        for guest in self.guest_list:
            print(guest.first_name, guest.last_name, guest.age)

    def loyalty_program(self):
        for guest in self.guest_list:
            if guest.rank >= 10:
                print(f"Gold Members: {guest.last_name}")

    def avg_guest_age(self):
        total_age = 0
        for guest in self.guest_list:
            total_age += guest.age
        
        avg = int(total_age / len(self.guest_list))
        print(f"Average Age: {avg}")


guest_list = GuestList()
guest_list.add_guests(Guest(
    "Bob", "Vance", random.randint(1, 20), random.randint(1, 80)
))
guest_list.add_guests(Guest(
    "Michael", "Scott", random.randint(1, 20), random.randint(1, 80)
))
guest_list.add_guests(Guest(
    "Dwight", "Schrutte", random.randint(1, 20), random.randint(1, 80)
))
guest_list.add_guests(Guest(
    "Jim", "Halpert", random.randint(1, 20), random.randint(1, 80)
))

guest_list.guest_info()
guest_list.loyalty_program()
guest_list.avg_guest_age()