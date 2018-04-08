from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
class MainMenu(Screen):
    def __init__(self,**kwargs):
        super(MainMenu,self).__init__(**kwargs)
        self.layout=BoxLayout(orientation='horizontal')
        self.bl=Button(text='Settings')
        self.bl.bind(on_press=self.changesettings)
        self.layout.add_widget(self.bl)
        self.bl2=Button(text='Quit')
        self.bl2.bind(on_press=self.quit)
        self.layout.add_widget=(self.bl2)
    def changesettings(self,value):
        self.manager.transition.direction='right'
        self.manager.current='menu'
    def quit(self,value):
        App.get_running_app().stop()
        
class OtherMenu(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        self.layout=BoxLayout(orientation='horizontal')
        self.q=Button(text='Back to menu',on_press=self.change_to_menu)
        self.layout.add_widget(self.q)
        self.se=Label(text='Brightness')
        self.layout.add_widget=(self.se)
    def change_to_menu(self,value):
        self.manager.transition.direction='left'
        self.manager.current='settings'
sm=ScreenManager()
sm.add_widget(MainMenu(name='menu'))
sm.add_widget(OtherMenu(name='settings'))
sm.current='menu'
class Switcher(App):
    def build(self):
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