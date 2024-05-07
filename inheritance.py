from datetime import date
class Staff:
    salary_increase = 1.1
    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def show_info(self):
        return "Name:{} Surname:{} Age:{} Salary:{} ".format(self.name, self.surname, self.age, self.salary)

    @classmethod
    def create_with_birth_year(cls, name, surname, birth_year, salary):
        return cls(name, surname, date.today().year - birth_year, salary)

    @classmethod
    def create_from_string(cls, str_):
        name, surname, age, salary = str_.split("-")
        return cls(name, surname, age, salary)

class Developer(Staff): #Inheritance
    def __init__(self, name, surname, age, salary, language=""):
        super().__init__(name, surname, age, salary) #We get these variables from super class.
        self.language = language
    def show_info(self):
        return "Name:{} Surname:{} Age:{} Salary:{} Language:{}".format(self.name, self.surname, self.age, self.salary, self.language)

personel1 = Staff("Bakhish", "Umudlu", 38, 5000)
developer1 = Developer("Farid", "Umudlu", 36, 8000, "Python")

personel2 = Staff.create_with_birth_year("Zeynab", "Umudlu", 2009, "3000")
personel3 = Staff.create_from_string("Lale-Umudlu-20-4500")

print(personel1.show_info())
print(developer1.show_info())
print(personel2.show_info())
print(personel3.show_info())

# We can use super class variables in child classes.
print(developer1.salary_increase)


