import json
from recipe import Recipe, RecipesDatabase


# Method for getting user input:
def get_user_input():
    print("1. Display all recipes")
    print("2. Find recipes by name")
    print("3. Find recipes by ingredients")
    print("4. Filter recipes by country")
    print("5. Display top-rated recipes")
    print("6. Display quick recipes")
    print("7. Random recipe suggestion")
    print("0. Exit\n")
    user_input = input("Enter your selection: ")

    # Check if the input is a valid number:
    try:
        # Try converting the input to an integer
        user_input = int(user_input)
    except ValueError:
        # If there is an error, print a warning and try again:
        print("Invalid input. Please enter a number.")
        return get_user_input()

    return user_input


# Method for printing all recipes in the provided list:
def print_recipes(recipes):
    print("\n")
    if len(recipes) == 0:
        print("No recipes found.\n")
    else:
        for recipe in recipes:
            recipe.print_recipe()
            print("---------------------------------------\n")


recipes_data = None

# Load the recipes JSON file into a dictionary:
with open("data/recipes.json", "r") as file:
    recipes_data = json.load(file)

# Create an instance of the RecipesDatabase class and add each recipe to it:
recipes_database = RecipesDatabase()
for recipe_data in recipes_data["recipes"]:
    recipe = Recipe(
        recipe_data["name"],
        recipe_data["ingredients"],
        recipe_data["instructions"],
        recipe_data["preparation_time"],
        recipe_data["country"],
        recipe_data["rating"],
    )
    recipes_database.add_recipe(recipe)

# Main Program:
print("=====================================")
print("Welcome to the Recipe App!")
print("=====================================\n")

user_input = get_user_input()

# Check which option the user has selected and call the corresponding method:
while user_input != 0:
    if user_input == 1:
        # Display all recipes
        recipes_database.print_all_recipes()
    elif user_input == 2:
        # Find recipes by name
        recipe_name = input("Enter the recipe name: ")
        found_recipes = recipes_database.find_recipes_by_name(recipe_name)
        print_recipes(found_recipes)
    elif user_input == 3:
        # Find recipes by ingredients
        ingredients = input("Enter the list of ingredients (comma-separated): ")
        ingredients = ingredients.split(",")  # Split the input into a list
        found_recipes = recipes_database.find_recipes_by_ingredients(ingredients)
        print_recipes(found_recipes)
    elif user_input == 4:
        # Filter recipes by country
        country = input("Enter the country: ")
        found_recipes = recipes_database.filter_recipes_by_country(country)
        print_recipes(found_recipes)
    elif user_input == 5:
        # Display top-rated recipes
        top_rated_recipes = recipes_database.display_top_rated_recipes(5)
        print_recipes(top_rated_recipes)
    elif user_input == 6:
        # Display quick recipes
        quick_recipes = recipes_database.display_quick_recipes(20)
        print_recipes(quick_recipes)
    elif user_input == 7:
        # Random recipe suggestion
        random_recipe = recipes_database.random_recipe_suggestion()
        random_recipe.print_recipe()
    else:
        print("Invalid input. Please enter a number between 0 and 8.")

    print("")
    user_input = get_user_input()

print("\nGoodbye!")
