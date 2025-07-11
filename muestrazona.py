from tkinter import Label, Button, Entry
from tkinter import ttk, messagebox
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from Conexion import *
from PIL import Image, ImageTk
import mysql.connector
import re
from pathlib import Path

cnn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="colegio")
cur = cnn.cursor()

vent = Tk()
vent.title("Registro y Control de Datos de los Estudiantes")
vent.geometry("800x600+600+100")
vent.wm_resizable(width=None, height=None)
vent.group()
vent.minsize(width=400,height=100)
vent.maxsize(width=800, height=600)
vent.configure(bg="white")
vent.group()

icono = tk.PhotoImage(file="imagenes/icono.png")
# Establecerlo como ícono de la ventana.
vent.iconphoto(True, icono)

id = InterruptedError()
dni = IntVar()
nombres = StringVar()
txtApe = StringVar()
apellidos = StringVar()
sexo = StringVar()
txtMsj = StringVar()
tvEst = StringVar()
txtDni = IntVar()
lista_sexo = StringVar()

global anc, alto
#------------ Foto de la Escuela ------------#
cuadro0 = tk.LabelFrame(vent,text="", 
   relief=tk.GROOVE,
   border=7,
   height=150,
   width=180,
   bg="green")
cuadro0.pack(padx=2, pady=2)
cuadro0.place(x=365, y=6)
anc = 125
alto = 140
#####---------------------------------------####
def buscar_archivo(nombre_archivo, directorio):
    directorio_path = Path(directorio)
    for archivo in directorio_path.rglob(nombre_archivo):
        return archivo
    return None
#anc = 125
#alto = 140
resultado = buscar_archivo('listar.png', 'fotos_alumnos')
if resultado:
  #print("Archivo encontrado: ",resultado)
  imagen_pil = Image.open('imagenes/listar.png')
  imagen_resize = imagen_pil.resize((anc, alto))
  #imagen_resize = imagen_pil.resize((125, 140))
  imagen_tk = ImageTk.PhotoImage(imagen_resize)
  #---------------------------------------------#
  lblfotos = tk.Label(cuadro0, text="", width=165)
  lblfotos.config(image = imagen_tk,
      compound=LEFT,
      bg="white", 
  border=1, padx=1, pady=1)
  lblfotos.image = imagen_tk
  lblfotos.pack()
  lblfotos.place(x=370, y=10)
else:
  #anc = 125
  #alto = 140
  #print("Archivo no encontrado.")
  ext = ".jpg"
  veo = "no"+ext
  carpeta = "fotos_alumnos/"
  fot = carpeta+veo
  imagen_pil = Image.open(fot)
  #imagen_pil = Image.open('fotos_alumnos/no.jpg')
  imagen_resize = imagen_pil.resize((anc, alto))
  imagen_tk = ImageTk.PhotoImage(imagen_resize)

  lblfotos = tk.Label(vent, text="", width=165)
  lblfotos.config(image = imagen_tk,compound=LEFT, 
  border=1, padx=1, pady=1)
  lblfotos.image = imagen_tk
  lblfotos.pack()
  lblfotos.place(x=370, y=10)

cuadro1 = tk.LabelFrame(vent,text="", 
   relief=tk.GROOVE,
   border=2,
   height=250,
   width=90,
   bg="lightblue")
cuadro1.pack(padx=90, pady=120)
cuadro1.place(x=13, y=10)

### Label & Estry ...
lblDni = tk.Label(cuadro1, text = "      DNI:", 
    font="consolas 10",
    anchor="w",
    padx=5, pady=5,
    bg="lightblue",
    width=10, height=1)
    #justify="left")
lblDni.place(x=13, y=20)
lblDni.pack(side=tk.LEFT)

txtDni = tk.Entry(cuadro1, width=30, justify=tk.RIGHT, 
        relief=tk.SUNKEN, bd=3,
        textvariable=dni)
txtDni.place(x=10, y=20)
txtDni.pack(side=tk.RIGHT, padx=10, pady=10)

cuadro2 = tk.LabelFrame(vent,text="", 
   relief=tk.GROOVE,
   border=2,
   height=250,
   width=90,
   bg="#F7A18B")
cuadro2.pack(padx=90, pady=120)
cuadro2.place(x=13, y=50)

lblNom = tk.Label(cuadro2, text="  Nombres:", 
    font="consolas 10",
    anchor="w",
    padx=5, pady=5,
    bg="#F7A18B", #<<<---- #F7A18B
    width=10, height=1)
    #justify="left")
lblNom.place(x=10, y=50)
lblNom.pack(side=tk.LEFT)

txtNom = tk.Entry(cuadro2, width=30,  
        relief=tk.SUNKEN, bd=3,
        textvariable=nombres)
txtNom.place(x=10, y=50)
txtNom.pack(side=tk.RIGHT, padx=10, pady=10)

cuadro3 = tk.LabelFrame(vent,text="", 
   relief=tk.GROOVE,
   border=2,
   height=250,
   width=140,
   bg="#EBCB61")
cuadro3.pack(padx=60, pady=120)
cuadro3.place(x=13, y=97)

lblApe = tk.Label(cuadro3, text="Apellidos:", 
    font="consolas 10",
    anchor="w",
    padx=2, pady=5,
    bg="#EBCB61", 
    width=12, height=1)
    #justify="left")
lblApe.place(x=30, y=127)
lblApe.pack(side=tk.LEFT)

txtApe = tk.Entry(cuadro3, width=30,  
        relief=tk.SUNKEN, bd=3,
        textvariable=apellidos)
txtApe.place(x=30, y=127)
txtApe.pack(side=tk.RIGHT, padx=6, pady=10)

cuadro13 = tk.LabelFrame(vent,text="", 
   relief=tk.GROOVE,
   border=2,
   height=150,
   width=490,
   bg="#B3E0D5")
cuadro13.pack(padx=150, pady=420)
cuadro13.place(x=13, y=143)

lblSexo = tk.Label(cuadro13, text="     Sexo:", 
    font="consolas 10",
    anchor="w",
    padx=2, pady=5,
    bg="#B3E0D5",
    width=12, height=1)
    #justify="left")
lblSexo.place(x=30, y=168)
lblSexo.pack(side=tk.LEFT)

sexo = tk.StringVar()
lista_sexo = ttk.Combobox(cuadro13,
   font="consolas 10",
   width=16,
   values=["Masculino","Femenino"],
   state="readonly",
   textvariable=sexo)
lista_sexo.set("Masculino")
lista_sexo.place(x=97, y=168)
lista_sexo.pack(side=tk.RIGHT, padx=32, pady=10)

### Tabla de la Lista de Estudiantes...
cuadro4 = tk.LabelFrame(vent,text="Lista de Estudiantes", 
        width=660, height=150, borderwidth = 0, padx=5, pady=5)
cuadro4.place(x=15, y=240)
#<<<------------ Inicio del Treeview ------------>>#

tvEst = ttk.Treeview(cuadro4, columns=("DNI", "Nombres", "Apellidos", "Sexo"))
tvEst.place(x=13, y=15)

tvEst["columns"]=("Id", "DNI", "Nombres", "Apellidos", "Sexo",)
tvEst.column("# 0", width=0, stretch=NO)                  
tvEst.column("Id", width=50, anchor=CENTER)                  
tvEst.column("DNI", width=100, anchor=CENTER)                  
tvEst.column("Nombres", width=180, anchor=CENTER)                  
tvEst.column("Apellidos", width=180, anchor=CENTER)                  
tvEst.column("Sexo", width=80, anchor=CENTER)
                  
# Crear el Treeview con el estilo personalizado

###--->>> ENCABEZADO DEL TREEVIEW ---<<< ###
tvEst.heading("#0", text="")                  
tvEst.heading("#1", text="Id", anchor=CENTER)                  
tvEst.heading("#2", text="DNI", anchor=CENTER)                  
tvEst.heading("#3", text="Nombres", anchor=CENTER)                  
tvEst.heading("#4", text="Apellidos", anchor=CENTER)                  
tvEst.heading("#5", text="Sexo", anchor=CENTER)   

tvEst.pack(side='right', fill="both", expand=True)
tvEst.bind("<<TreeviewSelect>>", lambda event: on_treeview_select(event))
tvEst.bind("<Double-1>",lambda event: onDoubleClick(event))
tvEst['selectmode'] = 'browse'
tvEst.pack(side='right', fill="both", expand=True)

#----------------- INSTRUCCIÓN DE MONTAJE DEL SCHROLL VERTICAL -----------------#
# Crear un Scrollbar vertical
# add a vertical scrollbar
scrollbar = tk.Scrollbar(cuadro4)
#### Coloco el Schroll y el Texto...
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tvEst.pack(side=tk.LEFT, fill=tk.Y)
#### Configuramos el Widgets...
### Indicamos que modificará a Texto en su Schroll(Y) usando
### el método "yview"
scrollbar.config(command=tvEst.yview)
### Asociamos con el Schroll para poder colocarlo en la
### posición invocada...
tvEst.config(yscrollcommand=scrollbar.set)

txtDni.focus() #<<<--- Colocandoel Foco en el campo Número de Cédula...

#----------------- FIN INSTRUCCIÓN DE MONTAJE DEL SCHROLL -----------------#
# Insertar datos con colores alternados
tvEst.tag_configure("even", background="#cddd83")  # Gris claro
tvEst.tag_configure("odd", background="#ffffff")   # Blanco
cnn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="colegio")
cur = cnn.cursor()
sql = "SELECT * FROM estudiantes ORDER BY DNI"
cur.execute(sql)
dat = cur.fetchall()
cur.close()
cnn.close()
p=0
for i in dat:
  #print(" p: ", p) 
  ver = (p % 2)
  #print("ver: ", ver)
  if ver ==0:
    tvEst.insert("", "end", values=(i), tags=("even",))
  else:
    tvEst.insert("", "end", values=(i), tags=("odd",))
  p = p+1

  #----------- ETIQUETA PARA OTROS MENSAJES -----------------#
  cuadro5 = tk.LabelFrame(vent,text="", 
        width=10, height=5, 
        bg="white", borderwidth = 0, 
           padx=2, pady=10)
  cuadro5.place(x=200, y=530)

  etiqueta = tk.Label(cuadro5, fg="Red", bg="white", text="", width=50)
  etiqueta.place(x=280, y=530, anchor=CENTER)
  etiqueta.pack()

  etiqueta.configure(text="Total : " + str(len(tvEst.get_children())) + " Reg.")
  etiqueta.pack()

######--->> FUNCIONES <<---######

def buscar_archivo(nombre_archivo, directorio):
    directorio_path = Path(directorio)
    for archivo in directorio_path.rglob(nombre_archivo):
        return archivo
    return None

def on_treeview_select(event):
  #---> Se ejecuta cuando una fila recibe un Doble Click...
  # Obtener el elemento seleccionado
  item_seleccionado = tvEst.focus()
  # Obtener el valor del ID (o cualquier columna)
  id_seleccionado = tvEst.item(item_seleccionado, 'values')[0]
  txtDni = tvEst.item(item_seleccionado, 'values')[1]
  #id_seleccionado = tvEst.item(item_seleccionado, 'values')[2]
  #id_seleccionado = tvEst.item(item_seleccionado, 'values')[3]
  #id_seleccionado = tvEst.item(item_seleccionado, 'values')[4]
  #print(f"ID seleccionado: {id_seleccionado}")
  #print(f"DNI seleccionado: {txtDni}")
  cnn = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="colegio")
  cur = cnn.cursor()
  valor = txtDni
  cur.execute("SELECT * FROM estudiantes WHERE DNI = %s", (txtDni,))
  dat = cur.fetchall()
  for i in dat:
      #print(i[0],i[1],i[2],i[3],i[4])
  
    recibo = i[1]
  #print("recibo", i[1])
  ext = ".*"
  veo = str(recibo) + ".jpg"
  carpeta = "fotos_alumnos/"
  fto = carpeta + veo 

  resultado = buscar_archivo(veo, carpeta)
  if resultado:
      #print("Archivo encontrado: ",resultado)
      imagen_pil = Image.open(fto)
      imagen_resize = imagen_pil.resize((anc, alto))
      imagen_tk = ImageTk.PhotoImage(imagen_resize)

      lblfotos = tk.Label(vent, text="", width=165)
      lblfotos.config(image = imagen_tk,compound=LEFT, 
            border=1, padx=5, pady=5)
      lblfotos.image = imagen_tk
      lblfotos.pack()
      lblfotos.place(x=370, y=10)
  else:
      #print("Archivo no encontrado.")
      #ext = ".*"
      veo = "no.jpg"
      fot = carpeta+veo
      imagen_pil = Image.open(fot)
      imagen_resize = imagen_pil.resize((anc, alto))
      imagen_tk = ImageTk.PhotoImage(imagen_resize)

      lblfotos = tk.Label(vent, text="", width=165)
      lblfotos.config(image = imagen_tk,compound=LEFT, 
            border=1, padx=5, pady=5)
      lblfotos.image = imagen_tk
      lblfotos.pack()
      lblfotos.place(x=370, y=10)

cur.close()
cnn.close()

def onDoubleClick(event):
  #---> Se ejecuta cuando una fila recibe un Doble Click...
  # Obtener el elemento seleccionado
  item_seleccionado = tvEst.focus()
  # Obtener el valor del ID (o cualquier columna)
  id_seleccionado = tvEst.item(item_seleccionado, 'values')[0]
  txtDni = tvEst.item(item_seleccionado, 'values')[1]
  #id_seleccionado = tvEst.item(item_seleccionado, 'values')[2]
  #id_seleccionado = tvEst.item(item_seleccionado, 'values')[3]
  #id_seleccionado = tvEst.item(item_seleccionado, 'values')[4]
  #print(f"ID seleccionado: {id_seleccionado}")
  #print(f"DNI seleccionado: {txtDni}")
  cnn = mysql.connector.connect(
    host="localhost", user="root", passwd="", database="colegio")
  cur = cnn.cursor()
  valor = txtDni
  cur.execute("SELECT * FROM estudiantes WHERE DNI = %s", (txtDni,))
  dat = cur.fetchall()
  for i in dat:
      #print(i[0],i[1],i[2],i[3],i[4])
      recibo = i[1]
  #print("recibo", i[1])
  ext = ".*"
  veo = str(recibo) + ".jpg"
  carpeta = "fotos_alumnos/"
  fto = carpeta + veo 

  resultado = buscar_archivo(veo, carpeta)
  if resultado:
      #print("Archivo encontrado: ",resultado)
      imagen_pil = Image.open(fto)
      imagen_resize = imagen_pil.resize((anc, alto))
      imagen_tk = ImageTk.PhotoImage(imagen_resize)

      lblfotos = tk.Label(vent, text="", width=165)
      lblfotos.config(image = imagen_tk,compound=LEFT, 
            border=1, padx=5, pady=5)
      lblfotos.image = imagen_tk
      lblfotos.pack()
      lblfotos.place(x=370, y=10)
  else:
      #print("Archivo no encontrado.")
      #ext = ".*"
      veo = "no.jpg"
      fot = carpeta+veo
      imagen_pil = Image.open(fot)
      imagen_resize = imagen_pil.resize((anc, alto))
      imagen_tk = ImageTk.PhotoImage(imagen_resize)

      lblfotos = tk.Label(vent, text="", width=165)
      lblfotos.config(image = imagen_tk,compound=LEFT, 
            border=1, padx=5, pady=5)
      lblfotos.image = imagen_tk
      lblfotos.pack()
      lblfotos.place(x=370, y=10)

cur.close()
cnn.close()
  
def limpiar():
  #print("Limpiando..")
  etiqueta["text"] = ""
  txtDni.delete(0, tk.END)
  txtNom.delete(0, tk.END)
  txtApe.delete(0, tk.END)
  etiqueta.configure(text="Total : " + str(len(tvEst.get_children())) + " Reg.")
  txtDni.focus()

def validar_input():
  # Valida si el texto ingresado es un número entero positivo.
  texto = txtDni.get()
  patron = r"^[1-9]\d*$"  # Expresión regular para enteros positivos
  if re.match(patron, texto):
     return True
  else:
    return False

def buscar():
  #validar_input(txtDni.get().lower())
  #print("Estoy entrando a Buscar...")
  busqueda = txtDni.get().lower()
  etiqueta.config(text="")
  # Ejemplo de uso del Patrón...
  patron = r"^[1-9]\d*$"  #<<-- Expresión regular para enteros positivos
  if re.match(patron, busqueda):
    valido = True
    etiqueta.config(text="Cédula Aceptada..!!", font=("consolas 10 bold"))
  else:
    valido = False
    etiqueta.config(text="Cédula No Válida", font=("consolas 10 bold"))
  #print("Válido: ", valido)
  ###--->> Mientras sea Verdadero el dato introducido...
  while valido == True:
    entrada = txtDni.get() #("Ingrese un número entero positivo: ")
    #print("Entrada válida:", entrada)
    for item in tvEst.get_children():
      # Obtener los valores de cada fila
      valores = tvEst.item(item, "values")
      # Verificar si el texto buscado está en alguno de los valores
      if any(busqueda in str(valor).lower() for valor in valores):
        # Seleccionar y enfocar el elemento encontrado
        tvEst.selection_set(item)
        tvEst.focus(item)
        etiqueta.config(text="Revise la Lista. El registro está Marcado", font=("consolas 10 bold"))
        txtDni.delete(0, tk.END)
        txtDni.focus()
        return
        #--- Fin del If any ---#
      else:
        # Si no se encuentra, mostrar un mensaje
        etiqueta.config(text="Registro No encontrado", font=("consolas 10 bold"))
        txtDni.focus()
        valido=False
    break
      #--- Fin del If de verificación ---#
  ###--- Fin de Buscar...

##############       
def modificar():
  #print("Eentré a Modificar..")
  item_selec = tvEst.focus()
  if (item_selec!=""):
    r = messagebox.askquestion("Desea Modificar", "este Registro ?")
    if (r == "yes"):
      valor = tvEst.item(item_selec, 'values')  # Obtiene los valores de la fila seleccionada
      if valor:  # Si hay valores, los coloca en los Entry
        txtDni.delete(0, tk.END)
        txtDni.insert(0, valor[1])
        
        txtNom.delete(0, tk.END)
        txtNom.insert(0, valor[2])

        txtApe.delete(0, tk.END)
        txtApe.insert(0, valor[3])

        lista_sexo.delete(0, tk.END)
        valor = tvEst.item(item_selec, 'values')[4]  # Obtener el valor Sexo, de la fila
        lista_sexo.set(valor)  # Asignar el valor al Combobox
        #print(valor)
  else:
      messagebox.showinfo("Si Desea Modificar:", "Seleccione un Registro..!!")  
      return
  pass

def actualizar_datos():
  #print ("Estoy en Actualizar Datos...")
  cnn = mysql.connector.connect(
   host="localhost", user="root", passwd="", database="colegio")
  cur = cnn.cursor()
  item_seleccionado = tvEst.focus()
  id_seleccionado = tvEst.item(item_seleccionado, 'values')[0]
  #print("Id_seleccionado: ", id_seleccionado)
  if (id_seleccionado):
    if  (txtDni.get()=="") or (txtNom.get() =="") or (txtApe.get()==""):
      messagebox.showerror("Error", "No puede Dejar Campos Vacíos..")
      return
    else:
      # Obtener el valor del ID (o cualquier columna)
      #id_seleccionado = tvEst.item(item_seleccionado, 'values')[0]
      #id = tvEst.item(item_seleccionado, 'values')[0]
      etiqueta.config(text="")
      #print(f"Id seleccionado: {id_seleccionado}")
      cnn = mysql.connector.connect(
       host="localhost", user="root", passwd="", database="colegio")
      cur = cnn.cursor()
      # Obtener nuevos valores
      dni = txtDni.get()
      #print("DNI: ", dni)
      nombres = txtNom.get()
      #print("Nombres: ", nombres)
      apellidos = txtApe.get()
      #print("Apellidos: ", apellidos)
      sexo = lista_sexo.get()
      #print("Id :", id_seleccionado, "DNI: ", dni, "Nombres: ", nombres, "Apellidos: ", apellidos, "Sexo: ", sexo)
      #---------->> Actualizar valores en el Treeview
      tvEst.item(item_seleccionado, values=(id_seleccionado,dni, nombres, apellidos, sexo))
      #lista = [dni, nombres, apellidos, sexo, id_seleccionado]
      sql = "UPDATE estudiantes SET DNI = '"+ dni +"', nombres = '" +nombres+"', apellidos = '"+apellidos+"', sexo = '"+ sexo +"' WHERE id ='"+id_seleccionado+"'"
      cur.execute(sql)
      cnn.commit()
      #print("Registro Modificado...")
      txtDni.delete(0, tk.END)
      txtNom.delete(0, tk.END)
      txtApe.delete(0, tk.END)
      etiqueta.configure(text="Total : " + str(len(tvEst.get_children())) + " Reg.")
      txtDni.focus()
      messagebox.showinfo("Modificación: ","  Exitosa..!!")
  else:
    messagebox.showwarning("Aviso", "Seleccione un Registro")
    return
###--->> Fin de actualizar_datos...

def recargar_datos():
  cnn = mysql.connector.connect(
  host="localhost", user="root", passwd="", database="colegio")
  cur = cnn.cursor()
  sql = "SELECT * FROM estudiantes ORDER BY id"
  cur.execute(sql)
  dat = cur.fetchall()
  cur.close()
  cnn.close()
  for i in dat:
    tvEst.insert("", "end", values=i)
    #print(" i: ", i)
    pass  
###--->> Fin de recargar_datos...

def eliminar():
  #print("Entrando a Eliminar..")
  #---> Se ejecuta cuando una fila recibe un Doble Click...
  # Obtener el elemento seleccionado
  item_seleccionado = tvEst.focus()
  if (item_seleccionado!=""):
    r = messagebox.askquestion("Desea Borrar", "este Registro ?")
    if  r == "yes":
      # Obtener el valor del ID (o cualquier columna)
      id_seleccionado = tvEst.item(item_seleccionado, 'values')[0]
      txtDni = tvEst.item(item_seleccionado, 'values')[1]
      #print(f"Id seleccionado: {txtDni}")
      cnn = mysql.connector.connect(
       host="localhost", user="root", passwd="", database="colegio")
      cur = cnn.cursor()
      #valor = txtDni
      for row in tvEst.get_children():
         tvEst.delete(row)
      cur.execute("DELETE FROM estudiantes WHERE DNI = %s", (txtDni,))
      cnn.commit()
      etiqueta.config(text="Dato Eliminado. Pulse Actualizar..!!")
      recargar_datos()
    else:
      #for i in dat:
      #    tvEst.insert
      #actualizar_datos()
      return
  else:
      messagebox.showinfo("Para Borrar:", "Seleccione un Registro..!!")  
      return
  #cur.close()
  #cnn.close()
###--->> Fin de eliminar...

def busc_pingreso():
  #print("Estoy entrando a Buscar...")
  busqueda = txtDni.get().lower()
  etiqueta.config(text="")
  # Ejemplo de uso del Patrón...
  patron = r"^[1-9]\d*$"  #<<-- Expresión regular para enteros positivos
  if re.match(patron, busqueda):
    valido = True
    etiqueta.config(text="Cédula Aceptada..!!", font=("consolas 10 bold"))
  else:
    valido = False
    etiqueta.config(text="Cédula No Válida", font=("consolas 10 bold"))
    #print("Válido: ", valido)
    return
  ###--->> Mientras sea Verdadero el dato introducido...
  while valido == True:
    entrada = txtDni.get() #("Ingrese un número entero positivo: ")
    #print("Entrada válida:", entrada)
    for item in tvEst.get_children():
      # Obtener los valores de cada fila
      valores = tvEst.item(item, "values")
      # Verificar si el texto buscado está en alguno de los valores
      if any(busqueda in str(valor).lower() for valor in valores):
        # Seleccionar y enfocar el elemento encontrado
        tvEst.selection_set(item)
        tvEst.focus(item)
        etiqueta.config(text="El registro Existe...", font=("consolas 10 bold"))
        txtDni.delete(0, tk.END)
        txtDni.focus()
        return
        #--- Fin del If any ---#
      else:
        return 
      #--- Fin del If de verificación ---#
  ###--- Fin de Buscar...
  #          
cnn = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="colegio")
cur = cnn.cursor()
sql= "ALTER TABLE estudiantes AUTO_INCREMENT = 1"
cur.execute(sql)
txtDni.delete(0,END)
txtDni.focus()

def agrega_nuevor():
  #print("Agregando..")
  if (txtDni.get() =="") or (txtNom.get() =="") or (txtApe.get() ==""):
    #print("LLene los Datos...")
    etiqueta.config(text="LLene los Datos..", font=("consolas 10 bold"))
    #txtDni.focus()
    return
  else:
    patron = r"^[1-9]\d*$"  #<<-- Expresión regular para enteros positivos
    if re.match(patron, txtDni.get()):
      valido = True
      cnn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="colegio")
      cur = cnn.cursor()
      sql= "SELECT * FROM estudiantes"
      list = (int(txtDni.get()))
      cur.execute(sql, list)
      resultado = cur.fetchall()
      for ss in resultado:
        #print("ss[1]: ",ss[1])
        if (list==ss[1]):
          etiqueta.config(text="Cédula Ya Existe..!!", font=("consolas 10 bold"))
          print("Cédula Ya Existe..!!", txtDni.get())
          return  
      #print("Cédula Aceptada..!!", txtDni.get())
      dni = txtDni.get()
      #print("dni: ", dni)
      nombres = txtNom.get()
      #print("nombres: ", nombres)
      apellidos = txtApe.get()
      #print("apellidos: ", apellidos)
      sexo = lista_sexo.get()
      #print("sexo: ", sexo)
      pass  
      #print("Voy a INSERT...")
      sql = "INSERT INTO estudiantes (DNI, nombres, apellidos, sexo) VALUES (%s, %s, %s, %s)"
      lista = (dni, nombres, apellidos, sexo)
      cur.execute(sql, lista)
      resu = cur.fetchone()
      #resultado = cur.rowcount() #<<<--- OJO SI FALLA. QUITAR...
      cnn.commit()
      cur.close()
      cnn.close()
      new_id = len(tvEst.get_children()) + 1
      tvEst.insert("", "end", values=(new_id, txtDni.get(), txtNom.get(), txtApe.get(), lista_sexo.get()))      
      etiqueta.config(text="Ingreso Satisfactorio..!!", font=("consolas 10 bold"))
      #print("Ingreso Satisfactorio..!!") 
      txtDni.delete(0,END)
      txtNom.delete(0,END)
      txtApe.delete(0,END)
      lista_sexo.set("Masculino")
      etiqueta.configure(text="Total : " + str(len(tvEst.get_children())) + " Reg.")

#----------------- MARCO DE LOS BOTONES -----------------#
#-----------------        ELIMINAR     ------------------#
imagen_pil = Image.open('imagenes/borrar.png') #<-- ELIMINAR
imagen_resize = imagen_pil.resize((20, 20))
imagen_tk = ImageTk.PhotoImage(imagen_resize)

btnLimp = tk.Button(vent, text="Borrar", 
    command = eliminar, width=70, height=20, fg="red", borderwidth=4)
btnLimp.config(image = imagen_tk,compound=LEFT, border=2, padx=1)
btnLimp.image = imagen_tk
btnLimp.pack()
btnLimp.place(x=15, y=510)

#----------------- ACTUALIZAR -----------------#
imagen_pil = Image.open('imagenes/listar.png') #<-- ELIMINAR
imagen_resize = imagen_pil.resize((20, 20))
imagen_tk = ImageTk.PhotoImage(imagen_resize)

btnLimp = tk.Button(vent, text="Actualizar", 
    command = actualizar_datos, width=80, height=20, fg="red", borderwidth=4)
btnLimp.config(image = imagen_tk,compound=LEFT, border=2, padx=1)
btnLimp.image = imagen_tk
btnLimp.pack()
btnLimp.place(x=115, y=510)

#----------------- MODIFICAR -----------------#
imagen_pil = Image.open('imagenes/modificar.png') #<-- ELIMINAR
imagen_resize = imagen_pil.resize((20, 20))
imagen_tk = ImageTk.PhotoImage(imagen_resize)

btnLimp = tk.Button(vent, text="Modificar", 
    command = modificar, width=75, height=20, borderwidth=4)
btnLimp.config(image = imagen_tk,compound=LEFT, border=2, padx=1)
btnLimp.image = imagen_tk
btnLimp.pack()
btnLimp.place(x=225, y=510)

#----------------- NUEVO -----------------#
imagen_pil = Image.open('imagenes/guardar.png')
imagen_resize = imagen_pil.resize((20, 20))
imagen_tk = ImageTk.PhotoImage(imagen_resize)

btnLimp = tk.Button(vent, text="Nuevo...", 
    command = agrega_nuevor, width=75, height=20, borderwidth=4)
btnLimp.config(image = imagen_tk,compound=LEFT, border=2, padx=1)
btnLimp.image = imagen_tk
btnLimp.pack()
btnLimp.place(x=334, y=510)

#----------------- BUSCAR -----------------#
imagen_pil = Image.open('imagenes/buscar.png')
imagen_resize = imagen_pil.resize((20, 20))
imagen_tk = ImageTk.PhotoImage(imagen_resize)

btnOjo = tk.Button(vent, text="Buscar", 
    command = buscar, width=75, height=20, borderwidth=4)
btnOjo.config(image = imagen_tk,compound=LEFT, border=2, padx=1)
btnOjo.image = imagen_tk
#btnOjo.pack()
btnOjo.place(x=442, y=510)

#----------------- LIMPIAR -----------------#
imagen_pil = Image.open('imagenes/limpiar.png')
imagen_resize = imagen_pil.resize((20, 20))
imagen_tk = ImageTk.PhotoImage(imagen_resize)

btnLimp = tk.Button(vent, text="Limpiar", 
    command = limpiar, width=75, height=20, borderwidth=4)
btnLimp.config(image = imagen_tk,compound=LEFT, border=2, padx=1)
btnLimp.image = imagen_tk
btnLimp.pack()
btnLimp.place(x=552, y=510)

vent.mainloop()

