import random


# Class for a single Recipe object:
class Recipe:
    def __init__(
        self,
        name: str,
        ingredients=[],
        instructions=[],
        preparation_time=0,
        country="",
        rating=0.0,
    ):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.preparation_time = preparation_time
        self.country = country
        self.rating = rating

    # Method for printing the recipe details in full:
    def print_recipe(self):
        print(f"==== {self.name} ====")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Preparation Time: {self.preparation_time} mins")
        print(f"Country: {self.country}")
        print(f"Rating: {self.rating}/5")
        instructions_str = "\n".join(self.instructions)
        print(f"Instructions: {instructions_str}")

    # Method for printing a summary of the recipe:
    def print_summary(self):
        print(f"== {self.name} ==")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Preparation Time: {self.preparation_time} mins")
        print(f"Country: {self.country}")
        print(f"Rating: {self.rating}/5")


# Class that holds a list of recipes and provides methods for finding and accessing them:
class RecipesDatabase:
    def __init__(self):
        self.recipes = []

    # Method for adding a recipe to the database:
    def add_recipe(self, recipe: Recipe):
        self.recipes.append(recipe)

    # Method for removing a recipe from the database:
    def remove_recipe(self, recipe: Recipe):
        self.recipes.remove(recipe)

    # Method for printing the summary of all recipes in the database:
    def print_all_recipes(self):
        for recipe in self.recipes:
            recipe.print_summary()
            print("\n---------------------------------------\n")

    # Method for finding all recipes that contain a name:
    def find_recipes_by_name(self, name: str):
        found_recipes = []
        for recipe in self.recipes:
            # Check if the recipe contains the name provided:
            if name.lower() in recipe.name.lower():
                found_recipes.append(recipe)  # Add to the list of found recipes
        return found_recipes

    # Method for finding all recipes that contain a list of ingredients:
    def find_recipes_by_ingredients(self, ingredients: list):
        found_recipes = []
        for recipe in self.recipes:
            # Flag to check if recipe has all ingredients provided:
            has_all_ingredients = True
            for ingredient in ingredients:
                # Check if the recipe is missing one of the ingredients:
                if ingredient.lower().strip() not in recipe.ingredients:
                    # Set the flag to false
                    has_all_ingredients = False
            # Only add ingredients that have all ingredients:
            if has_all_ingredients:
                found_recipes.append(recipe)
        return found_recipes

    # Method for filtering recipes by a specific country:
    def filter_recipes_by_country(self, country: str):
        filtered_recipes = []
        for recipe in self.recipes:
            # Check if the country matches:
            if recipe.country.lower() == country.lower():
                filtered_recipes.append(recipe)
        return filtered_recipes

    # Method for displaying the top-rated recipes:
    def display_top_rated_recipes(self, n=5):
        # Sort based on the rating in descending order, and slice the top n elements:
        sorted_recipes = sorted(
            self.recipes, key=lambda recipe: recipe.rating, reverse=True
        )[0:n]
        return sorted_recipes

    # Method for displaying recipes with prep time less than a certain value:
    def display_quick_recipes(self, max_preparation_time: int):
        quick_recipes = []
        for recipe in self.recipes:
            # Check if the recipe prep time is less than the max prep time:
            if recipe.preparation_time <= max_preparation_time:
                quick_recipes.append(recipe)
        return quick_recipes

    # Method for returning a random recipe:
    def random_recipe_suggestion(self):
        # Generate a random index in the range of the recipes list:
        random_index = random.randint(0, len(self.recipes) - 1)
        return self.recipes[random_index]
