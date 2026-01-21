class App:
    
    def __init__(self, user, storage, username):
        self.user = user
        self.storage = storage
        self.username = username
        self.login()


    def login(self):
        if self.username == "owner" and self.user > 1:
            print(f"Hello {self.username}")
        else:
            print("Login Denied")

    def increase_storage(self, number):
        self.storage += number
        print(f"Storage increased to {self.storage}")

    def check_storage(self):
        if self.user > self.storage:
            storage = int(input("Enter the storage: "))
            self.storage += storage
            print(f"Storage upgraded to {self.storage}")
        else:
            print(f"You have {self.storage - self.user} slots left")


print("/////////// USER 1 ///////////")
user_1 = App(25, 10, "owner")
# user_1.login()
user_1.increase_storage(90)
print("/////////// USER 2 ///////////")
user_2 = App(25, 10, "deepak")
# user_2.login()
# user_2.increase_storage()
user_2.check_storage()
print("/////////// USER 3 ///////////")
user_3 = App(10, 50, "deepak")
# user_2.login()
# user_2.increase_storage()
user_3.check_storage()
