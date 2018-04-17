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
from kivy.uix.label import Label

import time
KIVY_DPI=240
KIVY_METRICS_DENSITY=2
class Login(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Window.clearcolor=(1, 1, 1, 1)
        root=FloatLayout(size=(dp(300),dp(300)))
        self.layout = FloatLayout(size=(sp(300),sp(300)))
        self.layout.add_widget(Image(source='garden_lah.png', size_hint=(0.9,0.9), pos_hint={'top':1.03, 'right':0.95}))
        # self.layout.add_widget(self.insert_image)
        # self.layout.add_widget(Label(text='Login', color=(0,0,0,1),font_size=sp(60), center_x=dp(root.width*0.5), center_y=dp(root.top*2.2)))
        self.user_input=(TextInput(multiline=False, size_hint=(0.3,0.07), pos_hint={'x':0.368, 'y':0.21},font_size=(20)))
        self.layout.add_widget(self.user_input)
        username=(Label(text="Username",color=(0,0,0,1),font_size=(30),pos_hint={'x':-0.26, 'y':-0.25}))
        self.layout.add_widget(username)
        self.user_pwd=(TextInput(multiline=False, height=dp(10),width=dp(10), size_hint=(0.3,0.07),pos_hint={'x':0.368, 'y':0.13}, font_size=sp(20), password=True))
        usspwd=(Label(text="Password",color=(0,0,0,1),font_size=sp(30), pos_hint={'x':-0.26, 'y':-0.33}))
        self.layout.add_widget(usspwd)
        self.layout.add_widget(self.user_pwd)
        quit_button=(Button(text="Quit",color=(0,1,1,1),size_hint=(0.06, 0.06), pos_hint={'top':dp(0.12), 'right':dp(0.67)}))
        quit_button.bind(on_press=self.quit_app)
        self.layout.add_widget(quit_button)
        self.login_button=(Button(text="Login",color=(0,1,1,1),size_hint=(0.09, 0.09), pos_hint={'top':dp(0.12), 'right':dp(0.49)})) #fix login button size/position whatever
        self.login_button.bind(on_press=self.change_to_menu)
        self.layout.add_widget(self.login_button)
        self.add_widget(self.layout)
        self.current='login'
    def change_to_menu(self,value):
        if self.user_pwd.text=='test' and self.user_input.text=='test':
            self.manager.transition.direction='left'
            self.manager.current='menu'
        else:
            self.login_button.text='Error'
            time.sleep(0.1)
            self.login_button.text='Login'
    def quit_app(self,value):
        App.get_running_app().stop()
class Menu(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Window.clearcolor=(0.4, 0.8, 1, 1)
        self.layout = GridLayout(cols=2, spacing=(30))
        self.empty=(Label(text='[b]Gardens[/b]', color=(1,0,0,1), font_size=40, markup=True))
        self.layout.add_widget(self.empty)
        self.vote=(Label(text='[b]Voting[/b]', color=(1,0,0,1), font_size=40, markup=True))
        self.layout.add_widget(self.vote)
        self.garden1=(Button(text='', color=(0,0,0,1), font_size=30, background_normal='1st_garden.jpg'))
        self.layout.add_widget(self.garden1)
        self.vote1=Button(text='')
        self.layout.add_widget(self.vote1)
        self.garden2=(Button(text='', color=(0,0,0,1), font_size=30, background_normal='2nd_garden.jpg'))
        self.layout.add_widget(self.garden2)
        self.vote2=Button(text='',width=30, background_color=(0.3,1,0,1))
        self.layout.add_widget(self.vote2)
        self.garden3=Button(text='', color=(0,0,0,1), font_size=30)
        self.layout.add_widget(self.garden3)
        self.vote3=Button(text='',width=30)
        self.layout.add_widget(self.vote3)
        # self.vote1.bind(self.update_canvas)
        self.add_widget(self.layout)
        self.current='menu'


class Menu(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        super(Menu,self).__init__(**kwargs)
        navigationdrawer = NavigationDrawer()
        side_panel = BoxLayout(orientation='vertical')
        side_panel.add_widget(Label(text='Panel label'))
        # bl1=Button(text='A button')
        # bl1.bind(on_press=self.changesettings)
        #side_panel.add_widget(bl1)
        side_panel.add_widget(Button(text='Another button'))
        navigationdrawer.add_widget(side_panel)
        self.add_widget(navigationdrawer)
        main_panel = BoxLayout(orientation='vertical')
        label_bl = BoxLayout(orientation='horizontal')
        # label = Label(text=label_head, font_size='15sp',
                      # markup=True, valign='top')
        label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
        # label_bl.add_widget(label)
        label_bl.add_widget(Widget(size_hint_x=None, width=dp(10)))
        main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
        main_panel.add_widget(label_bl)
        main_panel.add_widget(Widget(size_hint_y=None, height=dp(10)))
        navigationdrawer.add_widget(main_panel)
        # label.bind(size=label.setter('text_size'))
        def set_anim_type(name):
            navigationdrawer.anim_type = name
        button = Button(text='toggle NavigationDrawer state (animate)',
                        size_hint_y=0.2)
        button.bind(on_press=lambda j: set_anim_type('slide_above_anim'))
        button.bind(on_press=lambda j: navigationdrawer.toggle_state())
        main_panel.add_widget(button)

class DWApp(App):
    def build(self):
        # load=self.load_kv("C:/Users/Me/Desktop/textfile.kv")
        sm=ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Login(name='login'))
        sm.current='login'
        return sm

if __name__ == '__main__':
    DWApp().run()
