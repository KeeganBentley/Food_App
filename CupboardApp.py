"""
App to store the contents of your cupboard. 
Keegan Bentley - started 23/6/17 half baked
"""

from kivy.app import App
from food import FoodItem
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty


class CupboardListApp(App):

    def __init__(self, **kwargs):
        """
        Initialise an instance of the app.
        """
        super(CupboardListApp, self).__init__(**kwargs)
