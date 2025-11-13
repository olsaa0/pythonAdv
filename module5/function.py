# def greet():
#     print("Hello World")
#
# greet()
#
# def greet_person(name):
#     print("Hello",name)
#
# greet_person("Olsa")
# greet_person("Kiki")

# local variable(mrena funksionit veq, del error nqita)
# def greet(name):
#     message=f"Hello, {name}"
#     print(message)
#
# greet("alice")
#  print(message)


# global variable (no errors)
# greeting="hello"
#
# def greet(name):
#     message=f"{greeting},{name}"
#     print(message)
#
# greet("bob")
# print(greeting)


# def greet():
#     global greeting
#     greeting="goodbye"
#     name="Alice"
#
#     message=f"{greeting}, {name}"
#     print(message)
# greet()
# print(greeting)


def greet_person(name,greeting="Hello"):
    message=f"{greeting},{name}"
    return message

print(greet_person("Alice"))
print(greet_person(name:"Bob, greeting:"Hi))
