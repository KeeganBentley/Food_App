from foodList import FoodList
from recipe import Recipe
from food import FoodItem


#f1 = FoodItem('Mustard', 200, 'g')
#f2 = FoodItem("BBQ Sauce", 100, 'g')
#print(f1, f2)
#f1 + f2
#print(f1)
r1 = Recipe("Strogonoff", FoodList([FoodItem("beef steak", 500, 'g'), FoodItem("Sour Cream", 300, 'g')]),
            ['frying pan'], ['Brown beef'], 'Russia')
print(r1)
