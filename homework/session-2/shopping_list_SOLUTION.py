# Recipe ingredients dictionary
recipe_ingredients = {
    "chocolate cake": {
        "flour": {"cups": 2},
        "sugar": {"cups": 2},
        "baking soda": {"teaspoons": 2},
        "salt": {"teaspoons": 0.5},
        "cocoa powder": {"cups": 0.75},
        "vegetable oil": {"cups": 0.5},
        "buttermilk": {"cups": 1},
        "eggs": {"count": 2},
        "vanilla extract": {"teaspoons": 2},
        "hot coffee": {"cups": 1}
    },

    "beer bread": {
        "flour": {"cups": 3},
        "sugar": {"teaspoons": 3},
        "baking powder": {"teaspoons": 3},
        "salt": {"teaspoons": 1},
        "beer": {"cans": 1},
        "butter": {"cups": 0.25}
    },
}


def main():
    # Ask user for recipe name
    while True:
        recipe_name = input("What recipe would you like to make? ")
        if recipe_name in recipe_ingredients:
            break
        else:
            print("Recipe not found.")
    while True:
        servings = input("How many servings? ")
        if servings.isdigit() and int(servings) > 0:
            break
        else:
            print("Please enter a number.")

    if recipe_name in recipe_ingredients:
        print(f"{servings} servings: ingredients for {recipe_name} are:")
        for ingredient, item in recipe_ingredients[recipe_name].items():
                for unit, amount in item.items():
                    print(f"{ingredient}: {amount * float(servings)} {unit}")
    else:
        print("Recipe not found.")

main()
