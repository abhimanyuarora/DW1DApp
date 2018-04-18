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
        Window.clearcolor=(1, 0.5, 1, 1)
        self.layout.add_widget(Label(text='[b]VOTING[/b]', font_size=50, color=(1,1,0,1), markup=True))
        self.layout.add_widget(Label(text='='*200, font_size=30, color=(1,0,0,1), markup=True, size_hint_y=None, height=30))
        formula=GridLayout(cols=2)
        formula.add_widget(Label(text='[u]Proposed formula[/u]', font_size=40, color=(1,0,0,1), markup=True))
        formula.add_widget(Label(text='', font_size=30, color=(1,0,0,1), markup=True))
        self.layout.add_widget(formula)
        waterlevel=GridLayout(cols=2)
        waterlevel.add_widget(Label(text='Water level: ',font_size=30, color=(0,0,0,1)))
        pb=ProgressBar(max=100)
        pb.value=75 #bind it to a method that extracts water level from firebase
        waterlevel.add_widget(pb)
        self.layout.add_widget(waterlevel)
        nutrientlevel=GridLayout(cols=2)
        nutrientlevel.add_widget(Label(text='Nutrient level: ',font_size=30, color=(0,0,0,1)))
        pb2=ProgressBar(max=100)
        pb2.value=75 #bind it to a method that extracts water level from firebase
        nutrientlevel.add_widget(pb2)
        self.layout.add_widget(nutrientlevel)
        regularity=GridLayout(cols=2)
        regularity.add_widget(Label(text='Regularity: ', font_size=30, color=(0,0,0,1)))
        duration=BoxLayout(orientation='vertical')
        duration.add_widget(Label(text='[u]'+'3'+'[/u]'+' times a week', font_size=30, color=(0,0,0,1), markup=True)) #update the number to a string obtained from a method
        duration.add_widget(Label(text='Time: '+'15:04', font_size=30, color=(0,0,0,1))) #update the time to a string obtained from a method
        regularity.add_widget(duration)
        self.layout.add_widget(regularity)
        light=GridLayout(cols=2)
        light.add_widget(Label(text='Light: ', font_size=30, color=(0,0,0,1)))
        slide=GridLayout(cols=2)
        value1=(Label(text='', font_size=30, color=(0,0,0,1), size_hint_x=None, width=40))
        slide.add_widget(value1)
        slider=Slider(min=0, max=200)
        def OnSliderValueChange(instance,value):
            value1.text = str(int(value))
        slider.bind(value=OnSliderValueChange)
        slide.add_widget(slider)
        light.add_widget(slide)
        # light.add_widget(Label(text=str(slider.value),font_size=50,color=(0,0,0,1)))
        self.layout.add_widget(light)
        self.layout.add_widget(Button(text='[b]Cast Your Vote[/b]', color=(1,0,0,1), font_size=50, markup=True, background_color=(1,0,0,1),size_hint_y=None, height=100))
        self.add_widget(self.layout)
        self.current='scr7'
class testapp(App):
    def build(self):
        sm=ScreenManager()
        sm.add_widget(Screen7(name='scr7'))
        return sm
testapp().run()
