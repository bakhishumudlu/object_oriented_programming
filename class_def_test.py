class Calisan:
    def __init__(self, name="girilmedi", surname="girilmedi", age="girilmedi"):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        print(f"Name:{self.name}\tSurname:{self.surname}\tAge:{self.age}")


calisan1 = Calisan("Umudlu","",38)
calisan1.show_info()


