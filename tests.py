from foodList import FoodList
from recipe import Recipe
from food import FoodItem


#f1 = FoodItem('Mustard', 200, 'g')
#f2 = FoodItem("BBQ Sauce", 100, 'g')
#print(f1, f2)
#f1 + f2
#print(f1)
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView


Builder.load_string('''
<RV>:
    viewclass: 'Label'
    RecycleBoxLayout:
        default_size: None, dp(56)
        default_size_hint: 1, None
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
''')

class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]


class TestApp(App):
    def build(self):
        return RV()

if __name__ == '__main__':
    TestApp().run()