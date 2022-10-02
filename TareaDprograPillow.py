#Saul Oswaldo Lopez Hernandez
#Naser Audeli Claros Rivera
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox
from tkinter import Tk, Button, Label, filedialog

#Creamos el def para cargar la imagen
def cargar():
    archivo=filedialog.askopenfilename()
    global imagen1
    imagen1=Image.open(archivo)
    imagenresiz2=imagen1.resize((250,250), Image.Resampling.LANCZOS)
    render2=ImageTk.PhotoImage(imagenresiz2)
    label2.configure(image=render2)
    label2.image=render2
    label2.place(x=50,y=60)
    
#Creamos los def que agregan los filtros a la imagen 
#Agrega filtro B/N
def filtro1():
    imagen2 = imagen1.convert("L")
    messagebox.showinfo('PIL','Se agrego el filtro B/N')
    imagen2.show()

#Agrega filtro Desenfocar
def filtro2():
    imagen2 = imagen1.filter(ImageFilter.GaussianBlur(radius=10))
    messagebox.showinfo('PIL','Se agrego el filtro Desenfocar')
    imagen2.show()

#Agrega filtro Contorno
def filtro3():
    imagen2 = imagen1.filter(ImageFilter.CONTOUR)
    messagebox.showinfo('PIL','Se agrego el filtro Contorno')
    imagen2.show()

#Agrega filtro Resaltar
def filtro4():
    imagen2 = imagen1.filter(ImageFilter.EDGE_ENHANCE)
    messagebox.showinfo('PIL','Se agrego el filtro Resaltar')
    imagen2.show()

#estableceremos tanto el color, tamano y botones de la ventana
ventana=Tk()
ventana.title("Proyecto con pillow: ")
ventana.geometry("500x500")
ventana.configure(bg="light pink")

label2=Label(ventana, image="")

#Creamos boton para cargar la imagen 
btn=Button(ventana,text="Cargar imagen", command=cargar)
btn.configure(bg="red")
btn.configure(fg="white")
btn.place(x=350,y=170)

#Creamos boton que agrega el filtro B/N
btn1 = Button(ventana, text="Blanco y Negro", command=filtro1)
btn1.configure(bg="red")
btn1.configure(fg="white")
btn1.place(x=20,y=350)

#Creamos boton que agrega el filtro Desenfocar
btn2 = Button(ventana, text="Desenfocar", command=filtro2)
btn2.configure(bg="red")
btn2.configure(fg="white")
btn2.place(x=150,y=350)

#Creamos boton que agrega el filtro Contorno
btn3 = Button(ventana, text="Contorno", command=filtro3)
btn3.configure(bg="red")
btn3.configure(fg="white")
btn3.place(x=250,y=350)

#Creamos boton que agrega el filtro Resaltar 
btn4 = Button(ventana, text="Resaltar", command=filtro4)
btn4.configure(bg="red")
btn4.configure(fg="white")
btn4.place(x=350,y=350)


label2.pack()
ventana.mainloop()  