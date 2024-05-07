class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            return value / len(self.students)


s1 = Student("Lalenur", 15, 85.0)
s2 = Student("Zeyneb", 14, 75.0)
s3 = Student("Cinar", 11, 70.0)

course = Course("Science", 2)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

print(course.students[1].name)

