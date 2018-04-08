from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.screenmanager import ScreenManager, Screen
class MainMenu(Screen):
    def __init__(self,**kwargs):
            super(MainMenu,self).__init__(**kwargs)
            # self.layout=BoxLayout()
            # self.bl=Button(text='Settings')
            # self.bl.bind(on_press=self.changesettings)
            # self.layout.add_widget(self.bl)
            #
            # self.bl2=Button(text='Quit')
            # self.bl2.bind(on_press=self.quit)
            # self.layout.add_widget(self.bl2)
            # self.add_widget(self.layout)

            navigationdrawer = NavigationDrawer()
            side_panel = BoxLayout(orientation='vertical')
            side_panel.add_widget(Label(text='Panel label'))
            bl1=Button(text='A button')
            bl1.bind(on_press=self.changesettings)
            side_panel.add_widget(bl1)
            side_panel.add_widget(Button(text='Another button'))
            navigationdrawer.add_widget(side_panel)
            self.add_widget(navigationdrawer)
            label_head = (
                '[b]Example label filling main panel[/b]\n\n[color=ff0000](p'
                'ull from left to right!)[/color]\n\nIn this example, the le'
                'ft panel is a simple boxlayout menu, and this main panel is'
                ' a BoxLayout with a label and example image.\n\nSeveral pre'
                'set layouts are available (see buttons below), but users ma'
                'y edit every parameter for much more customisation.')
            main_panel = BoxLayout(orientation='vertical')
            label_bl = BoxLayout(orientation='horizontal')
            label = Label(text=label_head, font_size='15sp',
                          markup=True, valign='top')
            label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
            label_bl.add_widget(label)
            label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
            main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
            main_panel.add_widget(label_bl)
            main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
            navigationdrawer.add_widget(main_panel)
            label.bind(size=label.setter('text_size'))
            def set_anim_type(name):
                navigationdrawer.anim_type = name
            button = Button(text='toggle NavigationDrawer state (animate)',
                            size_hint_y=0.2)
            button.bind(on_press=lambda j: set_anim_type('slide_above_anim'))
            button.bind(on_press=lambda j: navigationdrawer.toggle_state())
            main_panel.add_widget(button)
    def changesettings(self,instance):
        self.manager.transition.direction='right'
        self.manager.current='settings'
    def quit(self,instance):
        global app
        app.stop()

class OtherMenu(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        self.layout=BoxLayout(orientation='horizontal')
        self.se=Label(text='Brightness')

        self.layout.add_widget(self.se)
        self.add_widget(self.layout)
        self.q=Button(text='Back to menu',on_press=self.change_to_menu)
        self.layout.add_widget(self.q)
    def change_to_menu(self,value):
        self.manager.transition.direction='left'
        self.manager.current='menu'

class Switcher(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(MainMenu(name='menu'))
        sm.add_widget(OtherMenu(name='settings'))
        sm.current='menu'
        return sm
    def on_pause(self):
        return True


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
app = None
if __name__=='__main__':
    app = Switcher()
    app.run()
