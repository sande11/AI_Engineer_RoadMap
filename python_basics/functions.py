# reusable code

def greet():
    print("hi there")
    print("welcome aboard")


greet()
# passing arguments
def greet( first_name, last_name):
    # the f is for comverting to a formatted string
    print(f"hi {first_name} {last_name}")
    print("welcome aboard")


greet("kelvin", "sande")

# types of functions
    # performs a task
    # returns a value

# converting temperature function example

def convert_temp (fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(convert_temp(77))
print(convert_temp(55))