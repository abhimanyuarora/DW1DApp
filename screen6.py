from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics.instructions import Canvas, InstructionGroup
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp,sp
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image

class Screen6(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Window.clearcolor=(1, 1, 1, 1)
        self.layout=BoxLayout(orientation='vertical')
        self.layout.add_widget(Label(text='[u]Camera[/u]', font_size=50, color=(0,0,0,1), markup=True))
        #add camera here
        self.add_widget(self.layout)
        self.current='scr6'
class testapp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Screen6(name='scr6'))
        return sm
testapp().run()
