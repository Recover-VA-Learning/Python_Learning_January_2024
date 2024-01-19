# Print to screen
print("Hello, world!")

# region user input

# Ask user for name input
name = input("What's your name? ")
print("hello,")
print(name)

# endregion

# region formatting

# Formatting string
name = input("What's your name? ")
print(f"hello, {name}")

# endregion

# region methods

# String methods
name = input("What's your name? ")
name = name.strip().upper()
print(f"hello, {name}")

# endregion

# region ints

# Integers
x = 5
y = 6
z = x + y
print(z)

# endregion

# region modify ints

# Ask user for age
age = input("What's your age? ")
modifier = input("What to add to age? ")

new_age = age + modifier
print(new_age)

# endregion

# region correct modify ints

# Ask user for age
age = input("What's your age? ")
modifier = input("What to add to age? ")

# cast input strings to int
new_age = int(age) + int(modifier)
# or can directly cast the input statement like 'age = int(input(""What's your age? "))'
print(new_age)

# endregion

# region float basics

# Ask user for float
float_input = float(input("Type a decimal number? "))
modifier = float(input("What to add to number? "))

result = float_input + modifier
print(result)

# endregion

# region more float

numerator = float(input("what is numerator? "))
denominator = float(input("What is denominator? "))

result = numerator / denominator

print(result)
print(f"{result:.2f}") # format string to be to 2 decimal places
# can also use a built in method for rounding
print(round(result)) # by default rounds to nearest int
print(round(result, 3))

# endregion

# region functions basics

def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

# endregion

# region func parameters

def hello(name="world"):
    print("hello,", name)

hello()
name = input("What's your name? ")
hello(name)

#endregion

# region main function

def main():

    # Output using our own function
    user_input = input("What's your name? ")
    hello(user_input)

    # Output without passing the expected arguments
    hello()

# Create our own function
def hello(name="world"):
    print("hello,", name)

main()


#endregion

# region return values

def main():
    x = int(input("What's x? "))
    print("x plus 10 is", add_ten(x))


def add_ten(n):
    return n + 10


main()

# endregion