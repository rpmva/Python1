from classes.ingredients import Ingredient
from classes.recipes import Recipe

def main():
    i = Ingredient(title="eggs")

    r = Recipe(title="Scrambled eggs", ingredients = [i], directtions = ['Break egg', 'Beat egg', 'Cook egg'])

    r.print_recipe()

if __name__ == "__main__":
    main()
