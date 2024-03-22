from datetime import datetime as dt
import Juegopiedrapapelotijera as jp
import Lulo_traduccion as lt 
import lulo_dinero as ld 
import capitales as cp

import lulo_chiste as lch
def chatbot ():
    print("\n")
    print("Hola me llamo Lulo y voy a ser tu nuevo ayudante para todo lo que me necesites preguntar")
    respuesta = input ("Escribe algo : ")
    if respuesta == ("Cual es tu edad ? "):
        print("Soy una IA no tengo edad")
    elif respuesta == ("De donde eres ? "):
        print("Colombia")
    elif respuesta == ("que dia es hoy?"):
       dia = dt.now()
       print("La fecha y hora de hoy es: ",dia)
    elif respuesta == ("cual es tu comida favorita?"):
        print("Me encanta la pasta y a ti?")
    elif respuesta==("que dia de la semana es?"):
        dia = dt.now()
        semana = dia.weekday()
        print ("el dia de la semana es : ",semana)
    elif respuesta == ("Cuanto es 2 + 2 ?") :
        print("2 + 2 es igual a 4 ")
    elif respuesta == ("Cual es el pais mas grande del mundo ?"):
        print("El pais mas grande del mundo es Rusia")
    elif respuesta == ("cual es el animal mas rapido del mundo ?"):
        print("el animal mas rapido del mundo es el cheeta")
    elif "nombre" in respuesta or "llamas" in respuesta :
        print("mi nombre es Lulo")
        
    elif "hoy" in respuesta :
        dia = dt.now()
        print("el dia de hoy es",dia )
    elif "mas" in respuesta or "+" in respuesta :
        print(respuesta)
    elif "suma" in respuesta :
      numero1 =  int(input("pon un numero : "))
      numero2 = int(input ("pon otro numero : "))
      print("la respuesta es ", numero1 + numero2)
    elif "multiplica" in respuesta :
      numero1 =  int(input("pon un numero : "))
      numero2 = int(input ("pon otro numero : "))
      print("la respuesta es ", numero1 * numero2)
    elif "menos"in respuesta :
        respuesta1= int(input("pon un numero: "))
        respuesta2 = int(input("pon otro numero: "))
        print("la respuesta es ",respuesta1 - respuesta2)
    elif "divide"in respuesta :
        respuesta1= int(input("pon un numero: "))
        respuesta2 = int(input("pon otro numero: "))
        print("la respuesta es ",respuesta1 / respuesta2)
    elif "capital"in respuesta :
        pais= input("que pais deseas ? :")
        cp.obtenercapital(pais)

        """Desde aca vamos a usar los archivos para que lulo los pueda poner"""
    elif "piedra" in respuesta:
        jp.juego()
    elif "aventura"in respuesta :
        print()
    elif"ingles" in respuesta :
        lt.traduccion(respuesta)
    #elif "recordar" in respuesta:
        #lr.recordatorio(respuesta)
    elif "chiste" in respuesta :
        lch.lulo_chistes()
        print(lch.lulo_chistes())
    """elif "peso"or"dolar"in respuesta:
        respuesta2 = input("escoge una opcion\n (1) de peso a dolar (2) de dolar a peso: ")
        if respuesta2 == "1":
           convertir2=int(input("que numero quieres convertir: "))
           ld.peso_dolar(convertir2)

        elif respuesta2 =="2":
          convertir =  int(input("que numero quieres convertir: "))
          ld.dolar_a_peso(convertir)"""
    """ elif "chiste" in respuesta :
        lch.lulo_chistes()
        print(lch.lulo_chistes())"""




        
        





chatbot()
  







  

   

   





        
