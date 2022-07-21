from ast import Expression
from cProfile import label
from doctest import master
from operator import le, truediv
from re import I
import tkinter as tk
import sympy as sym
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib import pyplot as plt
from matplotlib import *

ventana = tk.Tk()
ventana.title('calculadora mamadisima')
ventana.geometry('800x600')
ventana.resizable(False,False)
ventana.configure(background='gray20')
operador=''
texto_pantalla = tk.StringVar()
pant = tk.StringVar()
pant2 = tk.StringVar()

pantalla = tk.Entry(ventana, font=('calibri',18), width=23, borderwidth=5, textvariable=texto_pantalla, justify=tk.RIGHT)
pantalla.place(x= 25, y=25)

pantalla2 = tk.Entry(ventana, font=('calibri',20), textvariable=pant, width=24, borderwidth=None)
pantalla2.place(x= 410, y=335, relheight=0.26)

pantalla3 = tk.Entry(ventana, width=60, borderwidth=None)
pantalla3.place(x=410,y=25, relheight=0.5)

pantalla4 = tk.Entry(ventana, font=('calibri',20), textvariable=pant2, width=24, borderwidth=1)
pantalla4.place(x=410,y=335, relheight=None)


def AC():
    global operador
    operador = ''
    texto_pantalla.set('')
    pant.set('')
    pant2.set('')

    figura= plt.figure(figsize=(4,3),dpi=100)
    tk.Canvas = FigureCanvasTkAgg(figura, master=ventana)
    tk.Canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455, relheight=0.44)
    barra_tareas=NavigationToolbar2Tk(tk.Canvas, ventana)
    barra_tareas.place(x=410,y=290, relwidth=0.455)
    tk.Canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)

    plt.clf()

I +=1

def click(n):
    global I
    pantalla.insert(I, n)
    I +=1

def operaciones(b):
    global I
    long_b = len(b)
    pantalla.insert(I, b)
    I+= long_b

def CDF():
    pant.set('')
    pant2.set('')
    mensaje='las raices son:'
    pantalla4.insert(0,mensaje)
    cdf= pantalla.get()
    cdf1=sym.sympify(cdf)
    t1=sym.roots(cdf1,multiple=True)

    raiz=t1[0]
    rd=(raiz).evalf(5)
    pantalla2.insert(0,rd)

    expresion=pantalla.get()
    expresion1=sym.sympify(expresion)
    x= sym.simbol('x')
    v= np.linspace(-15,15,100, endpoint=True)
    valores=[]

    figura=plt.figure(figsize=(4,3),dpi=100)
    tk.Canvas=FigureCanvasTkAgg(figura, master=ventana)
    tk.Canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455, relheight=0.44)
    barra_tareas=NavigationToolbar2Tk(tk.Canvas, ventana)
    barra_tareas.place(x=410,y=290, relwidth=0.455)
    tk.Canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)

    for i in range(len(v)):
        c=((expresion1).evalf(subs={x: v[i]}))
        valores.append(c)
    for j in range(len(t1)):
        figura.add_subplot(111).plot(v,valores,label='{0}'.format(expresion))
        if j==0:
            plt.legend(loc='upper left')
    plt.grid()
    tk.Canvas.draw()

def DEL():
    p = pantalla.get()
    if len(p)>0:
        np = p[:-1]
        AC()
        pantalla.insert(0,np)
    else:
        AC()

def igual():
    estado_P= pantalla.get()
    try:
        global expresion 
        expresion = sym.sympify(estado_P)

        AC()
        pantalla.insert(0, expresion)
    except:
        AC()

def aprox():
    contenido = pantalla.get()
    aproximacion = (sym.sympify(contenido)).evalf(15)
    AC()
    pantalla.insert(0,aproximacion)

def grafica():
    expresion =pantalla.get()
    expresion1= sym.sympify(expresion)
    x= sym.Symbol('x')
    v= np.linspace(-15,15,100, endpoint=True)
    valores=[]

    figura = plt.figure(figsize=(4,3),dpi=100)
    tk.Canvas=FigureCanvasTkAgg(figura, master=ventana)
    tk.Canvas.get_tk_widget().place(x=25,y=25, relwidth=0.455,relheight=0.44)
    barra_tareas = NavigationToolbar2Tk(tk.Canvas, ventana)
    barra_tareas.place(x=410,y=25, relwidth=0.455)
    tk.Canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)

    for i in range(len(v)):
        c = ((expresion1).evalf(subs={x: v[i]}))
        valores.append(c)
    
    figura.add_subplot(111).plot(v,valores,label='{0}'.format(expresion))
    plt.legend(loc = 'upper left')
    plt.grid()
    tk.Canvas.draw()

def limites():
    pant.set('')
    pant2.set('')
    c=pantalla.get()
    mensaje='el valor de la integral definida es: '
    pantalla4.insert(0, mensaje)
    c1=c.split(',')
    li=c1[1]
    ls=c1[2]
    inte =c1[0]
    inte1 = sym.sympify(inte)
    res =sym.integrate(inte1,('x',li,ls))
    pantalla2.insert(1,res)

def derivada():
    pant.set('')
    pant2.set('')
    d = pantalla.get()

    if 'x' in d:
        d1= sym.sympify(d)
        r= sym.diff(d1,'x')
        pantalla2.insert(0,r)
        mensaje='la derivada es: '
        pantalla4.insert(0, mensaje)
        expresion = pantalla2.get()
        expresion1= sym.sympify(expresion)
        x= sym.symbols('x')
        v= np.linspace(-15,15,100, endpoint=True)
        valores=[]
        figura=plt.figure(figsize=(4,3),dpi=100)
        ax= figura.add_subplot(111)
        tk.Canvas = FigureCanvasTkAgg(figura, master=ventana)
        tk.Canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        barra_tareas=NavigationToolbar2Tk(tk.Canvas, ventana)
        barra_tareas.place(x=410,y=290,relwidth=0.455)
        tk.Canvas.get_tk_widget().place(x=410,y=25,relwidth=0.455)

        for i in range(len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
        ax.clear()
        ax.plot(v,valores,label='{0}'.format(expresion))
        plt.grid()
        tk.Canvas.draw()
        expresion=pantalla.get()
        expresion1=sym.sympify(expresion)
        x=sym.Symbol('x')
        v = np.linspace(-15,15,100, endpoint=True)
        valores=[]
        figura=Figure(figsize=(4,3),dpi=100)
        tk.Canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        barra_tareas=NavigationToolbar2Tk(tk.Canvas, ventana)
        barra_tareas.place(x=410,y=290,relwidth=0.455)

        for i in range(len(v)):
            c=((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
            ax.plot(v,valores,label='{0}'.format(expresion))
            plt.legend(loc= 'upper left')
            tk.Canvas.draw()
    else:
        d1= sym.sympify(d)
        r= sym.diff(d1,'y')
        pantalla2.insert(0,r)
        mensaje='la derivada es: '
        pantalla4.insert(0, mensaje)
        expresion = pantalla2.get()
        expresion1= sym.sympify(expresion)
        x= sym.symbol('y')
        v= np.linspace(-15,15,100, endpoint=True)
        valores=[]
        figura=plt.figure(figsize=(4,3),dpi=100)
        ax= figura.add_subplot(111)
        tk.Canvas = FigureCanvasTkAgg(figura, master=ventana)
        tk.Canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        barra_tareas=NavigationToolbar2Tk(tk.Canvas, ventana)
        barra_tareas.place(x=410,y=290,relwidth=0.455)
        tk.Canvas.get_tk_widget().place(x=410,y=25,relwidth=0.455)

        for i in range(len(v)):
            c = ((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
        ax.clear()
        ax.plot(v,valores,label='{0}'.format(expresion))
        plt.grid()
        tk.Canvas.draw()
        expresion=pantalla.get()
        expresion1=sym.sympify(expresion)
        x=sym.Symbol('x')
        v = np.linspace(-15,15,100, endpoint=True)
        valores=[]
        figura=Figure(figsize=(4,3),dpi=100)
        tk.Canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455,relheight=0.44)
        barra_tareas=NavigationToolbar2Tk(tk.Canvas, ventana)
        barra_tareas.place(x=410,y=290,relwidth=0.455)

        for i in range(len(v)):
            c=((expresion1).evalf(subs={x: v[i]}))
            valores.append(c)
            ax.plot(v,valores,label='{0}'.format(expresion))
            plt.legend(loc= 'upper left')
            tk.Canvas.draw()

def integralindef():
    pant.set('')
    pant2.set('')
    inte=pantalla.get()
    inte1=sym.sympify(inte)
    res=sym.integrate(inte1,('x',None,None))
    pantalla2.insert(0,res)
    expresion=pantalla2.get()
    expresion1=sym.sympify(expresion)
    mensaje='la integral indefinida es:'
    pantalla4.insert(0,mensaje)
    x=sym.Symbol('x')
    v=np.linspace(-15,15,100, endpoint=True)
    valores=[]

    figura=plt.figure(figsize=(4,3),dpi=100)
    ax=figura.add_subplot(111)
    tk.Canvas=FigureCanvasTkAgg(figura, master=ventana)
    tk.Canvas.get_tk_widget().place(x=25,y=25,relwidth=0.455, relheight=0.44)
    barra_tareas=NavigationToolbar2Tk(tk.Canvas, ventana)
    barra_tareas.place(x=410,y=25, relwidth=0.455)
    tk.Canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)

    for i in range(len(v)):
        c=((expresion1).evalf(subs={x: v[i]}))
        valores.append(c)
    ax.clear()
    ax.plot(v,valores,label='{0}'.format(expresion))
    plt.legend(loc='upper left')
    plt.grid()
    
    tk.canvas.draw()
    expresion=pantalla.get()
    expresion1=sym.sympify(expresion)
    valores=[]
    figura=Figure(figsize=(4,3),dpi=100)
    tk.Canvas.get_tk_widget().tk.Place(x=25,y=25,relwrelwidth=0.455, relheight=0.44)
    barra_tareas=NavigationToolbar2Tk(tk.Canvas, ventana)
    barra_tareas.place(x=410,y=25, relwidth=0.455)
    tk.Canvas.get_tk_widget().place(x=410,y=25, relwidth=0.455)






boton11=tk.Button(ventana, text='x',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('x')).place(x=25,y=100)
boton12=tk.Button(ventana, text='y',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('y')).place(x=117,y=100)
boton13=tk.Button(ventana, text='x^',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('**')).place(x=210,y=100)
boton14=tk.Button(ventana, text='sin',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('sin')).place(x=301,y=100)

boton21=tk.Button(ventana, text='π',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('pi')).place(x=25,y=150)
boton22=tk.Button(ventana, text='e',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('E')).place(x=117,y=150)
boton23=tk.Button(ventana, text='√',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('sqrt')).place(x=210,y=150)
boton24=tk.Button(ventana, text='cos',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('cos')).place(x=301,y=150)

boton31=tk.Button(ventana, text=',',bd=10, bg='darkorange', width=8, height=1, command=lambda:click(',')).place(x=25,y=200)
boton32=tk.Button(ventana, text='(',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('(')).place(x=117,y=200)
boton33=tk.Button(ventana, text=')',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones(')')).place(x=210,y=200)
boton34=tk.Button(ventana, text='tan',bd=10, bg='darkorange', width=8, height=1, command=lambda:operaciones('tan')).place(x=301,y=200)

boton41=tk.Button(ventana, text='7',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(7)).place(x=25,y=300)
boton42=tk.Button(ventana, text='8',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(8)).place(x=97,y=300)
boton43=tk.Button(ventana, text='9',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(9)).place(x=169,y=300)
boton44=tk.Button(ventana, text='DEL',bd=10, bg='white', width=6, height=1, command=lambda:DEL()).place(x=241,y=300)
boton45=tk.Button(ventana, text='AC',bd=10, bg='white', width=6, height=1, command=lambda:AC()).place(x=313,y=300)

boton51=tk.Button(ventana, text='4',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(4)).place(x=25,y=370)
boton52=tk.Button(ventana, text='5',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(5)).place(x=97,y=370)
boton53=tk.Button(ventana, text='6',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(6)).place(x=169,y=370)
boton54=tk.Button(ventana, text='x',bd=10, bg='darkorange', width=6, height=1, command=lambda:operaciones('*')).place(x=241,y=370)
boton55=tk.Button(ventana, text='÷',bd=10, bg='darkorange', width=6, height=1, command=lambda:operaciones('/')).place(x=313,y=370)

boton61=tk.Button(ventana, text='1',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(1)).place(x=25,y=440)
boton62=tk.Button(ventana, text='2',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(2)).place(x=97,y=440)
boton63=tk.Button(ventana, text='3',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(3)).place(x=169,y=440)
boton64=tk.Button(ventana, text='+',bd=10, bg='darkorange', width=6, height=1, command=lambda:operaciones('+')).place(x=241,y=440)
boton65=tk.Button(ventana, text='-',bd=10, bg='darkorange', width=6, height=1, command=lambda:operaciones('-')).place(x=313,y=440)

boton71=tk.Button(ventana, text='0',bd=10, bg='darkorange', width=6, height=1, command=lambda:click(0)).place(x=25,y=510)
boton72=tk.Button(ventana, text='.',bd=10, bg='darkorange', width=6, height=1, command=lambda:operaciones('.')).place(x=97,y=510)
boton73=tk.Button(ventana, text='GRAF',bd=10, bg='darkorange', width=6, height=1, command=lambda:grafica()).place(x=169,y=510)
boton74=tk.Button(ventana, text='APROX',bd=10, bg='darkorange', width=6, height=1, command=lambda:aprox()).place(x=241,y=510)
boton75=tk.Button(ventana, text='=',bd=10, bg='darkorange', width=6, height=1, command=lambda:igual()).place(x=313,y=510)




boton1= tk.Button(ventana, text=' f/(x)', bd=10, bg='darkorange', font=('calibri',10), width=6, height=1, command=lambda:derivada()).place(x=420,y=510)

boton2= tk.Button(ventana, text=' ∫', bd=10, bg='darkorange', font=('calibri',10), width=6, height=1, command=lambda:integralindef()).place(x=500,y=510)

boton3= tk.Button(ventana, text=' ∫_a,b', bd=10, bg='darkorange', font=('calibri',10), width=6, height=1, command=lambda:limites()).place(x=580,y=510)

boton4= tk.Button(ventana, text='cero de funciones', bd=10, bg='darkorange', font=('calibri',10), width=6, height=1, command=lambda:CDF()).place(x=660,y=510)
ventana.mainloop()