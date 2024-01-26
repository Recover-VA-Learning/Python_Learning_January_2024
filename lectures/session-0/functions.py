def main():
    name = input("What's your name? ")
    result = hello(name)
    print(result)
    # number = add_ten(5)
    # print(number)

def hello(name="world"):
    return "Hello " + name + "!"

def add_ten(n):
    return n + 10

main()