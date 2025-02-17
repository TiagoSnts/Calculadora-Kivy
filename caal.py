from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import math

Window.size = (1000,700)

class MyCalc(App):
    def build(self):

        layout = BoxLayout(orientation = 'vertical') #define a orientação dos botoes
        botoes = GridLayout(cols = 3) #define quantas colunas os botoes ficaram divididos

        self.display = Label(text="", font_size='50px') #texto que irá aparecer no display e o tamanho da fonte

        self.button_zerar = Button(text='Zerar')
        self.button_zerar.bind(on_press = self.zerar) #adicionando um evento ao botao zerar

        self.button0 = Button(text='0')
        self.button1 = Button(text='1')
        self.button2 = Button(text='2')
        self.button3 = Button(text='3')
        self.button4 = Button(text='4')
        self.button5 = Button(text='5')
        self.button6 = Button(text='6')
        self.button7 = Button(text='7')
        self.button8 = Button(text='8')
        self.button9 = Button(text='9')
        self.button_soma = Button(text='+')
        self.button_igual = Button(text='=')
        self.button_sub = Button(text='-')
        self.button_mult = Button(text='*')
        self.button_div = Button(text='/')
        self.button_pot = Button(text='^')
        self.button_r2 = Button(text='√')

        self.button0.bind(on_press = self.armazenar)
        self.button1.bind(on_press = self.armazenar)
        self.button2.bind(on_press = self.armazenar)
        self.button3.bind(on_press = self.armazenar)
        self.button4.bind(on_press = self.armazenar)
        self.button5.bind(on_press = self.armazenar)
        self.button6.bind(on_press = self.armazenar)
        self.button7.bind(on_press = self.armazenar)
        self.button8.bind(on_press = self.armazenar)
        self.button9.bind(on_press = self.armazenar)
        self.button_soma.bind(on_press = self.armazenar)
        self.button_div.bind(on_press = self.armazenar)
        self.button_mult.bind(on_press = self.armazenar)
        self.button_pot.bind(on_press = self.armazenar)
        self.button_r2.bind(on_press = self.armazenar)
        self.button_sub.bind(on_press = self.armazenar)
        self.button_igual.bind(on_press = self.calcular)

        botoes.add_widget(self.button_zerar)
        botoes.add_widget(self.button0)
        botoes.add_widget(self.button1)
        botoes.add_widget(self.button2)
        botoes.add_widget(self.button3)
        botoes.add_widget(self.button4)
        botoes.add_widget(self.button5)
        botoes.add_widget(self.button6)
        botoes.add_widget(self.button7)
        botoes.add_widget(self.button8)
        botoes.add_widget(self.button9)
        botoes.add_widget(self.button_soma)
        botoes.add_widget(self.button_div)
        botoes.add_widget(self.button_r2)
        botoes.add_widget(self.button_mult)
        botoes.add_widget(self.button_pot)
        botoes.add_widget(self.button_sub)
        botoes.add_widget(self.button_igual)

        layout.add_widget(self.display)
        layout.add_widget(botoes)

        return layout

    def zerar(self, event):
        self.display.text = ''

    def armazenar(self, event):
        print(event.text)
        self.display.text += event.text

    def calcular(self,event):
        if '+' in self.display.text:
            numbers = self.display.text.split('+')
            calc = float(numbers[0]) + float(numbers[1])
            self.display.text = str(calc)
        elif '-' in self.display.text:
            numbers = self.display.text.split('-')
            calc = float(numbers[0]) - float(numbers[1])
            self.display.text = str(calc)
        elif '*' in self.display.text:
            numbers = self.display.text.split('*')
            calc = float(numbers[0]) * float(numbers[1])
            self.display.text = str(calc)
        elif '/' in self.display.text:
            numbers = self.display.text.split('/')
            calc = float(numbers[0]) / float(numbers[1])
            self.display.text = str(calc)
        elif '^' in self.display.text:
            numbers = self.display.text.split('^')
            print(numbers)
            calc = float(numbers[0]) ** float(numbers[1])
            self.display.text = str(calc)
        elif '√' in self.display.text:
            numbers = self.display.text.split('√')
            calc = math.sqrt(float(numbers[0])) 
            self.display.text = str(calc)

if __name__ == "__main__":
    MyCalc().run()