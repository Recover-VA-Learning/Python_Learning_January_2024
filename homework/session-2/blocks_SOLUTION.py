
def main():
    # Prompt the user for the height of the pyramid
    height = int(input("Enter the height of the pyramid: "))

    # Validate the user input
    while height <= 0:
        print("Invalid input. Height must be a positive integer.")
        height = int(input("Enter the height of the pyramid: "))

    # Create the pyramid
    for i in range(1, height + 1):
        print(" " * (height - i) + "#" * (2 * i - 1))

main()
