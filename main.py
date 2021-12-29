"""
EN ESTA VERSION 1.1 HEREDAMOS DE LA CLASE SCREEN, TRABAJAMOS CON DIFERENTES VENTANAS(SCREEN).
SE REALIZA EN LA MEDIDA DE LOS POSIBLE QUE LOS TEXTOS SE ADAPTEN AL TAMAÑO DE LA PANTALLA DEL DISPOSITIVO MOVIL
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.widget import Widget
from kivy.core.window import Window
#from Kivy.main import RootWidget
"""
Por si hay problemas con la version GL,tambien se puede crear una variable de entorno con 
clave-valor--> KIVY_GL_BACKEND : angle_sdl2
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
"""

from NumerosRomanos import *

__version__ = "1.1"

#Window.size = (1280,720)
Builder.load_file("design.kv")

resultado_mostrado = False #controlamos para que al mostrar la conversion y pulsar un boton se borre el display


class CalculadoraScreen(Screen):
    def pulsacion(self,digito):
        max_len_input = 15
        #Si la longitud del texto es mayor o igual a max_len no actualizamos el display
        if(len(self.ids.entry.text)>=max_len_input): return
        global resultado_mostrado
        #Borramos el display
        if(resultado_mostrado):
            self.borra_display()
            resultado_mostrado = False

        #Debemos comprobar que si la primera pulsacion es un cero no lo indque en el display
        if(digito == '0'):
            if(len(self.ids.entry.text)>=1):
                self.ids.entry.text += digito
        else:
            self.ids.entry.text += digito

    def borra_caracter(self):
        self.ids.entry.text = self.ids.entry.text[0:-1]

    def borra_display(self):
        self.ids.entry.text = ""

    def convertir(self):
        global resultado_mostrado
        #Comprobamos si es un numero entero y menor de 4000
        if( is_decimal(self.ids.entry.text) and (int(self.ids.entry.text)< 4000) ):
            self.ids.entry.text = calculadora_dec_to_rom(int(self.ids.entry.text))
        elif(eval_romano(self.ids.entry.text)):
            self.ids.entry.text= str(calculadora_rom_to_dec(self.ids.entry.text) )
        else:
            self.ids.entry.text= "ERROR"
    
        resultado_mostrado = True

    def ir_ayuda(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "ayuda_screen"
    

class RootWidget(ScreenManager):
        pass

    
class AyudaScreen(Screen):
    def atras(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "calculadora_screen"


class MainApp(App):
    def build(self):
        return RootWidget()

    
    #Cuando arranca la APP enlazamos un evento para que cuando presionemos un boton del teclado llamemos a la funcion presion_teclado
    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.presion_teclado)
    
    def presion_teclado(self, window, key, *args):
        #Detecta que se ha presionado escape
        if key == 27:
            # do what you want, return True for stopping the propagation
            print("Presionado escape")
            self.on_pause()
            return True 


if __name__ == "__main__":
    MainApp().run()