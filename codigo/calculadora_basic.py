from tkinter import Tk, Label, Button, Entry, Text
from math import sqrt

def sumar():
    num1= txt1.get()
    num2= txt2.get()
    r= float(num1) + float(num2)
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def restar():
    num1= txt1.get()
    num2= txt2.get()
    r= float(num1) - float(num2)
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def multlipicar():
    num1= txt1.get()
    num2= txt2.get()
    r= float(num1) * float(num2)
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def dividir():
    num1= txt1.get()
    num2= txt2.get()
    r= float(num1) / float(num2)
    txt3.delete(0, 'end')
    txt3.insert(0,r)

def ecu_segundo_grado():
    a= float(txt4.get())
    b= float(txt5.get())
    c= float(txt6.get())
    txt7.delete(0, 'end')
    try: 
        if a!= 0:
            x1= (-b+sqrt((b**2)-(4*a*c)))/(2*a)
            x2= (-b-sqrt((b**2)-(4*a*c)))/(2*a)
            if x1 == 0 and x2 == 0:
                r="Solucion x= %4.3f"%x1
                txt7.insert(0,r)
            else:
                r="Soluciones x1= %4.3f y x2=%4.3f"%(x1, x2)
                txt7.insert(0,r)
        else:
            if b!= 0:
                x= -c/b
                r="Solucion: x= %4.3f" % x
                txt7.insert(0,r)
    except:
        txt7.insert(0,"Sin solucion")
   

ventana= Tk()
ventana.config(background="snow")
ventana.title("Calculadora_drcv")
ventana.geometry("800x600")
ventana.iconbitmap("Python/Calculadora_drcv/img/Logo5.ico")

lbl0= Label(ventana, text="Calculadora Basica", bg= "lavender")
lbl0.place(x= 180, y= 0, width= 100, height=30)

lbl1= Label(ventana, text= 'Primer Numero', bg= "lavender")
lbl1.place(x= 10, y= 40, width= 100, height=30)
txt1= Entry(ventana, bg= "grey90")
txt1.place(x=120, y=40, width= 100, height=30)

lbl2= Label(ventana, text= 'Segundo Numero', bg= "lavender")
lbl2.place(x= 10, y= 80, width= 100, height=30)
txt2= Entry(ventana, bg= "grey90")
txt2.place(x=120, y=80, width= 100, height=30)

lbl3= Label(ventana, text= 'Resultado', bg= "lavender")
lbl3.place(x= 10, y= 150, width= 100, height=30)
txt3= Entry(ventana, bg= "grey90")
txt3.place(x=120, y=150, width= 100, height=30)

btm= Button(ventana, text= 'Suma', command= sumar, cursor= "hand2")
btm.place(x= 230, y=80, width= 80, height=30)

btm= Button(ventana, text= 'Resta', command= restar, cursor= "hand2")
btm.place(x= 230, y=40, width= 80, height=30)

btm= Button(ventana, text= 'Multlipicar', command= multlipicar, cursor= "hand2")
btm.place(x= 320, y=40, width= 80, height=30)

btm= Button(ventana, text= 'Dividir', command= dividir, cursor= "hand2")
btm.place(x= 320, y=80, width= 80, height=30)

lbl4= Label(ventana, text="Calculadora que resuelve\necuaciones de 1er y 2do grado", bg='lavender')
lbl4.place(x= 140, y= 210, width= 170, height=30)

lbl5= Label(ventana, text= "Valor de x2", bg= "lavender")
lbl5.place(x= 10, y= 250, width= 100, height=30)
lbl6= Label(ventana, text= "Valor de x", bg= "lavender")
lbl6.place(x= 10, y= 290, width= 100, height=30)
lbl7= Label(ventana, text= "Valor de c", bg= "lavender")
lbl7.place(x= 10, y= 330, width= 100, height=30)

txt4= Entry(ventana, bg="grey90")
txt4.place(x= 120, y= 250, width= 100, height=30)
txt5= Entry(ventana, bg="grey90")
txt5.place(x= 120, y= 290, width= 100, height=30)
txt6= Entry(ventana, bg="grey90")
txt6.place(x= 120, y= 330, width= 100, height=30)

btm= Button(ventana, text="Resolver ecucion", bg= "lavender", command= ecu_segundo_grado, cursor= "hand2")
btm.place(x= 230, y= 280, width= 100, height=50)

lbl8= Label(ventana, text= "Resultado", bg="lavender")
lbl8.place(x= 10, y= 400, width= 100, height=30)
txt7= Entry(ventana, bg="grey90")
txt7.place(x= 120, y= 400, width= 200, height=60)

lbl9=Label(ventana, text= "Notas", bg="lavender")
lbl9.place(x= 520, y= 0, width= 100, height=30)
txt8= Text(ventana, bg= "grey90", cursor= "hand2")
txt8.place(x=430, y=40, width= 280, height=450)


ventana.mainloop()