class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name

    @property
    def age(self,age):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age

student1=Student("Olsa", 15)
student1.name="Kiki"
print("Name:",student1.name)