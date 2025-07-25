class PersonalInfo:
    def __init__(self, name, age, city, hobby):
        self.name = name
        self.age = age
        self.city = city
        self.hobby = hobby

    def printPersonalInfo(self):
        print(f"Hello, {self.name}")
        print(f"You are {self.age} years old and live in {self.city}.")
        print(f"In your free time, you enjoy {self.hobby}.")

    @staticmethod
    def inputPersonalInfo():
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        city = input("Enter your city: ")
        hobby = input("Enter your hobby: ")
        return PersonalInfo(name, age, city, hobby)


person = PersonalInfo.inputPersonalInfo()
person.printPersonalInfo()
