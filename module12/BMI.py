class Person:
    def __init__(self, name, age, weight, height_cm):
        self.name = name
        self.age = age
        self.weight = weight
        self.height_cm = height_cm
        self.height_m = height_cm / 100

    def calculate_bmi(self):
        return self.weight / (self.height_m ** 2)

    def bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"

    def display_info(self):
        bmi = self.calculate_bmi()
        category = self.bmi_category()
        print("\n--- BMI RESULT ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("BMI:", round(bmi, 2))
        print("Category:", category)


name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kilograms: "))
height_cm = float(input("Enter your height in centimeters: "))

person = Person(name, age, weight, height_cm)
person.display_info()
