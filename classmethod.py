from datetime import date
class Staff:
    number_of_staff = 0 #Class variables

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Staff.number_of_staff += 1

    def show_info(self): #Instance Methods
        return f"Name:{self.name} Age:{self.age}"

    @classmethod # Class Methods (We don't use 'self')
    def create_from_string(cls, str_):
        name,age = str_.split("-")
        return cls(name, age)

    @classmethod
    def create_with_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    @staticmethod #Static method: We use neither cls nor self.
    def compute_birth_year(person):
        return date.today().year - person.age

# Use of class variables. We can use these variables without creating any instances.
print(Staff.number_of_staff)

# Creation of instances. Name and age are instance variables.
person1 = Staff("Bakhish", 38)
person2 = Staff("Farid", 36)

# We can see that after creation of instances the number of staff increased.
print(Staff.number_of_staff)

# We can create new instance with class method 1.
person3 = Staff.create_from_string("Faig-40")
print(person3.name, person3.age)
print(Staff.number_of_staff)

# Create new instance with class method 2.
person4 = Staff.create_with_birth_year("Lale", 2009)
print(person4.name, person4.age)
print(Staff.number_of_staff)

# How to use static method
print(Staff.compute_birth_year(person1))





