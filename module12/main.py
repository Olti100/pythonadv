from abc import ABC, abstractmethod

# ---------- Abstract Base Class ----------
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    # Encapsulation with property decorators
    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be positive")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")


# ---------- Adult Class ----------
class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


# ---------- Child Class ----------
class Child(Person):
    def calculate_bmi(self):
        adjustment_factor = 0.9
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"


# ---------- BMI Application Class ----------
class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def display_all(self):
        for person in self.people:
            person.print_info()


# ---------- Main Program ----------
def main():
    app = BMIApp()

    while True:
        print("\n1. Add Person")
        print("2. Show All")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            age = int(input("Age: "))
            weight = float(input("Weight (kg): "))
            height = float(input("Height (m): "))

            if age >= 18:
                person = Adult(name, age, weight, height)
            else:
                person = Child(name, age, weight, height)

            app.add_person(person)
            print("Person added successfully!")

        elif choice == "2":
            app.display_all()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()