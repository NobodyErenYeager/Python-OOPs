import random


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades


class OnlineCourse:
    name: str
    instructor: str
    students: list = []

    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        print(f"New course created: {self.name}")
        print(f"Instructor: {self.instructor}")

    def enroll_student(self, student: Student):
        self.students.append(student)
        print(f"{student.name} is enrolled to the course")

    def get_course_details(self):
        print(f"Course Name: {self.name}")
        print(f"Instructor: {self.instructor}")
        print("Students: ")
        for student in self.students:
            print(f"\t{student.name} (Avg.: {(sum(student.grades) / len(student.grades)):0.2f})")

    def complete_course(self, name):
        for student in self.students:
            if student.name in name:
                self.students.remove(student)
                print(f"Congratulations {student.name} on completing the course")
                break
        print(f"{student.name} is not enrolled to this course")

    def calculate_average_grade(self):
        grades = 0
        for student in self.students:
            avg = sum(student.grades) / len(student.grades)
            grades += avg
        
        average = f"{(grades / len(self.students)):0.2f}"
        print(f"Average of the Course: {average}")


new_course = OnlineCourse("Python OOPs", "Josh")
deepak = Student("Deepak", [random.randint(1, 100) for _ in range(3)])
new_course.enroll_student(deepak)
new_course.enroll_student(Student("John", [random.randint(1, 100) for _ in range(3)]))
new_course.enroll_student(Student("Bob", [random.randint(1, 100) for _ in range(3)]))
new_course.enroll_student(Student("Samson", [random.randint(1, 100) for _ in range(3)]))
new_course.get_course_details()
new_course.complete_course(deepak)
new_course.complete_course(Student("John", [random.randint(1, 100) for _ in range(3)]))
new_course.calculate_average_grade()
