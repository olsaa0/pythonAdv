# age=25
# print(type(age))
# age_as_str=str(age)
# print(age_as_str,"of type",type(age_as_str))
#
# x=5
# y=4.3
#
# result=x+y
# print(type(result))
#
# age=25
# message="I am"+ str(age) + " years old"
# print(message)
#
# a=5
# b="3"
# print(type(b))
# b1=int(b)
# result2=a+int(b)
# print(type(b))
# print(result2)


# name=input("enter your name:")
# print(f"Hello,{name}")
#
# age=input("enter your age:")
# print(type(age))
#
# num1=int(input("Enter the first number:"))
# num2=int(input("Enter the second number:"))
# result=num1+num2
# print(result)


# try:
#     result=10/2
#     print(result)
# except ZeroDivisionError:
#     print("Opps! Tried to devide to zero")
#
# fruits={
#     "apple":5,
#     "orange":7
# }
#
# try:
#     print(fruits["orange"])
# except KeyError:
#     print("The key does not exist")


try:
     result=10/0
     print(result)
except ZeroDivisionError:
     print("Opps! Tried to devide to zero")
finally:
    print("Finally block excecuted")


def divide_num(a,b):
    try:
        result=a/b
        print(result)
    except ZeroDivisionError:
        print("Invalid division by zero")
    except TypeError:
        print("Invalid type of division")
    except Exception as e:
        print({e})

divide_num(10,2)
divide_num(10,0)
divide_num(10,'2')

