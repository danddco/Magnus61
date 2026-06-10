import sqlite3
from cdMx_sql import *
from datetime import date
from cdMx_pandas import *
from cdMx_web_Arriba import *
from cdMx_web_Abajo import *
from secuencias_web import websecuencias
from Expediente_David import webExpDaniel
from Resumen_David import webResDaniel
from Expediente_Fashident import webExpIvan
from Resumen_Ivan import webResIvan
from Expediente_PurySystem import webExpPuSis
from Resumen_PuriSystem import webResPuSi
from Expediente_Duo import webExpDuo
from Resumen_Duo import webResDuo


from Expediente_Monterrey import webExpRey
#from Resumen_Monterrey  import webResRey


def Actualizacion_Web():
    opciones = ["Actualizacion Clientes", "Secuencia", "maria", "ana"]

    print("Opciones disponibles:")
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")

    eleccion = int(input("Escoge una opción (1-4): "))

    match eleccion:
        case 1:
            print("Actualizacion Expediente Clientes")
            clientes_Web()
        case 2:
            print("Actulizacion Expediente Clientes")
            clientes_Web()

        case 3:
            print("Acción para MARIA: calcular algo")
            resultado = 5 * 5
            print(f"Maria obtiene: {resultado}")

        case 4:
            print("Acción para ANA: mostrar mensaje motivador")
            print("¡Sigue adelante, Ana! 🚀")

        case _:
            print("Opción inválida")
# =======================================================================
def clientes_Web():
    opciones2 = ["David", "FashIdent", "PuriSystem", "Monterrey","Duo"]

    print("Opciones disponibles:")
    for i, opcion in enumerate(opciones2, start=1):
        print(f"{i}. {opcion}")

    eleccion = int(input("Escoge una opción (1-4): "))

    match eleccion:
        case 1:
            print("Acción para PEPE: imprimir saludo")
            print("Hola Pepe 👋")
            webExpDaniel()
            webResDaniel()
    
        case 2:
            print("Actualizar Registros asociados a Ivan Fashidente")
            webExpIvan()
            webResIvan()
            websecuencias(1,2,2)     

        case 3:
            print("Actualizar Registros asociados a PuriSistem")
            webExpPuSis()
            webResPuSi()
            websecuencias(1,2,2)  

        case 4:
            print("Actualizar Registros asociados a Monterrey")
            webExpRey()
            webResRey()
            websecuencias(1,2,2)  
        case 5:
            print("Actualizar Registros asociados a Duo")
            webExpDuo()
            webResDuo()
            websecuencias(1,2,2)  




        case _:
            print("Opción inválida")



Actualizacion_Web()