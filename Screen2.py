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
# from screen3 import Screen3
# from login import Login
# from screen4 import Screen4
# from screen5 import Screen5
# from screen6 import Screen6
# from screen7 import Screen7


KIVY_DPI=240
KIVY_METRICS_DENSITY=2
class Menu(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
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
        self.empty=(Button(text='[b]Logout[/b]', color=(0,0,0,1), font_size=40, markup=True)) #bind to login screen
        self.empty.bind(on_press=self.logout)
        self.layout.add_widget(self.empty)
        self.vote=(Label(text='[b]Voting[/b]', color=(0,0,0,1), font_size=40, markup=True))
        self.layout.add_widget(self.vote)
        self.garden1=(Button(id='Jurong Garden',text='', color=(0,0,0,0), font_size=30, background_normal='1st_garden.jpg'))
        self.garden1.bind(on_press=self.menu_switch)
        self.layout.add_widget(self.garden1)
        self.vote1=Button(text='')
        self.layout.add_widget(self.vote1)
        self.garden2=(Button(id='RedHill Garden',text='', color=(0,0,0,0), font_size=30, background_normal='2nd_garden.jpg'))
        self.garden2.bind(on_press=self.menu_switch)
        self.layout.add_widget(self.garden2)
        self.vote2=Button(text='',width=30, background_color=(0.3,1,0,1))
        self.vote2.bind(on_press=self.voting_switch)
        self.layout.add_widget(self.vote2)
        self.garden3=Button(id='Simei Garden',text='', color=(0,0,0,0), font_size=30, background_normal='3rd_garden.jpg')
        self.garden3.bind(on_press=self.menu_switch)
        self.layout.add_widget(self.garden3)
        self.vote3=Button(text='',width=30)
        self.layout.add_widget(self.vote3)
        self.add_widget(self.layout)
        self.current='menu'
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
        # self.current='menu'
        # label.bind(size=label.setter('text_size
    def menu_switch(self, instance):
        scr3 = self.manager.get_screen('scr3')
        from kivy.core.window import Window
        Config.set('graphics', 'resizable', False)
        Window.size=(650,650)
        Window.clearcolor=((252/255), (245/255), (237/255), 1)
        scr3.textupdate('[u][b]'+str(instance.id)+'[/b][/u]')
        self.manager.transition.direction='left'
        self.manager.current='scr3'
    def voting_switch(self,instance):
        print(instance.background_color)
        if instance.background_color==[0.3,1,0,1]:
            scr7=self.manager.get_screen('scr7')
            from kivy.core.window import Window
            Window.size=(650,650)
            Window.clearcolor=((252/255), (245/255), (237/255), 1)
            self.manager.transition.direction='left'
            self.manager.current='scr7'
    def logout(self,instance):
        login=self.manager.get_screen('login')
        from kivy.core.window import Window
        Config.set('graphics', 'resizable', False)
        Window.clearcolor=(1,1,1, 1)
        Window.size=(600,600)
        self.manager.transition.direction='left'
        self.manager.current='login'




# class Switcher(App):



def reset():
    import kivy.core.window as window
    from kivy.base import EventLoop
    if not EventLoop.event_listeners:
        from kivy.cache import Cache
        window.Window=window.core_select_lib('window', window.window_impl, True)
        Cache.print_usage()
        for cat in Cache._categories:
            Cache._objects[cat]={}
# reset()
# myapp=Switcher()
# myapp.run()
