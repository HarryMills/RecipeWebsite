import json
import random


def create_data(number):
    output = []

    # loop through the number of times supplied to the function
    for i in range(number):
        data = generate_recipe(i)
        output.append(data)

    return output


def generate_recipe(id_val):
    recipe = Recipe(id_val, random_value(recipeNames))
    recipe.image = random_value(images)
    recipe.author = Author(id_val, random_value(authorFirstNames), random_value(authorLastNames))
    recipe.datePublished = random_value(dates)
    recipe.description = random_value(descriptions)
    recipe.prepTime = random_value(times)
    recipe.cookTime = random_value(times)
    recipe.totalTime = random_value(times)
    for x in range(0, 3):
        recipe.keywords.append(random_value(keywords))
    recipe.recipeYield = random.randint(0, 100)
    recipe.recipeCategory = random_value(categories)
    recipe.recipeCuisine = random_value(cuisines)
    for y in range(0, 10):
        recipe.recipeIngredient.append(Ingredient(random_value(ingredients), random_value(ingredientsQuantities)))
    for z in range(0, 10):
        recipe.recipeInstructions.append(Instruction("Step " + str(z), random_value(instructionTexts), random_value(images)))
    recipe.rating = random.randint(0, 5)
    return recipe


def random_value(array):
    return array[random.randint(0, len(array)-1)]


class Recipe:
    id = None
    name = None
    image = None
    author = None
    datePublished = None
    description = None
    prepTime = None
    cookTime = None
    totalTime = None
    keywords = []
    recipeYield = None
    recipeCategory = None
    recipeCuisine = None
    recipeIngredient = []
    recipeInstructions = []
    rating = None

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Author:
    id = None
    firstName = None
    lastName = None

    def __init__(self, id, firstName, lastName):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName


class Ingredient:
    name = None
    quantity = None

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class Instruction:
    name = None
    text = None
    image = None

    def __init__(self, name, text, image):
        self.name = name
        self.text = text
        self.image = image


recipeNames = ["Brownies", "Cake", "Pizza", "Chicken Kiev", "Lasagna", "Cookies", "Greek Wraps", "Pesto Pasta", "Bread", "Gingerbread Men", "Fig Rolls", "Chicken Nuggets"]
images = ["https://i.imgur.com/1CQMUXz.jpg", "https://i.imgur.com/WyXF3TO.jpg", "https://i.imgur.com/nqCuRCy.jpg", "https://i.imgur.com/6yHQDkp.jpg", "https://i.imgur.com/RTGa3g6.jpg", "https://i.imgur.com/Z0iD1Ad.jpg", "https://i.imgur.com/iH2QOvd.jpg"]
authorFirstNames = ["Harry", "Emma", "Joe", "Mark", "David", "Molly"]
authorLastNames = ["Mills", "Hemus", "Coombs", "Stokes", "Snowden", "Matthews"]
dates = ["25.12.2021"]
descriptions = ["testing description", "testing 2"]
times = ["10 Mins", "100 Hours", "30 Mins", "1 Hour", "5 Mins", "3 Hours"]
keywords = ["Easy", "Simple", "Complex", "Tasty"]
categories = ["Home", "Baking", "Posh", "One-Pot"]
cuisines = ["Mexican", "Chinese", "Home-Style", "American", "English", "Asian", "French"]
ingredients = ["Milk", "Chocolate", "Cheese", "Coriander", "Sugar", "Tomatoes", "Pasta", "Chicken", "Beef", "Cumin"]
ingredientsQuantities = ["1 tbsp", "500ml", "60g", "10kg"]
instructionTexts = ["test 1", "test 2", "test 3"]

val = create_data(10)
print(val)
