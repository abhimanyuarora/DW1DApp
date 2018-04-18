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
from kivy.uix.slider import Slider

class Screen8(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Window.clearcolor=(1, 0.5, 1, 1)
        self.layout=BoxLayout(orientation='vertical')
        menubar=GridLayout(cols=2)
        menubtn=Button(text='<-', font_size=20, color=(0,0,0,1), size_hint_x=None, size_hint_y=None, width=30, height=70)
        menubtn.bind(on_press=self.back_to_menu)
        menubar.add_widget(menubtn)
        menubar.add_widget(Label(text='[b]Results[/b]', font_size=50, color=(97/255,127/255,62/255,1), markup=True))
        self.layout.add_widget(menubar)
        results=GridLayout(cols=2)
        results.add_widget(Label(text='[b][u]Results: [/u][/b]', font_size=50, color=(1,0,0,0), markup=True)) #include pictures in the other cells
        self.layout.add_widget(results)
        water=GridLayout(cols=2)
        water.add_widget(Image(source='waterdrop.png'))
        water.add_widget(Label(text='[u]'+'1000'+'[/u]', font_size=30, color=(0,0,0,1), markup=True)) #update from data
        self.layout.add_widget(water)
        nutrients=GridLayout(cols=2)
        nutrients.add_widget(Image(source='canteen.png'))
        nutrients.add_widget(Label(text='[u]'+'1000'+'[/u]', font_size=30, color=(0,0,0,1), markup=True))
        self.layout.add_widget(nutrients)
        sunlight=GridLayout(cols=2)
        sunlight.add_widget(Image(source='sunlight.png'))
        sunlight.add_widget(Label(text='[u]'+'1000'+'[/u]', font_size=30, color=(0,0,0,1), markup=True))
        self.layout.add_widget(sunlight)
        self.add_widget(self.layout)
        self.current='scr8'
    def back_to_menu(self, instance):
        self.manager.transition.direction='right'
        self.manager.current='scr3'
        from kivy.core.window import Window
        Window.clearcolor=((252/255), (245/255), (237/255), 1)
        Window.size=(650,650)
# class testapp(App):
#     def build(self):
#         sm=ScreenManager()
#         sm.add_widget(Screen8(name='scr8'))
#         return sm
# testapp().run()
