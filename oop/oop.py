# OOP's core idea: bundle related data and the functions that act on that data into one unit. That unit is an object.
# The blueprint for making objects is a class.

class User:
    pass

# A class is not a user. It's a blueprint for making users —
# like an architectural drawing isn't a house, it's instructions for building houses.
# To actually build (instantiate) a user from the blueprint:


u = User()

# u is now an object (also called instance) of the class User
# you can make as many objects as you want

#  giving objects there own data
# we want each User to have their own name and email using the __init__ method


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def greet(self):
        return f"hi, i'm {self.name}"


# def __init__(...) — this defines a function that lives inside the class
# A function inside a class is called a method
# The name __init__ (two underscores each side, pronounced "dunder init") is special:
#  Python calls it automatically the moment you build an object. You never call it yourself by name.
# It stands for "initialize" — its job is to set up the new object's starting data.
# self — this is the parameter that confuses everyone, so read slowly. When you write:

u = User("Alice", "alice@example.com")
u1 = User("kelvin", "kelvin@example.com")
# Python does this behind the scenes:

# Creates a fresh, empty object.
# Calls __init__, and passes that brand-new object in as the first argument, which lands in the parameter named self.
# Then passes your arguments: "Alice" → name, "alice@example.com" → email.

print(u.email)
print(u1.name)

# behaviour: methiods that do things
# A method is a function defined in the class that acts on the object. seen in the example above:
# greet takes self as its first parameter — like every method — because it needs access to 
# the object's own data. Inside, self.name fetches this object's name.
print(u1.greet())

