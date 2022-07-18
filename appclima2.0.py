from ast import Param
from tkinter import *
import requests

#75e55ad50d2bf30c6a704bb4be9618a3
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def clima_json(ciudad):
    API_key="75e55ad50d2bf30c6a704bb4be9618a3"
    URL="https://api.openweathermap.org/data/2.5/weather"
    parametros={"APPID":API_key, "q":ciudad,"units":"metric","lang":"es"}
    response=requests.get(URL, params=parametros)
    clima=response.json()
    mostrar_respuesta(clima)
    

def mostrar_respuesta (clima):
    nombre_ciudad=clima["name"]
    desc=clima["weather"][0]["description"]
    temp=clima["main"]["temp"]
    ciudad["text"]=nombre_ciudad
    temperatura["text"]=str(int(temp))+" °C"
    descripcion["text"]=desc

ventana=Tk()
ventana.geometry("350x550")

texto_ciudad=Entry(ventana,font=("Courier",20,"normal"),justify="center")
texto_ciudad.pack(padx=30,pady=30)

obtener_clima=Button(ventana,text="Obtener clima",font=("Courier",20,"normal"),justify="center",command=lambda:clima_json(texto_ciudad.get()))
obtener_clima.pack()

ciudad=Label(font=("Coursier",20,"normal"))
ciudad.pack()

temperatura=Label(font=("Coursier",50,"normal"))
temperatura.pack(padx=20,pady=20)

descripcion=Label(font=("Coursier",20,"normal"))
descripcion.pack(padx=10,pady=10)

ventana.mainloop()