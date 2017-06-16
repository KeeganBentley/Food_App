"""
Class to store a recipe
started: 16/6/17
"""


class Recipe:
    def __init__(self, title, ingredients, equipment, method, country_of_origin='na'):
        self.title = title
        self.ingredients = ingredients
        self.equipment = equipment
        self.method = method
        self.country_of_origin = country_of_origin

    def __str__(self):
        return "{}\nCountry of origin: {}\n{}\n{}\n{}".format(self.title, self.country_of_origin, self.ingredients,
                                                              self.equipment, self.method)
