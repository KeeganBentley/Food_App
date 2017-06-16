"""
class to handle lists of food items 
"""


class FoodList:
    def __init__(self, foods):
        # rename foods
        self.foods = foods

    def __str__(self):
        return str([str(item) for item in self.foods])

