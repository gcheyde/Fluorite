import kivy
kivy.require('2.2.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class SliderWidget(BoxLayout):
    pass


class Slider(App):

    def build(self):
        return SliderWidget()


if __name__ == '__main__':
    Slider().run()