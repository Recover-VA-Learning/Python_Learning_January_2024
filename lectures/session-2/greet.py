def main():
    greet_loop(get_number_from_user())


def get_number_from_user():
    while True:
        n = int(input("How many times to greet? "))
        if n > 1:
            return n


def greet_loop(n):
    for _ in range(n):
        print("hi")


main()