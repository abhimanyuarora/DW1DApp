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
from kivy.config import Config
from kivy.garden.navigationdrawer import NavigationDrawer
from screen4 import Screen4
from screen5 import Screen5
from screen6 import Screen6
from screen7 import Screen7


class Screen3(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Window.clearcolor=(0.4, 0.8, 1, 1)
        '''Designing of the layout and buttons'''
        self.layout=BoxLayout(orientation='vertical')
        backbuttons=GridLayout(rows=1,cols=2)
        bckbutton = Button(text='<-',font_size=30,size_hint_x=None,size_hint_y=None,width=40, height=50, color=(0,0,0,1))
        backbuttons.add_widget(bckbutton)
        backbuttons.add_widget(Label(text=''))
        bckbutton.bind(on_press=self.menu_screen)
        self.layout.add_widget(backbuttons)
        self.gardenlabel=(Label(text='', font_size=60, color=(0,0,0,1), markup=True))
        self.layout.add_widget(self.gardenlabel)
        self.layout.add_widget(Label(text='Health Status: ', font_size=45, color=(0,0,0,1)))
        self.healthlabel=(Label(text='[b]GOOD[/b]', font_size=60, color=(1,0,0,1), markup=True)) #update with the appropriate status
        self.layout.add_widget(self.healthlabel)
        self.button0=(Button(id='0',text='Results', font_size=35, color=(0,0,0,1)))
        self.button0.bind(on_press=self.screenswitch)
        self.layout.add_widget(self.button0)
        self.button1=(Button(id='1',text='Garden statistics', font_size=35, color=(0,0,0,1)))
        self.button1.bind(on_press=self.screenswitch)
        self.layout.add_widget(self.button1)
        self.button2=(Button(id='2',text='Real life monitoring', font_size=35, color=(0,0,0,1)))
        self.button2.bind(on_press=self.screenswitch)
        self.layout.add_widget(self.button2)
        self.button3=(Button(id='3',text='Leaderboard', font_size=35, color=(0,0,0,1)))
        self.button3.bind(on_press=self.screenswitch)
        self.layout.add_widget(self.button3)
        self.add_widget(self.layout)
        self.current='scr3'
    '''Switcher functions to switch between menu and other screens'''
    def menu_screen(self, instance):
        from kivy.core.window import Window
        Config.set('graphics', 'resizable', False)
        Window.clearcolor=((252/255), (245/255), (237/255), 1)
        Window.size=(650,650)
        self.manager.transition.direction='right'
        self.manager.current='menu'
    def textupdate(self,data):
        self.gardenlabel.text=data
    def screenswitch(self, instance):
        if instance.id=='1':
            self.manager.transition.direction='left'
            self.manager.current='scr5'
            from kivy.core.window import Window
            Window.size=(650,650)
            Window.clearcolor=((252/255), (245/255), (237/255), 1)
        elif instance.id=='2':
            self.manager.transition.direction='left'
            self.manager.current='scr6'
            from kivy.core.window import Window
            Window.size=(650,650)
            Window.clearcolor=((252/255), (245/255), (237/255), 1)
        elif instance.id=='0':
            self.manager.transition.direction='left'
            self.manager.current='scr8'
            from kivy.core.window import Window
            Window.size=(650,650)
            Window.clearcolor=((252/255), (245/255), (237/255), 1)
        elif instance.id=='3':
            self.manager.transition.direction='left'
            self.manager.current='scr4'
            from kivy.core.window import Window
            Window.size=(650,650)
            Window.clearcolor=((252/255), (245/255), (237/255), 1)


# class testapp(App):
#     def build(self):
#         sm=ScreenManager()
#         sm.add_widget(Screen3(name='scr3'))
#         sm.current='scr3'
#         return sm
# myApp=testapp()
# myApp.run()
