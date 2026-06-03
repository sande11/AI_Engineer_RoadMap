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