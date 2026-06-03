# Python has two primitive loop commands:
# while loops
# for loops

# With the while loop we can execute a set of statements as long as a condition is true.
# i = 1
# while i < 6:
#   print(i)
#   i += 1

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.
# With the break statement we can stop the loop even if the while condition is true:
# y = 1
# while y < 9:
#   print(y)
#   if y == 3:
#     break
#   y += 1

# With the continue statement we can stop the current iteration, and continue with the next:
y = 1
while y < 9:
    y += 1
    if y == 3:
        continue
    print(y)
    
# output differences between break and continue
# kelvinsande@Kelvins-MacBook-Air python_basics % python3 loops.py
# break statement
# 1
# 2
# 3
# kelvinsande@Kelvins-MacBook-Air python_basics % python3 loops.py
# continue statement
# 2
# 4
# 5
# 6
# 7
# 8
# 9

# With the else statement we can run a block of code once when the condition no longer is true:
i =1
while i < 9:
    print(i)
    i += 1
else:
    print("no match")

# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# With the break statement we can stop the loop before it has looped through all the items:

# Example
# Exit the loop when x is "banana":

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#   With the continue statement we can stop the current iteration of the loop, and continue with the next:
# Example
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#   The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)