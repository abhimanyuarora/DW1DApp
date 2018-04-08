from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.graphics import Canvas
class Login(Screen):
    def __init__(self, **kwargs):
        self.canvas.add(Color(1., 1., 0)))
        self.canvas.add(Rectangle(size=(50, 50))))
        self.add_widget(Label(text="Login",color="0,0,0,1",font_size=60, center_x=root.width*0.5, center_y=root.top*0.8))

class myApp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Login(name='login'))
        sm.current='login'
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
if __name__=='__main__':
    myApp().run()
