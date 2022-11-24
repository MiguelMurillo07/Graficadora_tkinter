from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from numpy import pi,sin,cos,tan
N=100

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará..")
    ventana_principal.destroy()

def borrar():
  messagebox.showinfo("Cálculo v1.0", "Los datos a continuación serán borrados...")
  a.set("")
  b.set("")
  c.set("")
  d.set("")
  frame_operaciones.delete("1.0","end")


  
#Funcion Lineal
def calcularlineal(m,b,x):
  return int(m.get())*x+int(b.get())
def mostrar_lineal():
  y= calcularlineal(m,b,x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Función Lineal: y = mx + b")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 
def funcion_lineal():
  
  
  # Etiqueta para m
  lb_x = Label(frame_operaciones, text = "m =  ")
  lb_x.config(bg="red", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # Entry para m
  entry_x = Entry(frame_operaciones, textvariable=m)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # Etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="red", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  # Entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)

  # Etiqueta para c
  lb_x = Label(frame_operaciones, text = "   ")
  lb_x.config(bg="red", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)

  # Entry para c
  lb_x = Label(frame_operaciones, text = "     ")
  lb_x.config(bg="red", fg="blue", font=("Arial",16))
  lb_x.place(x=135,y=100,width=115, height=30)

  # Etiqueta para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="red", fg="blue", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # Entry para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="red", fg="blue", font=("Arial",16))
  lb_x.place(x=350,y=20,width=115, height=30)
  
  #Botón Cuadrática
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_lineal)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)

# Función Cuadrática
def calcular_cuadratica(a,x,b,c):
    return int(a.get())*x**2+int(b.get())*x+int(c.get())
def funcion_cuadratica():
  # Etiqueta para a
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="green", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # Entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # Etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="green", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  # Entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)
  # Etiqueta para c
  lb_x = Label(frame_operaciones, text = "c =  ")
  lb_x.config(bg="green", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)
  # Entry para c
  entry_x = Entry(frame_operaciones, textvariable=c)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=100,width=115, height=30)
  # Etiqueta para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="green", fg="blue", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # Entry para d
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="green", fg="blue", font=("Arial",16))
  lb_x.place(x=350,y=20,width=115, height=30)
  
  #Botón calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_cuadratica)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)

def mostrar_cuadratica():
  y=calcular_cuadratica(a,x,b,c)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Función Cuadrática: ax² + bx + c = 0")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 
def calcular_cubica(a,x,b,c,d):
    return int(a.get())*x**3+int(b.get())*x**2+int(c.get())*x+int(d.get())
def mostrar_cubica():
  y=calcular_cubica(a,x,b,c,d)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Funcion Cúbica: ax³ + bx² + c + d")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 

# Función Cúbica

def funcion_cubica():
  
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # Entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # Etiqueta para b
  lb_x = Label(frame_operaciones, text = "b =  ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  # Entry para b
  entry_x = Entry(frame_operaciones, textvariable=b)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=60,width=115, height=30)
  # Etiqueta para c
  lb_x = Label(frame_operaciones, text = "c =  ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)
  # Entry para c
  entry_x = Entry(frame_operaciones, textvariable=c)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=100,width=115, height=30)

  # Etiqueta para d
  lb_x = Label(frame_operaciones, text = "d =  ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # Entry para d
  entry_x = Entry(frame_operaciones, textvariable=d)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=350,y=20,width=115, height=30)

  # Botón Calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_cubica)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)


# Función Exponencial

def calcular_expotencial(x,a):
  return int(a.get())**x
def funcion_expotencial():
  
  lb_x = Label(frame_operaciones, text = "a =  ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # Entry para a
  entry_x = Entry(frame_operaciones, textvariable=a)
  entry_x.config(font=("Arial",20), justify=LEFT, fg="blue")
  entry_x.focus_set()
  entry_x.place(x=135,y=20,width=115, height=30)
  # Etiqueta para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  # Entry para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=135,y=60,width=115, height=30)
  # Etiqueta para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)
  # Entry para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=135,y=100,width=115, height=30)
  # Etiqueta para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # Entry para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="pink", fg="blue", font=("Arial",16))
  lb_x.place(x=350,y=20,width=115, height=30)
  #Botón Calcular
  bt_cuadratica = Button(frame_operaciones, text="Calcular", command=mostrar_expotencial)
  bt_cuadratica.place(x=50,y=150, width=100, height=30)
def mostrar_expotencial():
  y=calcular_expotencial(x,a)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Función Exponencial: f(x) = b**x")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show() 
  
#Función Logaritmo

def funcion_logaritmica(x):
  return np.log(x)
def mostrar_logaritmo():
  y=funcion_logaritmica(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Función Logarítmica: f(x)=loga(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()

# Función Trigonométrica

def funcion_trigonometrica():
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=20, width=115, height=30)
  # Entry para a
  lb_x = Label(frame_operaciones, text = "        ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=135,y=20,width=115, height=30)
  
  # Etiqueta para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=60, width=115, height=30)
  # Entry para b
  lb_x = Label(frame_operaciones, text = "          ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=135,y=60,width=115, height=30)
  # Etiqueta para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=10, y=100, width=115, height=30)
  # Entry para c
  lb_x = Label(frame_operaciones, text = "           ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=135,y=100,width=115, height=30)
  # Etiqueta para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=250, y=20, width=115, height=30)
  # Entry para d
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=350,y=20,width=115, height=30)
  # Botón Calcular
  lb_x = Label(frame_operaciones, text = "            ")
  lb_x.config(bg="brown", fg="blue", font=("Arial",16))
  lb_x.place(x=50,y=150, width=100, height=30)

  #Botón Seno
  
  bt_seno = Button(frame_operaciones, text="sen(x)", command=mostrar_seno)
  bt_seno.place(x=50,y=150, width=100, height=30)

  bt_coseno = Button(frame_operaciones, text="cos(x)", command=mostrar_coseno)
  bt_coseno.place(x=180,y=150, width=100, height=30)

  bt_tangente= Button(frame_operaciones, text="tan(x)", command=mostrar_tangente)
  bt_tangente.place(x=350,y=150, width=100, height=30)
  return bt_coseno.destroy
  
def funcion_trigonometricaseno(x):
  return sin(x)
def mostrar_seno():
  y=funcion_trigonometricaseno(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Función Sen(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
  
def funcion_trigonometricacoseno(x):
  return cos(x)
def mostrar_coseno():
  y=funcion_trigonometricacoseno(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Función Cos(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
def funcion_trigonometricatangente(x):
  return tan(x)
def mostrar_tangente():
  y=funcion_trigonometricatangente(x)
  plt.plot(x,y,color="r")
  plt.xlabel("x")
  plt.ylabel("y")
  plt.title("Función Tan(x)")
  plt.grid()
  plt.axhline(y=0,color="b")
  plt.axvline(x=0, color="b")
  plt.show()
    
ventana_principal = Tk()
c= StringVar()
a = StringVar()
b = StringVar()
m = StringVar()
d = StringVar()
x= np.linspace(-10,10, num=N)


# titulo de la ventana
ventana_principal.title("Funciones Matemáticas")

# tamañan de la ventana
ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

# color de fondo de la ventana
ventana_principal.config(bg= "purple")

# Etiqueta para el titulo de la app
titulo = Label(ventana_principal, text= "Graficadora de Funciones")
titulo.config(bg="LightBlue4", fg="white", font=("Arial",18))
titulo.place(x=50,y=10, width=400, height=40)
# Botón Lineal
bt_lineal = Button(ventana_principal, text="Lineal", command=funcion_lineal)
bt_lineal.place(x=200,y=60, width=100, height=30)

#Botón Cuadrática
bt_cuadratica = Button(ventana_principal, text="Cuadrática", command=funcion_cuadratica)
bt_cuadratica.place(x=200,y=95, width=100, height=30)

#Botón Cúbica
bt_cubica= Button(ventana_principal, text="Cúbica", command=funcion_cubica)
bt_cubica.place(x=200,y=130, width=100, height=30)

#Botón Expotencial
bt_expotencial= Button(ventana_principal, text="Exponencial", command=funcion_expotencial)
bt_expotencial.place(x=200,y=165, width=100, height=30)

#Botón logaritmo
bt_logaritmo= Button(ventana_principal, text="Logarítmica", command=mostrar_logaritmo)
bt_logaritmo.place(x=200,y=200, width=100, height=30)

#Botón Trigonométrica
bt_trigonometrica= Button(ventana_principal, text="Trigonométrica", command=funcion_trigonometrica)
bt_trigonometrica.place(x=200,y=235, width=100, height=30)

# ------------------------
# Frame Operaciones
# ------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="goldenrod", width=480, height=190)
frame_operaciones.place(x=10,y=300)


# Boton Borrar
bt_borrar = Button(ventana_principal, text="Borrar", command=borrar)
bt_borrar.place(x=40, y=250, width=100, height=30)



# Botón Salir
bt_salir = Button(ventana_principal, text="Salir", command=salir)
bt_salir.place(x=370, y=250, width=100,height=30)


ventana_principal.mainloop()
