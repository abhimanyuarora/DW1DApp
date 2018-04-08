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

class Login(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
            # Label:
            #     text: "Login"
            #     color: (0,0,0,1)
            #     font_size: 60
            #     center_x: root.width * 0.5
            #     center_y: root.top * 0.8
        from kivy.core.window import Window
        Window.clearcolor=(0.127, 0.191, 0.63, 1)
        root=Screen()
        self.layout = FloatLayout(size_hint=(1,1))
        self.layout.add_widget(Label(text='Login', color=(0,0,0,1),font_size=60, center_x=root.width*0.5, center_y=root.top*0.8))
        #self.layout.add_widget(TextInput(multiline=False, height=35,width=30))
        self.layout.add_widget(Label(text="Login",color=(0,1,1,1),size_hint=(0.10, 0.1), pos_hint={'top':0.60, 'right':0.7}))
        self.layout.add_widget(Button(text="Login2",color=(0,1,1,1),size_hint=(0.10, 0.1), pos_hint={'top':0.4, 'right':0.7}))
        self.add_widget(self.layout)
        # self.layout=BoxLayout(orientation='vertical')
        # # Add your code below to add the two Buttons
        # button1 = Button(text = 'setting')
        # #button1.bind(on_press=self.change_to_setting)
        # self.layout.add_widget(button1)
        #
        # button2 = Button(text = 'quit')
        # #button2.bind(on_press = self.quit_app)
        # self.layout.add_widget(button2)
        #
        # self.add_widget(self.layout)

class Menu(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        self.layout=BoxLayout(orientation='horizontal')
        self.bl=Button(text='Settings')
        #self.bl.bind(on_press=self.changesettings)
        self.layout.add_widget(self.bl)
        self.bl2=Button(text='Quit')
        #self.bl2.bind(on_press=self.quit)
        self.layout.add_widget=(self.bl2)
        self.add_widget(self.layout)

class LatihanApp(App):
    def build(self):
        # load=self.load_kv("C:/Users/Me/Desktop/textfile.kv")
        sm=ScreenManager()
        sm.add_widget(Menu(name='menu'))
        sm.add_widget(Login(name='login'))
        sm.current='login'
        return sm


if __name__ == '__main__':
    LatihanApp().run()
