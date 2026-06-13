# reusable code

# def greet():
#     print("hi there")
#     print("welcome aboard")


# greet()
# # passing arguments
# def greet( first_name, last_name):
#     # the f is for comverting to a formatted string
#     print(f"hi {first_name} {last_name}")
#     print("welcome aboard")


# greet("kelvin", "sande")

# types of functions
# performs a task
# returns a value

# converting temperature function example

# def convert_temp (fahrenheit):
#     return (fahrenheit - 32) * 5 / 9

# print(convert_temp(77))
# print(convert_temp(55))


# You can assign default values to parameters. If the function is called without an argument, it uses the default value:

# Example
# def my_function(name = "friend"):
#   print("Hello", name)

# my_function("Emil")
# my_function("Tobias")
# my_function()
# my_function("Linus")

# Using *args to accept any number of arguments when you dont know how many arguments you will need:

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# You can combine regular parameters with *args.

# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)

# my_function("Hello", "Emil", "Tobias", "Linus")

# Arbitrary Keyword Arguments - **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.

# This way, the function will receive a dictionary of arguments and can access the items accordingly:
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# Decorators let you add extra behavior to a function, without changing the function's code.
# A decorator is a function that takes another function as input and returns a new function.

def changecase(func):
    def myinner():
        return func().upper()
    return myinner


@changecase
def myfunction():
    return "Hello Sally"


print(myfunction())
