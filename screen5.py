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
class Screen5(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Window.clearcolor=(1, 1, 1, 1)
        self.layout=GridLayout(cols=2, spacing=(30,0))
        self.layout.add_widget(Label(text='[u]Soil Moisture: [/u]', font_size=30, color=(0,0,0,1), markup=True))
        percentage=(Label(text='percentage%', font_size=40, color=(0,0,0,1)))
        self.layout.add_widget(percentage)
        self.layout.add_widget(Label(text='[u]pH[/u]', font_size=30, color=(0,0,0,1), markup=True))
        pH=(Label(text='')) #add pH graph here
        self.layout.add_widget(pH)
        self.layout.add_widget(Label(text='[u]Temperature[/u]', font_size=30, color=(0,0,0,1), markup=True))
        temp=(Label(text='')) #add temp graph here
        self.layout.add_widget(temp)
        self.layout.add_widget(Label(text='[u]Humidity: [/u]', font_size=30, color=(0,0,0,1), markup=True))
        humidity=(Label(text='')) #add humidity graph here
        self.layout.add_widget(humidity)
        self.layout.add_widget(Label(text='[u]Fluroscence[/u]', font_size=30, color=(0,0,0,1), markup=True))
        fluorescence=(Label(text='')) #add Fluroscence graph here
        self.layout.add_widget(fluorescence)
        self.add_widget(self.layout)
        self.current='scr5'
class testapp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Screen5(name='scr5'))
        return sm
testapp().run()
