# used to campare the objects not if they are equal but if they are actually the same object with the same memory location
# 'is' returns true if both variables are the same object e.g x is y
# 'is not' returns True is both variables are. not the same object e.g x is not y
#  is - Checks if both variables point to the same object in memory
#  == - Checks if the values of both variables are equal
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x 

print (x is z)
print (x is y)
print (x == y)