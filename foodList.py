"""
class to handle lists of food items 
"""
from food import FoodItem
import csv
from operator import attrgetter


class FoodList:
    def __init__(self):
        # rename foods
        self.foods = []

    def __str__(self):
        return str([str(item) for item in self.foods])

    def add_item(self, item):
        """
        :param item: FoodItem object to be added to the list
        :return: None
        """
        self.foods.append(item)

    def use_some(self, item_name, amount_used):
        """
        function to modify a certain item in the list based on some being used. 
        :param item_name: name of the item to be modified
        :param amount_used: amount of the item used. 
        :return: None
        """
        for item in self.foods:
            if item.name == item_name:
                item.amount -= amount_used

    def load_foods(self, file_name):
        """
        Open csv file, real line by line, create an instance of FoodItem for each line then add the items to self.foods
        :param file_name: The path and name of csv file holding books
        """
        with open(file_name, 'r') as input_file:
            input_reader = csv.reader(input_file)
            for row in input_reader:
                # check if the row is a properly formatted csv line, deals with blank lines in the file
                if row:
                    try:
                        self.foods.append(FoodItem(row[0], row[1], row[2]))
                    except IndexError:
                        self.foods.append(FoodItem(row[0], row[1]))

    def save_foods(self, file_name):
        """
        :param file_name: The path and name of csv file intended to record food list
        """
        with open(file_name, 'w') as output_file:
            output_writer = csv.writer(output_file)
            for item in self.foods:
                output_writer.writerow([item.name, item.amount, item.amount_type])

    def sort_books(self):
        """
        Sort foods by name.
        :return: None
        """
        self.foods = sorted(self.foods, key=attrgetter("name"))
