def main():
    x = get_user_input()
    print(f"x = {x}")

def get_user_input():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
            print("Invalid Input")
        else:
            break
    return x

main()