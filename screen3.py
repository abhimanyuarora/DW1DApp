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
from kivy.uix.image import Image
from kivy.garden.navigationdrawer import NavigationDrawer

class Screen3(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Window.clearcolor=(0.4, 0.8, 1, 1)
        self.layout=BoxLayout(orientation='vertical')
        backbuttons=GridLayout(rows=1,cols=2)
        backbuttons.add_widget(Button(text='<',font_size=30,size_hint_x=None,width=40))
        backbuttons.add_widget(Label(text=''))
        self.layout.add_widget(backbuttons)
        self.gardenlabel=(Label(text='[u][b]Garden name here[/b][/u]', font_size=60, color=(0,0,0,1), markup=True))
        self.layout.add_widget(self.gardenlabel)
        self.layout.add_widget(Label(text='Health Status: ', font_size=45, color=(0,0,0,1)))
        self.healthlabel=(Label(text='[b]GOOD[/b]', font_size=60, color=(1,0,0,1), markup=True)) #update with the appropriate status
        self.layout.add_widget(self.healthlabel)
        self.button1=(Button(text='Garden statistics', font_size=35, color=(0,0,0,1)))
        # #button1.bind(on_press=screen5)
        self.layout.add_widget(self.button1)
        self.button2=(Button(text='Real life monitoring', font_size=35, color=(0,0,0,1)))
        #button2.bind(on_press=screen6)
        self.layout.add_widget(self.button2)
        self.button3=(Button(text='Leaderboard', font_size=35, color=(0,0,0,1)))
        #button1.bind(on_press=screen4)
        self.layout.add_widget(self.button3)
        self.add_widget(self.layout)
        self.current='scr3'
class testapp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Screen3(name='scr3'))
        sm.current='scr3'
        return sm
myApp=testapp()
myApp.run()
