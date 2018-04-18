from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.metrics import dp,sp
from kivy.config import Config

KIVY_DPI=240
KIVY_METRICS_DENSITY=2
class Menu(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Config.set('graphics', 'resizable', False)
        Window.clearcolor=(0.4, 0.8, 1, 1)
        Window.size=(500,500)
        '''navigationdrawer KIV'''
        # self.navigationdrawer = NavigationDrawer()
        # self.side_panel = BoxLayout(orientation='vertical')
        # self.side_panel.add_widget(Button(text='Settings'))
        # bl1=Button(text='A button')
        # self.side_panel.add_widget(Button(text='Logout'))
        # self.navigationdrawer.set_anim_type='slide_above_anim'
        # self.navigationdrawer.toggle_state()
        # self.navigationdrawer.add_widget(self.side_panel)
        # self.add_widget(self.navigationdrawer)
        self.layout = GridLayout(cols=2, spacing=(10))
        self.empty=(Button(text='[b]< Gardens[/b]', color=(0,0,0,1), font_size=40, markup=True)) #bind to login screen
        self.layout.add_widget(self.empty)
        self.vote=(Label(text='[b]Voting[/b]', color=(0,0,0,1), font_size=40, markup=True))
        self.layout.add_widget(self.vote)
        self.garden1=(Button(text='', color=(0,0,0,1), font_size=30, background_normal='1st_garden.jpg'))
        self.layout.add_widget(self.garden1)
        self.vote1=Button(text='')
        self.layout.add_widget(self.vote1)
        self.garden2=(Button(text='', color=(0,0,0,1), font_size=30, background_normal='2nd_garden.jpg'))
        self.layout.add_widget(self.garden2)
        self.vote2=Button(text='',width=30, background_color=(0.3,1,0,1))
        self.layout.add_widget(self.vote2)
        self.garden3=Button(text='', color=(0,0,0,1), font_size=30, background_normal='3rd_garden.jpg')
        self.layout.add_widget(self.garden3)
        self.vote3=Button(text='',width=30)
        self.layout.add_widget(self.vote3)
        self.add_widget(self.layout)
        # self.navigationdrawer.add_widget(self.layout)


        # self.main_panel = BoxLayout(orientation='vertical')
        # label_bl = BoxLayout(orientation='horizontal')
        # label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
        # # label_bl.add_widget(label)
        # label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
        # self.main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
        # self.main_panel.add_widget(label_bl)
        # self.main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
        # navigationdrawer.add_widget(main_panel)
        self.current='menu'
        # label.bind(size=label.setter('text_size'))

class Switcher(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.current='menu'
        return sm


def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window=window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat]={}
reset()
myapp=Switcher()
myapp.run()
