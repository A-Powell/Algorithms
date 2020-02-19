#!/usr/bin/python

import math

# Takes recipe and ingredients on hand in form of dictionary
# The keys will be the ingredient names, with their associated values being the amounts.
# should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you

# ```python
# should return 0 since we don't have enough butter!
# recipe_batches(
# { 'milk': 100, 'butter': 50, 'flour': 5 },
# { 'milk': 138, 'butter': 48, 'flour': 51 }
# )
# ```


def recipe_batches(recipe, ingredients):

    max_batches = 0

    for ingredient in recipe.keys():
        if ingredient not in ingredients:
            return 0
        batches = ingredients[ingredient]//recipe[ingredient]
        if batches <= 0:
            return 0
        elif max_batches == 0 or batches < max_batches:
            max_batches = batches

    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 532, 'butter': 500, 'flour': 551}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
