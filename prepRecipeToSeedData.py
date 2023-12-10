def transform_recipe_line(line):
    # Splitting the string and stripping extra characters
    parts = line.strip().strip('[]').split('",')
    parts = [p.strip().strip('"') for p in parts]

    # Extracting the recipe name (last element) and the ingredients (all elements before '=')
    recipe_name = parts[-1]
    ingredients = [p for p in parts[:-1] if p != "+" and p != "="]

    # Creating the combination string
    combination = " + ".join(ingredients)
    return recipe_name, combination

def process_recipes(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        recipe_id = 1
        for line in infile:
            name, combination = transform_recipe_line(line)
            recipe_str = f"new Recipe\n{{\n    RecipeId = {recipe_id},\n    Name = \"{name}\",\n    Combination = new[] {{{combination}}}\n}},\n"
            outfile.write(recipe_str)
            recipe_id += 1

# File names
input_file = 'scrapedRecipe.txt'  # Input file name
output_file = 'prepRecipeDataToSeed.txt'  # Output file name

# Process the recipes
process_recipes(input_file, output_file)
