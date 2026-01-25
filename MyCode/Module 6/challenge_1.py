class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Employee [Name: {self.name}, ID: {self.id}]"
    
    def __eq__(self, value):
        if isinstance(value, Employee):
            return self.id == value.id
        else:
            return False
        

class Manager(Employee):
    def __init__(self, name, id, department):
        super().__init__(name, id)
        self.department = department

    def __str__(self):
        return f"Manager [Name: {self.name}, ID: {self.id}, Department: {self.department}]"
    
    def __eq__(self, value):
        return super().__eq__(value)
    

class Staff(Employee):
    def __init__(self, name, id, role):
        super().__init__(name, id)
        self.role = role

    def __str__(self):
        return f"Staff [Name: {self.name}, ID: {self.id}, Role: {self.role}]"
    
    def __eq__(self, value):
        return super().__eq__(value)


employee1 = Employee("John Doe", 1)
employee2 = Employee("Jane Doe", 2)

manager1 = Manager("Bruce Bruce",9,"marketing")
manager2 = Manager("Sarah Jane", 8, "sales")

staff1 = Staff("Mark Jones", 12, "Marketing Ops Dev")
staff2 = Staff("Emily Davis", 14, "Software Engineer")


print(employee1)
print(manager1)
print(staff1)

print(employee1 == employee2)
print(staff1 == staff2)
