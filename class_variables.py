class Staff: #Class variables
    number_of_staff = 0
    salary_increase_rate = 1.1

    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        Staff.number_of_staff += 1

print(f"Number of staff: {Staff.number_of_staff}")
staff1 = Staff("Baxış", "Umudlu", 38, 5000)
staff2 = Staff("Farid", "Umudlu", 36, 10000)
print(f"New staff created: {staff1.__dict__}")
print(f"New staff created: {staff2.__dict__}")

print(f"Number of staff: {Staff.number_of_staff}")

print(Staff.salary_increase_rate)
print(staff1.salary_increase_rate)
print(staff2.salary_increase_rate)

staff1.salary_increase_rate = 1.2
print(Staff.salary_increase_rate)
print(staff1.salary_increase_rate)
print(staff2.salary_increase_rate)




