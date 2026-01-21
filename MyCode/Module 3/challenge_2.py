import random


class OnlineCourse:
    name: str
    instructor: str
    students: list = []

    def __init__(self, name, instructor):
        self.name = name
        self.instructor = instructor
        print(f"New course created: {self.name}")
        print(f"Instructor: {self.instructor}", end="\n")


    def enroll_student(self, student_name):
        self.students.append(student_name)
        print(f"New student {student_name} is enrolled to {self.name}", end="\n")

    def get_course_details(self):
        print(f"Course Name: {self.name}")
        print(f"Instructor: {self.instructor}")
        print("Students: ")
        for student in self.students:
            print(f"\t{student}")
        print("\n")

    def complete_course(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"Congratulations {student_name} on completing the course")
        else:
            print(f"{student_name} is not enrolled to this course")

    def calculate_average_grade(self, grades: list):
        average = sum(grades) / len(grades)
        print(f"{average:.02f} is the average grade for this course")


new_course = OnlineCourse(name="Python OOPs", instructor="Josh")
new_course.enroll_student("Deepak")
new_course.enroll_student("Harish")
new_course.get_course_details()
new_course.complete_course("Deepak")
new_course.complete_course("Samson")
new_course.calculate_average_grade([random.randint(1, 100) for _ in range(100)])
