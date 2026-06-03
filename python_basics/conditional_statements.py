# if statements
# x = 1
# if (x == 1):
#     print('true')

# a = 5
# b = 10

# if (a > b):
#     print('a is greater than b')
# else:
#     print('a is less than b')

# multiple conditions

# c = 10
# d = 23

# if ((c > 23) and (d > 25)):
#     print('both them numbers are greater than 20')

# elif ((c == 10) and (d == 23)):
#     print('c and d match the expected values')

# else:
#     print('no they are not')


# Nested If
# age = 25
# has_license = True


# if age >= 25:
#     if has_license:
#         print("user can drive")
#     else:
#         print("you need a licence")
# else:
#     print("user cant drive")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if
#  statement with no content, put in the pass statement to avoid getting an error.
# a = 33
# b = 200

# if b > a:
#   pass
# # or
# age = 16

# if age < 18:
#   pass # TODO: Add underage logic later
# else:
#   print("Access granted")

# Python Match
# The match statement is used to perform different actions based on different conditions.
# instead of writing many if...else statements, you can use match statements

# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

day = 4
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3: 
        print("wednesday")
    case 4:
        print("thurday")
    case 5:
        print("friday")

# OR
month = 4
match month:
    case 1 | 2 | 3 | 4 | 5:
        print("today is a weekday")
    case 6 | 7:
        print("i love weekends")

#you can also add if statements as guards to the match statements
month = 4
match month:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("today is a weekday")
    case 6 | 7 if month == 5:
        print("i love weekends")
    # then you can also add a default
    case _:
        print("no match")