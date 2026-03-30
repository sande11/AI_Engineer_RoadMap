"""
Variables are used to store data in a program. 
They can hold different types of data, such as numbers, strings, lists, and more. 
In Python, you can create a variable by simply assigning a value to it using the equals sign (=). For example:
"""

# Creating a variable and assigning a value to it
x = 1 #int 
y = 3.14 #float
name = "Alice" #string
is_student = True #boolean


#OR
x, y, name, is_student = (1, 3.14, "Alice", True)


#Math 
a = x + y
print(a)

#type
print(type(x))

#casting (e.g turning x an int into a string)
x = str(x)
print(type(x))

#turning y into an int
y = int(y)
print(type(y))
print(y)