import os
import sys

def read_recipe_file(file_path):
    recipe = {}
    current_section = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith('Title:'):
                new_recipe = {}
                current_section = 'title'
                new_recipe[current_section] = line.replace('Title:', '').strip()
            elif line.startswith('Ingredients:'):
                current_section = 'ingredients'
                new_recipe[current_section] = line.replace('Ingredients:', '').strip()
            elif line.startswith('Directions:'):
                current_section = 'directions'
                new_recipe[current_section] = line.replace('Directions:', '').strip()
                recipe[new_recipe["title"]] = new_recipe

    return recipe

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python recipe_SOLUTION.py <file_path> <recipe_section>")
        sys.exit(1)

    file_path = sys.argv[1]
    target_section = sys.argv[2]

    recipe = read_recipe_file(file_path)

    if not os.path.exists(file_path):
        print("File not found")
        sys.exit(1)

    if not recipe:
        print("No recipes found")
        sys.exit(1)

    if not target_section:
        print("No recipe section provided")
        sys.exit(1)

    # find the recipe section with the key as target_section
    found_recipe = recipe.get(target_section)

    # print the recipe section
    if found_recipe:
        print(found_recipe)
    else:
        print("Invalid recipe section")
        sys.exit(1)


