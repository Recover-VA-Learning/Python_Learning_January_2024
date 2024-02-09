def main():
    x = get_user_input()
    print(f"x = {x * 100}%")

def get_user_input():
    while True:
        try:
            input_string = input("Enter a fraction (a/b): ")
            decimal = parse_fraction_string(input_string)
            if decimal:
                return decimal
        except ValueError:
            print("Invalid Input")
    # return x

def parse_fraction_string(input_string):
    if ('/') in input_string:
        split_numbers = input_string.split('/')
        # make sure only 2 numbers
        if len(split_numbers) == 2:
            numerator = split_numbers[0]
            denominator = split_numbers[1]
            try:
                decimal = float(numerator) / float(denominator)
                if numerator > denominator:
                    print("Numerator must be less than denominator")
                    return
                return decimal
            except ValueError:
                print("Invalid Input")
            except ZeroDivisionError:
                print("divide by zero error")


main()