#!/usr/bin/python
# -*- coding: utf-8 -*-

import htmler
import textfile
import spider
import urllib
from tkinter import *
from urllib.parse import urlparse, urljoin


class Pyconsole(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")   
         
        self.parent = parent
        
        self.initUI()

    
    def initUI(self):
      
        self.parent.title("First Launcher")
        self.pack(fill=BOTH, expand=1)
        
        logo = PhotoImage(file="python-logo.png")
        self.x = StringVar()
        self.label1 = Label(self, image=logo)
        self.label1.image = logo
        self.label1.place(x=2, y=2)

        self.label2 = Label(self, text="Zona de mensajes        ", textvariable=self.x)
        self.label2.place(x=5, y=260)
        
        self.label3 = Label(self, text="Par1:")
        self.label3.place(x=5, y=170)
        self.label3 = Label(self, text="Par2:")
        self.label3.place(x=5, y=200)

        self.abtn1 = Button(self, text="Boton 1", command=self.pru)
        self.abtn1.place(x=5, y=230)
        self.abtn2 = Button(self, text="Imagen10", command=self.imagen10)
        self.abtn2.place(x=105, y=230)
        self.abtn3 = Button(self, text="Crawler", command=self.spider)
        self.abtn3.place(x=205, y=230)

        self.par1 = Entry(self, width=40)
        self.par1.place(x=50, y=170)
        self.par2 = Entry(self, width=40)
        self.par2.place(x=50, y=200)
       
    def pru(self):
        texto = self.par1.get()
        print(texto)
        self.x.set(texto)
        
    
    def imagen10(self):
        img_base = self.par1.get()
        imagen = img_base.replace('#', '{0}')
        self.x.set(imagen)
        up = urllib.parse.urlparse(img_base)
        urlImage = up.netloc
        linea = htmler.generabase()
        for i in [0,1,2,3,4]:
                linea = htmler.muestraImagen(linea, imagen.format(i), "prueba")
        linea = htmler.fila(linea)
        for i in [5,6,7,8,9]:
                linea = htmler.muestraImagen(linea, imagen.format(i), "prueba")
        linea = htmler.insertaenlace(urlImage,linea)
        linea = htmler.cierra(linea)
        file_base = self.par2.get()
        textfile.escribe(file_base, linea)
        self.x.set("Proceso Terminado")
    
    def spider(self):
        resultado = "Inicio"
        urlIni = self.par1.get()
        deep = self.par2.get()
        resultado = spider.spider(urlIni, deep)
        self.x.set(resultado)   
        

def main():
  
    root = Tk()
    root.geometry("300x300+300+300")
    app = Pyconsole(root)
    root.mainloop()  



if __name__ == '__main__':
    main()
