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
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.uix.slider import Slider


class Screen7(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self,**kwargs)
        self.layout=BoxLayout(orientation='vertical')
        from kivy.core.window import Window
        Window.clearcolor=((252/255), (245/255), (237/255), 1)
        menubar=GridLayout(cols=2)
        menubtn=Button(text='<-', font_size=20, color=(0,0,0,1), size_hint_x=None, size_hint_y=None, width=30, height=70)
        menubtn.bind(on_press=self.back_to_menu)
        menubar.add_widget(menubtn)
        menubar.add_widget(Label(text='[b]VOTING[/b]', font_size=50, color=(97/255,127/255,62/255,1), markup=True))
        self.layout.add_widget(menubar)
        self.layout.add_widget(Label(text='='*200, font_size=30, color=(97/255,127/255,62/255,1), markup=True, size_hint_y=None, height=30))
        formula=GridLayout(cols=2)
        formula.add_widget(Label(text='[u]Proposed formula[/u]', font_size=40, color=(97/255,127/255,62/255,1), markup=True))
        formula.add_widget(Label(text=''))
        self.layout.add_widget(formula)
        waterlevel=GridLayout(cols=2)
        waterlevel.add_widget(Label(text='Water: ',font_size=30, color=(97/255,127/255,62/255,1)))
        slide1=GridLayout(cols=2)
        slider=Slider(min=0, max=200)
        value1=(Label(text='', font_size=30, color=(97/255,127/255,62/255,1), size_hint_x=None, width=40))
        slide1.add_widget(value1)
        def OnSliderValueChange(instance,value):
            value1.text = str(int(value))
        slider.bind(value=OnSliderValueChange)
        slide1.add_widget(slider)
        waterlevel.add_widget(slide1)
        self.layout.add_widget(waterlevel)

        nutrientlevel=GridLayout(cols=2)
        nutrientlevel.add_widget(Label(text='Nutrients: ',font_size=30, color=(97/255,127/255,62/255,1)))
        slide2=GridLayout(cols=2)
        value2=(Label(text='', font_size=30, color=(0,0,0,1), size_hint_x=None, width=40))
        slide2.add_widget(value2)
        slider2=Slider(min=0, max=200)
        def OnSliderValueChange(instance,value):
            value2.text = str(int(value))
        slider2.bind(value=OnSliderValueChange)
        slide2.add_widget(slider2)
        nutrientlevel.add_widget(slide2)
        self.layout.add_widget(nutrientlevel)

        regularity=GridLayout(cols=2)
        regularity.add_widget(Label(text='Regularity: ', font_size=30, color=(97/255,127/255,62/255,1)))
        duration=BoxLayout(orientation='vertical')
        count=GridLayout(cols=2)
        count.add_widget(TextInput(multiline=False, size_hint_x=None,width=70, font_size=30))
        count.add_widget(Label(text='times a day', font_size=30, color=(97/255,127/255,62/255,1))) #update the number to a string obtained from a method
        duration.add_widget(count)
        duration.add_widget(Label(text='Time: '+'15:04', font_size=30, color=(97/255,127/255,62/255,1))) #update the time to a string obtained from a method
        regularity.add_widget(duration)
        self.layout.add_widget(regularity)
        light=GridLayout(cols=2)
        light.add_widget(Label(text='Light: ', font_size=30, color=(97/255,127/255,62/255,1)))

        slide3=GridLayout(cols=2)
        value3=(Label(text='', font_size=30, color=(0,0,0,1), size_hint_x=None, width=40))
        slide3.add_widget(value3)
        slider3=Slider(min=0, max=100)
        def OnSliderValueChange(instance,value):
            value3.text = str(int(value))
        slider3.bind(value=OnSliderValueChange)
        slide3.add_widget(slider3)
        light.add_widget(slide3)
        # light.add_widget(Label(text=str(slider.value),font_size=50,color=(0,0,0,1)))
        self.layout.add_widget(light)
        self.layout.add_widget(Button(text='[b]Cast Your Vote[/b]', color=(152/255,188/255,111/255,1), font_size=50, markup=True, background_color=(97/255,127/255,62/255,1),size_hint_y=None, height=100))
        self.add_widget(self.layout)
        self.current='scr7'
    def back_to_menu(self, instance):
        self.manager.transition.direction='right'
        self.manager.current='menu'
# class testapp(App):
#     def build(self):
#         sm=ScreenManager()
#         sm.add_widget(Screen7(name='scr7'))
#         return sm
# testapp().run()
