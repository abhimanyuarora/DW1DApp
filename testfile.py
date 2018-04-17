from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            Color=(1,1,0,1)
            Ellipse(pos=self.pos,size=self.size)
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
