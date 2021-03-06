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
from kivy.uix.scrollview import ScrollView

class Screen4(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        self.layout=BoxLayout(orientation='vertical')
        leaderboard=GridLayout(cols=2)
        menubtn=Button(text='<-', font_size=20, color=(0,0,0,1), size_hint_x=None, size_hint_y=None, width=30, height=50)
        menubtn.bind(on_press=self.back_to_menu)
        leaderboard.add_widget(menubtn)
        leaderboard.add_widget(Label(text='Leaderboard', font_size=60, color=(0,0,0,1)))
        self.layout.add_widget(leaderboard)
        leaders=GridLayout(rows=1, cols=3)
        leaders.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        leaders.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        leaders.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        self.layout.add_widget(leaders)
        self.layout.add_widget(Label(text='[b]Experts[/b]', font_size=30, color=(0,0,0,1), markup=True))
        experts=GridLayout(rows=1, cols=3)
        experts.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        experts.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        experts.add_widget(Label(text='add image here'))
        scroll=ScrollView()
        scroll.add_widget(experts)
        # leaders.add_widget(Image(source=''))
        self.layout.add_widget(scroll)
        self.layout.add_widget(Label(text='Intermediate', font_size=20, color=(0,0,0,1)))
        junior=GridLayout(rows=1, cols=3)
        junior.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        junior.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        junior.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        self.layout.add_widget(junior)
        self.layout.add_widget(Label(text='Newcomers', font_size=20, color=(0,0,0,1)))
        newcomers=GridLayout(rows=1, cols=3)
        newcomers.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        newcomers.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        newcomers.add_widget(Label(text='add image here'))
        # leaders.add_widget(Image(source=''))
        self.layout.add_widget(newcomers)
        self.add_widget(self.layout)
        self.current='scr4'
    def back_to_menu(self, instance):
        self.manager.transition.direction='right'
        self.manager.current='scr3'
        from kivy.core.window import Window
        Window.clearcolor=((252/255), (245/255), (237/255), 1)
        Window.size=(650,650)
# class Switcher(App):
#     def build(self):
#         sm=ScreenManager()
#         sm.add_widget(Screen4(name='scr4'))
#         sm.current='scr4'
#         return sm
#
#
# def reset():
#     import kivy.core.window as window
#     from kivy.base import EventLoop
#     if not EventLoop.event_listeners:
#         from kivy.cache import Cache
#         window.Window=window.core_select_lib('window', window.window_impl, True)
#         Cache.print_usage()
#         for cat in Cache._categories:
#             Cache._objects[cat]={}
# reset()
# myapp=Switcher()
# myapp.run()
