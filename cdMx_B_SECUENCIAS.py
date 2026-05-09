import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import *
from tkcalendar import DateEntry
import numpy as np
import pandas as pd
from tkinter.ttk import Combobox
from cdMx_calculos import *
#from cdMx_web_secuencias import *
from cdMx_sql import *
from cdMx_pandas import *
#from cdMx_web_placas import *
#from cdMx_web_placas_cliente import *
#from cdMx_A_MAIN import *

class ventana_secuencia(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Control del Registro de las Secuencias. CircuitDesignMx 2026.02.12")
        self.state('zoomed')
        self.geometry("1350x650")

        self.protocol("WM_DELETE_WINDOW", self.volver_inicial)

        self.rMarcos()
        self.rTabla2()
        self.listado2()

        self.rTabla()
        self.entrada()


        # .....................................
        global gproye
        try:
            gproye
        except NameError:
            gproye=(1,1,1,1,1,1,1,1,1)
        

        global filt2
        try:
            filt2
        except NameError:
            filt2=' ORDER by gs_id DESC'
            #self.Bj8(filt2)
            whe_gs=""
            sor_gs=" ORDER by gs_id DESC"  
        #PonerDomingos()
        
        
        self.listado(whe_gs,sor_gs)
               
        barra_menu = tk.Menu()
        self.config(menu=barra_menu)
        menu_ventanas = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Edicion", menu=menu_ventanas)
        menu_ventanas.add_command(label="Añadir", command=lambda:self.agregar_entrada(filt2,gproye))
        menu_ventanas.add_command(label="Modificar", command=lambda:self.modificar_entrada(filt2,gproye))
        menu_ventanas.add_command(label="Eliminar", command=lambda:self.eliminar_producto(whe_gs,sor_gs))
        menu_ventanas2 = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Ordenar", menu=menu_ventanas2)
        menu_ventanas2.add_command(label="Proceso", command=lambda:self.Aj1(whe_gs,sor_gs))
        menu_ventanas2.add_command(label="Proyecto", command=lambda:self.Aj2(whe_gs,sor_gs))
        menu_ventanas2.add_command(label="Lote", command=lambda:self.Aj3(whe_gs,sor_gs))
        menu_ventanas2.add_command(label="Proyecto+Lote", command=lambda:self.Aj4(whe_gs,sor_gs))
        menu_ventanas2.add_command(label="Fecha", command=lambda:self.Aj5(whe_gs,sor_gs))
        menu_ventanas2.add_command(label="Can", command=lambda:self.Aj6(whe_gs,sor_gs))
        menu_ventanas2.add_command(label="FFE", command=lambda:self.Aj7(whe_gs,sor_gs))
        menu_ventanas2.add_command(label="VER", command=lambda:self.Aj8(whe_gs,sor_gs))
        menu_ventanas2.add_command(label="Consecutivo", command=lambda:self.Aj9(whe_gs,sor_gs))
        menu_ventanas3 = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Filtrar", menu=menu_ventanas3)
        menu_ventanas3.add_command(label="Todas", command=lambda:self.Bj1(whe_gs,sor_gs))
        menu_ventanas3.add_command(label="Proceso", command=lambda:self.Bj2(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="Proceso:Fabricacion", command=lambda:self.Bj3(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="Proyecto", command=lambda:self.Bj4(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="Lote", command=lambda:self.Bj5(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="Proyecto+Lote", command=lambda:self.Bj6(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="Fecha", command=lambda:self.Bj7(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="Fecha Actual+Adelante", command=lambda:self.Bj8(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="Fecha Registro+Adelante", command=lambda:self.Bj9(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="Can", command=lambda:self.Bj10(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="FFE", command=lambda:self.Bj11(whe_gs,sor_gs,gproye))
        menu_ventanas3.add_command(label="VER", command=lambda:self.Bj12(whe_gs,sor_gs,gproye))
        menu_ventanas4 = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Funciones", menu=menu_ventanas4)
        menu_ventanas4.add_command(label="Reajustar por Dia", command=rehajustar)
        menu_ventanas4.add_command(label="Reajustar por FFe", command=reajutar)
        menu_ventanas5 = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Publicar", menu=menu_ventanas5)
        menu_ventanas5.add_command(label="Comportamiento Fabricacion", command=self.Balance_Placas) # cdMx_web_placas
        menu_ventanas5.add_command(label="Placa Cliente", command=lambda:mierda(gproye)) # cdMx_web_placas_cliente
        menu_ventanas5.add_command(label="Pantalla", command=lambda:websecuencias(gproye)) # cdMx_web_secuencias
        menu_ventanas6 = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Ventanas", menu=menu_ventanas6)
        menu_ventanas6.add_command(label="Principal", command=self.abrir_principal)
        menu_ventanas6.add_command(label="STOCK", command=self.abrir_stock)
        menu_ventanas6.add_command(label="Proyecto", command=self.abrir_proyecto)
        menu_ventanas6.add_command(label="Registros", command=self.abrir_registros)
        barra_menu.add_command(label="Salir", command=self.volver_inicial)

    def rMarcos(self):
        self.marco = tk.Frame(width=1280, height=750, bg="light sky blue")
        self.marco.place(x=305, y=30)
        self.marco3 = tk.Frame(width=300, height=750, bg="green")
        self.marco3.place(x=1, y=30)
    def rTabla2(self): # Tabla del Listado de los Proyectos
        self.tabla2 = ttk.Treeview(
            self.marco3,
            columns=("gs_proyecto","gs_lote"),
            show="headings")
        self.tabla2.place(x=3, y=3, width=294, height=742)
        self.tabla2.heading(0, text="Proyecto")
        self.tabla2.column("gs_proyecto", width=100, anchor="center")  # Derecha
        self.tabla2.heading(1, text="Sub-Proyecto")
        self.tabla2.column("gs_lote", width=100, anchor="center")  # Derecha
        self.tabla2.bind("<ButtonRelease-1>", self.seleccionar_fila2)
    def seleccionar_fila2(self, event):
        fila = self.tabla2.focus()
        valores = self.tabla2.item(fila, "values")
        accions = [
            self.gs_proyecto,self.gs_lote
        ]
        for accion in accions:
            accion.delete(0, tk.END)
        for i, valor in enumerate(valores):
            if i < len(accions):
                accions[i].insert(0, valor)
        gproye=valores
        if not valores:
            return  # Si no hay valores, salir
        PP1=valores[0]
        PP2=valores[1]

        #gproye=[1,valores[0]]
        whe_gs=" WHERE gs_proyecto = '"+ PP1 +"' and gs_lote = '"+PP2+"'"
        sor_gs=" ORDER by gs_fecha DESC"
        self.consultar(whe_gs,sor_gs)
        
        #self.seleccionar_fila_Datos(gproye)
        #return(gproye)
    def listado2(self):
        productos2=self.conectabla2()
        for fila in self.tabla2.get_children():
            self.tabla2.delete(fila)
        for producto in productos2:
            self.tabla2.insert("", tk.END, values=producto) 
    def conectabla2(self):  # Conecta con los proyectos de las secuencias
        self.conexion = sqlite3.connect("CirDesMx.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("SELECT DISTINCT gs_proyecto, gs_lote  FROM gs_secuencias ORDER by gs_proyecto, gs_lote")
        productos2 = self.cursor.fetchall()
        self.conexion.close()
        return productos2
    def seleccionar_fila(self, event):
        global gproye
        fila = self.tabla.focus()
        valores = self.tabla.item(fila, "values")
        accions = [
            self.gs_id, self.gs_proceso, self.gs_proyecto,self.gs_lote, self.gs_fecha, self.gs_desc, self.gs_ctda, self.gs_can, self.gs_ffe, self.gs_ver
        ]
        for accion in accions:
            accion.delete(0, tk.END)
        for i, valor in enumerate(valores):
            if i < len(accions):
                accions[i].insert(0, valor)
        gproye=valores
        
        
        self.seleccionar_fila_Datos(gproye)
        return(gproye)
    def entrada(self):
        self.gs_id = tk.Entry(self.marco)
        self.gs_id.place(x=30, y=3,width=25)
        self.gs_proceso = Combobox(self.marco, values=["Fabricacion-Entrada","Fabricacion-Proceso","Fabricacion-Salida","Venta-Planificada","Venta-Estimada", "Venta-Concretada","Compra-Planificada","Compra-Eventual","Diseño","Libre","Domingo"])
        self.gs_proceso.place(x=75, y=3,width=160)
        self.gs_proyecto = tk.Entry(self.marco)
        self.gs_proyecto.place(x=240, y=3,width=175)
        self.gs_lote = tk.Entry(self.marco)
        self.gs_lote.place(x=425, y=3,width=100)  
        self.gs_fecha = DateEntry(self.marco, date_pattern='yyyy-mm-dd', width=18)
        self.gs_fecha.place(x=555, y=3,width=82)
        self.gs_fecha.set_date(date.today())
        self.gs_desc= tk.Entry(self.marco)
        self.gs_desc.place(x=650, y=3,width=360)
        self.gs_ctda = tk.Entry(self.marco)
        self.gs_ctda.place(x=1035, y=3,width=40)
        self.gs_can = tk.Entry(self.marco)
        self.gs_can.place(x=1100, y=3,width=35)
        self.gs_ffe = tk.Entry(self.marco)
        self.gs_ffe.place(x=1160, y=3,width=35)
        self.gs_ver = Combobox(self.marco, values=["SI","NO"])
        self.gs_ver.place(x=1220, y=3,width=45)
    def listado(self,whe_gs,sor_gs):
        self.tabla.tag_configure('alerta', background='red', foreground='white')
        self.tabla.tag_configure('alerta2', background='blue', foreground='white')
        self.tabla.tag_configure('alerta3', background='light sky blue', foreground='black')
        self.whe_gs= " WHERE gs_can=0 "
        productos = gs_sql(whe_gs,sor_gs)
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for producto in productos:
            match ((producto[1])[:5]):
                case 'Libre':
                    self.tabla.insert("", tk.END, values=producto, tags=('alerta3',))
                case 'Compr':
                    self.tabla.insert("", tk.END, values=producto, tags=('alerta',))
                case 'Domin':
                    self.tabla.insert("", tk.END, values=producto, tags=('alerta2',))
                case _:
                    self.tabla.insert("", tk.END, values=producto)  
        return()
    def rTabla(self):
        self.tabla = ttk.Treeview(self.marco, columns=("gs_id", "gs_proceso","gs_proyecto", "gs_lote","gs_fecha","gs_desc","gs_ctda","gs_can", "gs_ffe","gs_ver"), show="headings")
        self.tabla.place(x=2, y=25, width=1276, height=720)      
        self.tabla.heading(0, text="id")
        self.tabla.column("gs_id", width=20, anchor="e")  # Derecha     
        self.tabla.heading(1, text="Proceso")
        self.tabla.column("gs_proceso", width=115, anchor="w")  # Derecha        
        self.tabla.heading(2, text="Proyecto")
        self.tabla.column("gs_proyecto", width=130, anchor="w")  # Derecha  
        self.tabla.heading(3, text="Sub-Proyecto")
        self.tabla.column("gs_lote", width=60, anchor="w")  # Derecha
        self.tabla.heading(4, text="Fecha")
        self.tabla.column("gs_fecha", width=80, anchor="center")  # Derecha
        self.tabla.heading(5, text="Actividad a desarrollar")
        self.tabla.column("gs_desc", width=300, anchor="w")  # Derecha
        self.tabla.heading(6, text="Ctdad")   
        self.tabla.column("gs_ctda", width=40, anchor="e")  # Derecha
        self.tabla.heading(7, text="Can")   
        self.tabla.column("gs_can", width=10, anchor="e")  # Derecha
        self.tabla.heading(8, text="FFE")   
        self.tabla.column("gs_ffe", width=10, anchor="e")  # Derecha
        self.tabla.heading(9, text="Ver")   
        self.tabla.column("gs_ver", width=10, anchor="e")  # Derecha
        self.tabla.bind("<ButtonRelease-1>", self.seleccionar_fila)
    def Linea_Vacio():
        if not valores:
            return  # Si no hay valores, salir
    def eliminar_producto(self,whe_gs,sor_gs):
        self.conexion = sqlite3.connect("CirDesMx.db")
        self.cursor = self.conexion.cursor()
        item = self.tabla.selection()
        if item:
            id_producto = self.tabla.item(item)["values"][0]
            try:
                self.cursor.execute("DELETE FROM gs_secuencias WHERE gs_id = ?", (id_producto,))
                self.conexion.commit()
                messagebox.showinfo("Eliminado", "Producto eliminado")
            except Exception as e:
                self.conexion.rollback()  # ← importante para evitar transacciones bloqueadas
                messagebox.showerror("Error", f"No se pudo eliminar: {e}")
        rehajustar()
        self.consultar(whe_gs,sor_gs)
    def modificar_secuencia(self,gproye):
        gproye=[self.gs_id.get(),
        self.gs_proceso.get(),
        self.gs_proyecto.get(),
        self.gs_lote.get(),
        self.gs_fecha.get(),
        self.gs_desc.get(),
        self.gs_ctda.get(),
        self.gs_can.get(),
        self.gs_ffe.get(),
        self.gs_ver.get()]
        self.conexion = sqlite3.connect("CirDesMx.db")
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""
            UPDATE gs_secuencias
            SET gs_proceso=?,gs_proyecto=?,gs_lote=?,gs_fecha=?,gs_desc=?,gs_ctda=?,gs_can=?,gs_ffe=?,gs_ver=?
            WHERE gs_id = ?
        """, (gproye[1],gproye[2],gproye[3],gproye[4],gproye[5],gproye[6],gproye[7],gproye[8],gproye[9],gproye[0]
        ))            
        self.conexion.commit()
        messagebox.showinfo("Éxito", "Producto modificado correctamente.")
        self.conexion.close()
    def modificar_entrada(self, filt2,gproye):
        AE0=self.gs_id.get()
        AE1=self.gs_proceso.get()
        AE2=self.gs_proyecto.get()
        AE3=self.gs_lote.get()
        AE4=self.gs_fecha.get()
        AE5=self.gs_desc.get()
        AE6=self.gs_ctda.get()
        AE7=self.gs_can.get()
        AE8=self.gs_ffe.get()
        AE9=self.gs_ver.get()
        gproye=(AE0,AE1,AE2,AE3,AE4,AE5,AE6,AE7,AE8,AE9)
        self.modificar_secuencia(gproye)
        sor_gs=" ORDER by gs_fecha"
        whe_gs=''
        self.consultar(whe_gs,sor_gs)
    def agregar_entrada(self, whe_gs,gproye):
        AE0=self.gs_id.get()
        AE1=self.gs_proceso.get()
        AE2=self.gs_proyecto.get()
        AE3=self.gs_lote.get()
        AE4=self.gs_fecha.get()
        AE5=self.gs_desc.get()
        AE6=self.gs_ctda.get()
        AE7=self.gs_can.get()
        AE8=self.gs_ffe.get()
        gproye=(AE0,AE1,AE2,AE3,AE4,AE5,AE6,AE7,AE8)
        self.agregar_secuencia(gproye)
        sor_gs=" ORDER by gs_fecha"
        rehajustar()
        self.consultar(whe_gs,sor_gs)
    def agregar_secuencia(self, gproye):
        conexion = sqlite3.connect("CirDesMx.db")
        cursor = conexion.cursor()
        cursor.execute("""
        INSERT INTO gs_secuencias (gs_proceso,gs_proyecto,gs_lote, gs_fecha,gs_desc,gs_ctda, gs_can,gs_ffe)
            VALUES (?, ?, ?, ?, ?,?,?,?)
        """, (
            gproye[1],
            gproye[2],
            gproye[3],
            gproye[4],
            gproye[5],
            gproye[6],
            gproye[7],  
            gproye[8]
        ))   
        conexion.commit()
        conexion.close()        
    def consultar(self,whe_gs,sor_gs):
        messagebox.showinfo(whe_gs,sor_gs)
        self.listado(whe_gs,sor_gs) 
    def seleccionar_fila_Datos(self, gproye):
        self.marco2 = tk.Frame(width=916, height=27, bg="green")
        self.marco2.place(x=350, y=1)
        Ref2=gproye[2]
        Ref3=gproye[3]
        LisDic=cargar_entradas()
        cLisDic=len(LisDic)
        for i in range(0,cLisDic):
            Reg=LisDic[i]
            E0=Reg[0] # Proyecto
            E1=Reg[1] # Lote
            E2=int(Reg[2]) # Entrada
            E3=int(Reg[3]) # Salida
            E4=int(Reg[4]) # Venta
            if Ref2==E0 and Ref3==E1:                               
                texto = 'Proyecto/SubProyecto:  ' + str(E0)+" / "+str(E1)
                tk.Label(self.marco2,text=texto).place(x=5, y=3)
                texto = 'Entradas: ' + str(E2)
                tk.Label(self.marco2,text=texto).place(x=400, y=3)
                texto6 = 'Salida: '+ str(E3)
                tk.Label(self.marco2,text=texto6).place(x=500, y=3)
                texto7 = 'Venta: '+ str(E4)
                tk.Label(self.marco2,text=texto7).place(x=590, y=3)
                ED=int(E3-E4)
                EF=int(E2-E3)
                textoF = 'En Fabricacion: ' +str(EF)
                tk.Label(self.marco2,text=textoF).place(x=660, y=3)
                textoD = 'Disponible: '+str(ED)
                tk.Label(self.marco2,text=textoD).place(x=780, y=3)
# SISTEMA DE MENUES ==============================
    def Aj1(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_proceso"
        self.consultar(whe_gs,sor_gs)
    def Aj2(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_proyecto"
        self.consultar(whe_gs,sor_gs)
    def Aj3(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_lote"
        self.consultar(whe_gs,sor_gs)
    def Aj4(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_proyecto, gs_lote"
        self.consultar(whe_gs,sor_gs)       
    def Aj5(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_fecha DESC"
        self.consultar(whe_gs,sor_gs)
    def Aj6(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_can"
        self.consultar(whe_gs,sor_gs)
    def Aj7(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_ffe"
        self.consultar(whe_gs,sor_gs)   
    def Aj8(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_ver DESC"
        self.consultar(whe_gs,sor_gs)   
    def Aj9(self,whe_gs,sor_gs):
        sor_gs=" ORDER by gs_id DESC"
        self.consultar(whe_gs,sor_gs)  

    def Bj1(self,whe_gs,sor_gs):
        sor_gs= " ORDER by gs_id DESC"
        gs_sql_up_0(sor_gs)
        self.consultar(whe_gs,sor_gs)  
    def Bj2(self,whe_gs,sor_gs,gproye):
        vGP=gproye[1]
        whe_gs= " WHERE gs_proceso= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)     
    def Bj3(self,whe_gs,sor_gs,gproye):
        whe_gs= " WHERE gs_proceso LIKE 'Fabrica%'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
    def Bj4(self,whe_gs,sor_gs,gproye):
        vGP=gproye[2]
        whe_gs= " WHERE gs_proyecto= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
    def Bj5(self,whe_gs,sor_gs,gproye):
        vGP=gproye[3]
        whe_gs= " WHERE gs_lote= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
    def Bj6(self,whe_gs,sor_gs,gproye):
        vGP=gproye[2]
        whe_gs= " WHERE gs_proyecto= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
        vGP=gproye[3]
        whe_gs= " WHERE gs_lote= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
    def Bj7(self,whe_gs,sor_gs,gproye):
        vGP=gproye[4]
        whe_gs= " WHERE gs_fecha = '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
    def Bj8(self,whe_gs,sor_gs,gproye):  # Fecha Actual en Adelante
        fecha_actual = date.today()
        vGP = fecha_actual.strftime("%Y-%m-%d")
        whe_gs = f" WHERE gs_fecha >= '{vGP}'"
        self.consultar(whe_gs,sor_gs) 
    def Bj9(self,whe_gs,sor_gs,gproye):
        vGP=gproye[4]
        whe_gs= " WHERE gs_fecha >= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
    def Bj10(self,whe_gs,sor_gs,gproye):
        vGP=gproye[7]
        whe_gs= " WHERE gs_can!= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
    def Bj11(self,whe_gs,sor_gs,gproye):
        vGP=gproye[8]
        whe_gs= " WHERE gs_ffe!= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)
    def Bj12(self,whe_gs,sor_gs,gproye):
        vGP=gproye[9]
        whe_gs= " WHERE gs_ver= '" +vGP+"'"
        gs_sql_up_1(whe_gs)
        self.consultar(whe_gs,sor_gs)








# Seleccionar la Fila del Dato de los Proyectos  ==========================
   


    

    def Balance_Placas(self): # Envia a Web la cantidad de placas disponibles.
        messagebox.showinfo("Web", "Balance de placas")
        exis_placas()

        
    def abrir_principal(self):
        self.destroy()
        ventana_inicial()
    def abrir_stock(self):
        self.destroy()
        ventana_stock()
    def abrir_proyecto(self):
        self.destroy()
        ventana_proyecto()
    def abrir_registros(self):
        self.destroy()
        ventana_registro()     
        
        
        





# Cerrar Conexion =====
    def cerrar_conexion(self):
        if self.conexion:
            self.cursor.close()
            self.conexion.close()
# ===================================================================================
    def volver_inicial(self):
        self.destroy()
        ventana_inicial()


        
    
# Ejecutar la aplicación
if __name__ == "__main__":
    app = ventana_secuencia()
    app.mainloop()

