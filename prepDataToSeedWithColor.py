import json
import webcolors

def hex_to_rgb(hex_code):
    # Provide a default RGB value in case of invalid hex_code
    default_rgb = (0, 0, 0)  # Default to black
    if not hex_code or len(hex_code) != 6:
        return default_rgb

    try:
        return tuple(int(hex_code[i:i+2], 16) for i in (0, 2, 4))
    except ValueError:
        return default_rgb

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_color_name(hex_color):
    try:
        # Directly find the name, if possible
        return webcolors.hex_to_name(hex_color)
    except ValueError:
        # Calculate closest color name if exact name is not found
        rgb_color = hex_to_rgb(hex_color)
        return closest_color(rgb_color)

def prepDataToSeedWithColor(input_file, output_file, colors_output_file):
    # Read data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)

    assigned_colors = set()  # To keep track of all assigned colors

    # Function to transform each bean object
    def transform_bean(bean):
        background_color = bean.get('BackgroundColor', '').lstrip('#')
        color_group = get_color_name(background_color)
        assigned_colors.add(color_group)  # Add the color to the set
        return (
            "new Bean\n{\n"
            f"\tBeanId = {bean.get('BeanId', '')},\n"
            f"\tGroupNameSerialized = \"{bean.get('GroupName', '')}\",\n"
            f"\tFlavorName = \"{bean.get('FlavorName', '')}\",\n"
            f"\tDescription = \"{bean.get('Description', '')}\",\n"
            f"\tIngredients = new [] {{\"{bean.get('Ingredients', '')}\"}},\n"
            f"\tColorGroup = \"{color_group}\",\n"
            f"\tBackgroundColor = \"#{background_color}\",\n"
            f"\tImageUrl = \"{bean.get('ImageUrl', '')}\",\n"
            f"\tGlutenFree = {str(bean.get('GlutenFree', False)).lower()},\n"
            f"\tSugarFree = {str(bean.get('SugarFree', False)).lower()},\n"
            f"\tSeasonal = {str(bean.get('Seasonal', False)).lower()},\n"
            f"\tKosher = {str(bean.get('Kosher', False)).lower()}\n"
            "},\n\n"
        )

    # Transform each bean in the data
    transformed_data = [transform_bean(bean) for bean in data]

    # Write the transformed data to the output file
    with open(output_file, 'w') as file:
        for bean in transformed_data:
            file.write(f"{bean}")

    # Write the list of colors to the colors output file
    with open(colors_output_file, 'w') as file:
        for color in sorted(assigned_colors):
            file.write(f"{color}\n")

# Call the function with the appropriate file names
prepDataToSeedWithColor('toCapitalize.json', 'seeded_beans_with_color_name.txt', 'list_of_colors.txt')
