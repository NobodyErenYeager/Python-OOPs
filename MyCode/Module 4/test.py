import random


class Main:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def user_info(self):
        print(f"Wecome {self.name}")
        print(f"You are {self.age}")
        print(f"You live in {self.location}")


class User(Main):
    def __init__(self, name, age, location, score):
        super().__init__(name, age, location)
        self.score = score

    # def user_info(self):
    #     super().user_info()
    #     print(f"Your scores: {self.score}")


    def check_avg(self):
        # super().user_info()
        self.user_info()
        avg = sum(self.score) / len(self.score)
        print(f"Avg Score: {avg}")


user = User("Michael Scott", 44, "Scranton, Pennsylvania", [random.randint(1, 100) for _ in range(5)])
# user.user_info()
user.check_avg()
