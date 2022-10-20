from email.mime import image
import PIL 
from PIL import Image, ImageTk, ImageFilter
from tkinter import Y, Tk, Entry, Label, Button, Radiobutton, IntVar, messagebox

vent1= Tk()
vent1.geometry("500x465")


def factura():
    pass


labl1=Label(vent1, bg = "#D5F1F1",text="Cafeteria")

image1 = Image.open("carne.jpeg")
image1= image1.resize((55,55), Image.ANTIALIAS)
img1 = ImageTk.PhotoImage(image1)
image1 = Label(vent1, image = img1)

image2 = Image.open("pollo.jpg")
image2= image2.resize((55,55), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(image2)
image2 = Label(vent1, image = img2)

image3 = Image.open("pollo.jpg")
image3= image3.resize((55,55), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(image3)
image3 = Label(vent1, image = img3)

labl2=Label(vent1,bg = "#D5F1F1", text="Ensaladas")

image4 = Image.open("ensalada_fresca.jpg")
image4= image4.resize((55,55), Image.ANTIALIAS)
img4 = ImageTk.PhotoImage(image4)
image4 = Label(vent1, image = img4)

image5 = Image.open("ensalada_de_coditos.jpg")
image5= image5.resize((55,55), Image.ANTIALIAS)
img5 = ImageTk.PhotoImage(image5)
image5 = Label(vent1, image = img5)

image6 = Image.open("ensalada_rusa.jpeg")
image6 = image6.resize((55,55), Image.ANTIALIAS)
img6 = ImageTk.PhotoImage(image6)
image6 = Label(vent1, image = img6)

labl3=Label(vent1,bg = "#D5F1F1", text="Frescos.")

image7 = Image.open("gaseosas.jpg")
image7 = image7.resize((55,55), Image.ANTIALIAS)
img7 = ImageTk.PhotoImage(image7)
image7 = Label(vent1, image = img7)


image8 = Image.open("frescos.jpeg")
image8 = image8.resize((55,55), Image.ANTIALIAS)
img8 = ImageTk.PhotoImage(image8)
image8 = Label(vent1, image = img8)

image9 = Image.open("cafe.jpg")
image9 = image9.resize((55,55), Image.ANTIALIAS)
img9 = ImageTk.PhotoImage(image9)
image9 = Label(vent1, image = img9)


#variables en donde se guardan las elecciones del cliente
eleccion_almuerzo = IntVar()

eleccion_ensalada = IntVar()

eleccion_bebida = IntVar()

#Radios para marcas los almuerzos
rdbtn1 = Radiobutton(vent1, bg = "#D5F1F1",text="Carne Asada", value=1, variable=eleccion_almuerzo)

rdbtn2 = Radiobutton(vent1, bg = "#D5F1F1",text="Pollo Guisado", value=2, variable=eleccion_almuerzo)

rdbtn3 = Radiobutton(vent1, bg = "#D5F1F1",text="Lasaña", value=3, variable=eleccion_almuerzo)

#Radios para marcar las ensaladas
rdbtn4 = Radiobutton(vent1, bg = "#D5F1F1",text="Fresca", value=1, variable=eleccion_ensalada)

rdbtn5 = Radiobutton(vent1, bg = "#D5F1F1",text="Coditos", value=2, variable=eleccion_ensalada)

rdbtn6 = Radiobutton(vent1, bg = "#D5F1F1",text="Rusa", value=3, variable=eleccion_ensalada)

#Radios para sacar las bebidas
rdbtn7 = Radiobutton(vent1, bg = "#D5F1F1",text="Gaseosa", value=1, variable=eleccion_bebida)

rdbtn8 = Radiobutton(vent1, bg = "#D5F1F1",text="Fresco", value=2, variable=eleccion_bebida)

rdbtn9 = Radiobutton(vent1, bg = "#D5F1F1",text="Cafe", value=3, variable=eleccion_bebida)




#Las entradas de los inputs
input1=Entry(vent1)

input2=Entry(vent1)


def factura():

    #Ciclo para evaluar la eleccion del cliente
    if eleccion_almuerzo.get()==1:
        plato = "Carne asada"
        precio_1 = 2.50
    elif eleccion_almuerzo.get()==2:
        plato = "Pollo guisado"
        precio_1 = 2.25
    elif eleccion_almuerzo.get()==3:
        plato = "Lasaña"
        precio_1 = 3.00
    
    if eleccion_ensalada.get()==1:
        ensalada = "Fresca"
        precio_2 = 0.25
    elif eleccion_ensalada.get()==2:
        ensalada = "Coditos"
        precio_2 = 0.25
    elif eleccion_ensalada.get()==3:
        ensalada = "Rusa"
        precio_2 = 0.25


    if eleccion_bebida.get()==1:
        bebida ="Gaseosa"
        precio_3= 0.75
    elif eleccion_bebida.get()==2:
        bebida ="Frescos"
        precio_3= 0.50
    elif eleccion_bebida.get()==3:
        bebida ="Cafe"
        precio_3= 0.65

    #Se imprimen los resultados obtenidos por el cliente
    precio_f = precio_1 + precio_2 + precio_3
    print("---------------Factura de los productos---------------")
    print("Plato principal: ",plato, "Precio $: ", precio_1)
    print("Ensalada: ",ensalada,"Precio: $",precio_2 )
    print("Bebida: ",bebida, "Precio: $", precio_3)
    print("Total: $", precio_f)
    print("------------------------------------------------------")

#Declaracion de los radio button
btn1 = Button(vent1,text="Calcular Factura",command=factura,bg='#D5F1F9')

vent1.configure(bg='#D5F1F1')
vent1.title("Cafeteria Buen Oscar")

#Se agrega titulo a la ventana
labl1.place(y=10, x=70 )
image1.place(y=50, x=70)
rdbtn1.place(y=110, x=50)

labl2.place(y=150, x=70)
image2.place(y=50, x=200)
rdbtn2.place(y=110, x=180)

image3.place(y=50, x=350)
rdbtn3.place(y=110, x=340)

image4.place(y=180, x=70)
rdbtn4.place(y=245, x=50)

image5.place(y=180, x=200)
rdbtn5.place(y=245, x=180)

image6.place(y=180, x=350)
rdbtn6.place(y=245, x=340)

labl3.place(y=280, x=70)
image7.place(y=310, x=70)
rdbtn7.place(y=380, x=50)

image8.place(y=310, x=200)
rdbtn8.place(y=380, x=180)

image9.place(y=310, x=350)
rdbtn9.place(y=380, x=340)

btn1.place(y=420, x=200)


vent1.mainloop()