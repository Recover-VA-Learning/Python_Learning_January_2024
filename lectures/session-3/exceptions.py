# Errors
# 1. Syntax Error
# print("Hello World)

# 2. ValueError
# print(int("Hello World"))

# 3. Can use try-except block to handle errors
try:
    x = int(input("Enter a number: "))
except:
    # except if anything goes wrong. Not recommended
    print("Will not crash the program and will print this message instead")
print(f"x = {x}")

# 4. Can use specific except block
try:
     x = int(input("Enter a number: "))
except ValueError:
    print("Invalid Input")
print(f"x = {x}")

# 5. Can use multiple except blocks
try:
    print(int(input("Enter a number: ")) / 0)
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Zero Division Error")

# 6. Can use else block
try:
    print(int(input("Enter a number: ")))
except ValueError:
    print("Invalid Input")
else: # only runs if no error
    print("No Error")


# 7. Create a function to handle errors
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Zero Division Error")
    else:
        print(f"Result = {result}")

#8. User Input
def get_user_input():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("Invalid Input")
        else:
            break
    return x

# 9. Can tighten the code
def get_user_input():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Invalid Input") # can use pass here
