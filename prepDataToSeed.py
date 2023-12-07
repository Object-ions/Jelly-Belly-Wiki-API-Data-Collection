import json

def prepDataToSeed(input_file, output_file):
    # Read data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Function to safely get a value from a bean object, providing a default if the key is missing
    def get_value(bean, key, default=""):
        return bean.get(key, default)

    # Function to transform each bean object
    def transform_bean(bean):
        return (
            "new Bean\n{\n"
            f"\tBeanId = {get_value(bean, 'BeanId')},\n"
            f"\tGroupNameSerialized = \"{get_value(bean, 'GroupName')}\",\n"
            f"\tFlavorName = \"{get_value(bean, 'FlavorName')}\",\n"
            f"\tDescription = \"{get_value(bean, 'Description')}\",\n"
            f"\tIngredients = new [] {{\"{get_value(bean, 'Ingredients')}\"}},\n"
            f"\tColorGroup = \"White\",\n"
            f"\tBackgroundColor = \"#{get_value(bean, 'BackgroundColor')}\",\n"
            f"\tImageUrl = \"{get_value(bean, 'ImageUrl')}\",\n"
            f"\tGlutenFree = {str(get_value(bean, 'GlutenFree', False)).lower()},\n"
            f"\tSugarFree = {str(get_value(bean, 'SugarFree', False)).lower()},\n"
            f"\tSeasonal = {str(get_value(bean, 'Seasonal', False)).lower()},\n"
            f"\tKosher = {str(get_value(bean, 'Kosher', False)).lower()}\n"
            "},\n\n"
        )

    # Transform each bean in the data
    transformed_data = [transform_bean(bean) for bean in data]

    # Write the transformed data to the output file
    with open(output_file, 'w') as file:
        for bean in transformed_data:
            file.write(f"{bean}")

# Call the function with the appropriate file names
prepDataToSeed('toCapitalize.json', 'seeded_beans.txt')
