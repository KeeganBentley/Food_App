"""
General class for all food items 

"""


class FoodItem:
    def __init__(self, name, amount, amount_type='na'):
        self.name = name
        self.amount_type = amount_type
        self.amount = amount

    def __str__(self):
        return "{}, weight: {}{}".format(self.name, self.amount, self.amount_type)

    def __add__(self, other):
        """
        need control for different units of measure 
        :param other: 
        :return: none
        """
        self.amount += other.amount

    def use_some(self, amount_used):
        """
        Update item amount when it has been used for something
        eg, Cook a meal, all ingredients have 'some used' xD
        :param amount_used: amount of the item used up
        :return: none
        """
        self.amount -= amount_used
