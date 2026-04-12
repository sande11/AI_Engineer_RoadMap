"""
Strings is a built-in data type in Python that represents a sequence of characters. 
Strings are enclosed in either single quotes (' ') or double quotes (" "). For example:
"""

name = "Kelvin"
age = 30

#String concatenation
conc = name + "is " + str(age) + " years old."
# print(conc)

#String formatting
#used to insert variables into a string

#arguments by position
# print ("My name is {name} and I am {age}". format(name = name, age = age))
#f-strings (formatted string literals)
# print (f'Hello, my name is {name} and i am {age}')

#string methods
#string methods are built-in functions you can call on a string using dot notation.
"hello".upper()       # 'HELLO'
"HELLO".lower()       # 'hello'
"python".capitalize() # 'Python'
"python rocks".title()# 'Python Rocks'
"PyThOn".swapcase()   # 'pYtHoN'

"  hi  ".strip()      # 'hi'
"  hi  ".lstrip()     # 'hi  '
"  hi  ".rstrip()     # '  hi'

"hello world".replace("world", "Python")   # 'hello Python'

"abc".isalpha()      # True
"123".isdigit()      # True
"abc123".isalnum()   # True
"hello".islower()    # True
"HELLO".isupper()    # True
"   ".isspace()      # True

"hello".find("e")         # 1
"hello".index("e")        # 1
"hello".startswith("he")  # True
"hello".endswith("lo")    # True
"banana".count("a")       # 3

school = 'kasungu demo'
print(school.upper([0]))