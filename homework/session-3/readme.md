## Homework for session 3

Challenge 1: Percentage Exceptions- Create a program that will ask the user for a fraction and then print out the percentage of the fraction. Make sure to handle any exceptions that may occur. For example, if the user enters a string instead of a number, or if the user enters 0 as the denominator.
Hint: Use try/except blocks to handle the exceptions.
Hint: ZeroDivisionError, ValueErrors
Hint: Use the sting method split() to separate the numerator and denominator.

Example
```
Enter a fraction (a/b): 1/2
50.0%
```


Challenge 2: Recipe from file- Create a program that will read a recipe from a file and print it out to the user. Make sure to handle any exceptions that may occur. For example, if the file does not exist, or if the file is empty.
Hint: Use OS to open and read the file.
Hint: Use try/except blocks to handle the exceptions.
Hint: FileNotFoundError, IOError

Example
```
Recipe for Beer Bread
Ingredients:
- 3 cups flour
- 3 teaspoons baking powder
- 1 teaspoon salt
- 1/4 cup sugar
- 1 (12 ounce) can beer

Directions:
1. Preheat oven to 375 degrees F (190 degrees C). Lightly grease a 9x5 inch baking pan.
2. In a large mixing bowl, combine flour, baking powder, salt and sugar. Gradually add the beer and continue to mix. Pour into prepared pan.
3. Bake for 45 to 55 minutes.
```
Extra Credit: Have multiple recipes in the file and allow the user to choose which recipe to print out.


Challenge 3: Use Python Statistics- Create a program that will read a list of numbers from a file and print out the mean, median, and mode of the numbers. Make sure to handle any exceptions that may occur. For example, if the file does not exist, or if the file is empty.
Hint: Use OS to open and read the file.
Hint: Use try/except blocks to handle the exceptions.
Hint: FileNotFoundError, IOError
Hint: Use the statistics module to calculate the mean, median, and mode.

Example
```
Numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Mean: 5.5
Median: 5.5
Mode: No mode
```

Extra Credit: Use Commnad Line Arguments- Use the sys module to allow the user to pass the file name as a command line argument. For example, the user would run the program like this: 
'''
python3 my_program.py numbers.txt mean
'''
Where numbers.txt is the file that contains the list of numbers and mean is the command line argument that the user wants to run.




