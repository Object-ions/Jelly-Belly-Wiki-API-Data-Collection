def process_recipes(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    recipes = []
    recipe_id = 1

    for line in lines:
        # Remove square brackets and split by '=' to separate ingredients and recipe name
        ingredients, recipe_name = line.strip('[]\n').split(' = ')

        # Create the recipe structure
        recipe = {
            'RecipeId': recipe_id,
            'Name': recipe_name.strip(),
            'Combination': [ingredients.strip()]
        }

        recipes.append(recipe)
        recipe_id += 1

    return recipes

def format_recipes(recipes):
    for recipe in recipes:
        print(f'new Recipe\n{{\n    RecipeId = {recipe["RecipeId"]},')
        print(f'    Name = "{recipe["Name"]}",')
        print(f'    Combination =  new[] {recipe["Combination"]}\n}},\n')

# Usage
filename = 'RecipeReadyToSeed.txt'
recipes = process_recipes(filename)
format_recipes(recipes)