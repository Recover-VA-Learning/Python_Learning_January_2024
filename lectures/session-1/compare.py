# region if

x = input('What is x? ')
y = input('What is y? ')

if x > y:
    print(f'x > y')
if x < y:
    print(f'x < y')
if x == y:
    print(f'x == y')

# endregion
    
# region elif
    
x = input('What is x? ')
y = input('What is y? ')

if x > y:
    print(f'x > y')
elif x < y:
    print(f'x < y')
elif x == y:
    print(f'x == y')

# endregion

# region else

x = input('What is x? ')
y = input('What is y? ')

if x > y:
    print(f'x > y')
elif x < y:
    print(f'x < y')
else:
    print(f'x == y')

# endregion
    
# region or
    
x = input('What is x? ')
y = input('What is y? ')

if x > y or x < y: # either one compares to true will execute
    # could alse be x =! y
    print(f'x and y are not equal')
else:
    print(f'x == y')

# endregion
    
# region and
    
grade = int(input('What is your grade? '))
if grade >= 90:
    print('A')
elif grade >= 80 and grade < 90:
    print('B')
elif grade >= 70 and grade < 80:
    print('C')
elif grade >= 60 and grade < 70:
    print('D')
else:
    print('F')

# can also be written as
if grade >= 90:
    print('A')
elif 80 <= grade < 90:
    print('B')
elif 70 <= grade < 80:
    print('C')
elif 60 <= grade < 70:
    print('D')
else:
    print('F')

# can even be simplified more
if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
else:
    print('F')

# endregion
    
# region modulo

# check in input is even or odd
num = int(input('What is your number? '))
if num % 2 == 0:
    print('even')
else:
    print('odd')

# endregion
    
# region def is_even
    
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
# endregion
