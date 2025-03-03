from guizero import App, Text, TextBox, PushButton, Picture
from funciones import *

app= App(
    bg="light grey",
    title="LA RULETA DE LA SUERTE",
    height=200,
    width=350)

# Pregunta jugador 1
nombre1=app.question("jugador 1","Cual es tu nombre?")
jugador1=nombre1
# Pregunta jugador 2
nombre2=app.question("jugador 2","Cual es tu nombre?")
jugador2=nombre2
# Pregunta jugador 3
nombre3=app.question("jugador 3","Cual es tu nombre?")
jugador3=nombre3

#Marcador de puntos que llevas en la ronda
puntos_marcador=TextBox(app, text="Puntos: ", align="left")
puntos_marcador.enabled= False

def resultado_tirada():
    x = tirar_de_la_ruleta()
    print(x)
    global puntos_marcador
    puntos_marcador.value= "Puntos:" +str(x)
    

boton_tirar= PushButton(app,text="Tirar de la ruleta",image="ruleta.gif",align="left",command=resultado_tirada)
boton_tirar.bg="lightblue"
picture= Picture(app, image="descargas/witch_hat_atelier_panel.png")

app.display()