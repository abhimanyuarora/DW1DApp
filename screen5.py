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
from kivy.garden.graph import Graph, MeshLinePlot
from math import sin
import matplotlib.pyplot as plt
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import copy
class Screen5(Screen):
    def __init__(self,**kwargs):
        Screen.__init__(self,**kwargs)
        from kivy.core.window import Window
        Window.clearcolor=(1, 1, 1, 1)
        self.layout=GridLayout(cols=2)
        menubar=GridLayout(cols=2)
        menubtn=Button(text='<-',font_size=20,size_hint_x=None,size_hint_y=None,width=30, height=50)
        menubtn.bind(on_press=self.back_to_menu)
        menubar.add_widget(menubtn)
        menubar.add_widget(Label(text='[u]Soil Moisture: [/u]', font_size=30, color=(0,0,0,1), markup=True))
        self.layout.add_widget(menubar)
        percentage=(Label(text='', font_size=40, color=(0,0,0,1))) #raw percentage
        self.layout.add_widget(percentage)
        self.layout.add_widget(Label(text='[u]pH[/u]', font_size=30, color=(0,0,0,1), markup=True))
        plt.gcf().subplots_adjust(bottom=0.3)
        plt.plot([1, 23, 2, 4])
        self.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.layout.add_widget(Label(text='[u]Temperature[/u]', font_size=30, color=(0,0,0,1), markup=True))
        plt.figure()
        plt.gcf().subplots_adjust(bottom=0.3)
        plt.plot([13, 15, 25, 10])
        self.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.layout.add_widget(Label(text='[u]Humidity: [/u]', font_size=30, color=(0,0,0,1), markup=True))
        plt.figure()
        plt.gcf().subplots_adjust(bottom=0.3)
        plt.plot([13, 35, 55, 10])
        self.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.layout.add_widget(Label(text='[u]Fluroscence[/u]', font_size=30, color=(0,0,0,1), markup=True))
        plt.figure()
        plt.gcf().subplots_adjust(bottom=0.3)
        plt.plot([13, 15, 40, 10])
        self.layout.add_widget(FigureCanvasKivyAgg(plt.gcf()))
        self.add_widget(self.layout)
        self.current='scr5'

    def back_to_menu(self, instance):
        self.manager.transition.direction='right'
        self.manager.current='scr3'
# class testapp(App):
#     def build(self):
#         sm=ScreenManager()
#         sm.add_widget(Screen5(name='scr5'))
#         return sm
# testapp().run()
