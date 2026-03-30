"""
Strings is a built-in data type in Python that represents a sequence of characters. 
Strings are enclosed in either single quotes (' ') or double quotes (" "). For example:
"""

name = "Kelvin"
age = 30

#String concatenation
conc = name + "is " + str(age) + " years old."
print(conc)

#String formatting
#used to insert variables into a string

#arguments by position
print ("My name is {name} and I am {age}". format(name = name, age = age))
#f-strings (formatted string literals)
print (f'Hello, my name is {name} and i am {age}')

#string methods