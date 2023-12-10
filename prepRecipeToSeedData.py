# Input File: The script will read from a file named scrapeRecipe.txt. This file contains arrays of ingredients and a resulting product, formatted as strings.

# Data Format: Each array in the file represents a recipe. The elements of the array are ingredients, denoted by strings. The '+' sign is used to separate ingredients, and the '=' sign precedes the name of the final product.

# Transformation:

# The script will convert each array into a structured format.
# The '+' signs will be retained to concatenate the ingredients.
# The '=' sign will be omitted.
# The last element in the array (after the '=') is considered the name of the recipe.
# Each transformed recipe will be encapsulated in a new Recipe structure with three attributes: RecipeId, Name, and Combination.
# RecipeId will be a sequential integer starting from 1 and incrementing for each recipe.
# Name will be the final product's name (the last element in the array).
# Combination will be a string composed of the ingredients concatenated with '+' signs.
# Output Format: The transformed data will be outputted in the specified structure. This should be save to a file name : prepRecipeToSeed.txt






# NOT WORKING PROPERLY






def transform_recipe(file_path, output_path):
    with open(file_path, 'r') as file:
        # Read the entire file content
        file_content = file.read()

    # Split the content by double newlines to separate each recipe
    raw_recipes = file_content.split('\n\n')

    transformed_recipes = []
    recipe_id = 1

    for raw_recipe in raw_recipes:
        # Split by newline and remove empty lines
        recipe_lines = [line.strip() for line in raw_recipe.split('\n') if line.strip()]

        # Initialize an empty list to hold ingredients
        ingredients = []

        for line in recipe_lines:
            if line in ['+', '=']:
                ingredients.append(line)
            else:
                # Handle special characters and ensure correct string formatting
                cleaned_line = line.replace('®', '').replace('"', '\\"')
                ingredients.append(f'"{cleaned_line}"')

        # Skip malformed recipes
        if len(ingredients) < 3 or '=' not in ingredients:
            print(f"Skipping malformed recipe: {ingredients}")
            continue

        # Extract the name of the recipe (last element after '=')
        name_index = ingredients.index('=') + 1
        name = ingredients[name_index]

        # Join all ingredients (except last two elements, '=' and the name) with '+'
        combination = ' + '.join(ingredients[:name_index - 1])

        # Create the transformed recipe string
        transformed_recipe = f"""new Recipe
{{
    RecipeId = {recipe_id},
    Name = {name},
    Combination = new[] {{"{combination}"}}
}},"""

        transformed_recipes.append(transformed_recipe)
        recipe_id += 1

    # Save the transformed recipes to the output file
    with open(output_path, 'w') as output_file:
        output_file.write('\n'.join(transformed_recipes))

    print(f"Recipes transformed and saved to {output_path}")

# Execute the transformation
transform_recipe('scrapedRecipe.txt', 'prepRecipeToSeed.txt')
