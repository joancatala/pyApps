#!/usr/bin/python
from Tkinter import *
import tkMessageBox, os, datetime, MySQLdb, smtplib

root = Tk()
#root.geometry('600x480+400+200')
root.geometry('600x560+350+150')
root.title('Base de dades - SEPAM')
root.resizable(0,0)

def SobreElPrograma():
    tkMessageBox.showinfo("Sobre el programa", "Aquest programa serveix als responsables tecnics del SEPAM - Diputacio de Castello.\n\nPer qualsevol incidencia escriviu a grupotic@dipcas.es")

def GestioAjuntaments():
        import subprocess
        subprocess.Popen('C:\Python24\python.exe pyGestioAjuntaments.py')
        root.destroy()
	
def InsertarIncidencia():
	import subprocess
        subprocess.Popen('C:\Python24\python.exe pyPOW.py')
        root.destroy()

def ResponsablesWeb():
	import subprocess
        subprocess.Popen('C:\Python24\python.exe pyResponsablesWeb.py')
        root.destroy()

def ObrimWebSEpam():
	import subprocess
        subprocess.Popen('explorer http://sepam.dipcas.es')
        root.destroy()
        
	
def Eixir():
    #i eixim del programa.
    root.destroy()


#######################################################################
# PANTALLA1: Pantalla principal
#######################################################################	

# El menu del programa
menubar = Menu(root)
filemenu1 = Menu(menubar, tearoff= 0)
filemenu2 = Menu(menubar, tearoff= 0)
filemenu3 = Menu(menubar, tearoff= 0)
filemenu4 = Menu(menubar, tearoff= 0)

filemenu1.add_command(label="Insertar Incidencia", command=InsertarIncidencia)
filemenu1.add_command(label="Gestio Responables Webs Municipals", command=GestioAjuntaments)
filemenu1.add_command(label="Gestio Responables Webs Municipals", command=ResponsablesWeb)
filemenu1.add_separator()
filemenu1.add_command(label="Eixir del programa", command=Eixir)

filemenu2.add_command(label="Copiar")
filemenu2.add_command(label="Tallar")
filemenu2.add_command(label="Enganxar")
filemenu2.add_separator()
filemenu2.add_command(label="Guardar els canvis", command=Eixir)

filemenu3.add_command(label="Fitxa de l'entitat actual", command=Eixir)
filemenu3.add_command(label="Fitxa de totes las entidats", command=Eixir)
filemenu3.add_command(label="Codi INE de las entidats", command=Eixir)
filemenu3.add_command(label="Telefons de las entitats", command=Eixir)
filemenu3.add_command(label="Emails de les entidats", command=Eixir)
filemenu3.add_command(label="Dominis webs de les entidats", command=Eixir)

filemenu4.add_command(label="Sobre el programa", command=SobreElPrograma)

menubar.add_cascade(label="Arxiu", menu = filemenu1)
menubar.add_cascade(label="Editar", menu = filemenu2)
menubar.add_cascade(label="Exportar", menu = filemenu3)
menubar.add_cascade(label="Ajuda", menu = filemenu4)
root.config(menu=menubar)

# Frame superior: Afegim la imatge de l'aplicacio
frame_logo = Frame(root)
frame_logo.grid(row=0, column=1, sticky=N)

photo = PhotoImage(file="imatges/logo.gif")
w = Label(frame_logo, image=photo)
w.photo = photo
w.grid(row=0, sticky=N)

# Frames de baix on afegim els widgets
frame_baix = Frame(root, width="400", height="400")
frame_baix.grid(row=1, column=1, sticky=W, pady=40)

#frame1
frame_baix1 = Frame(frame_baix, width="140", height="400")
frame_baix1.grid(row=0, column=0, sticky=W)

photo = PhotoImage(file="imatges/logos_aplicacions/aplicacio_1.gif")
w1 = Label(frame_baix1, image=photo)
w1.photo = photo
w1.grid(row=0, sticky=N)

boto1 = Button(frame_baix1, text='Abrir programa', command=GestioAjuntaments)
boto1.grid(row=1, column=0, pady=30)

#frame2
frame_baix2 = Frame(frame_baix, width="140", height="400")
frame_baix2.grid(row=0, column=1, sticky=W)

photo = PhotoImage(file="imatges/logos_aplicacions/aplicacio_2.gif")
w2 = Label(frame_baix2, image=photo)
w2.photo = photo
w2.grid(row=0, sticky=N)

boto2 = Button(frame_baix2, text='Abrir programa', command=ResponsablesWeb)
boto2.grid(row=1, column=0, pady=30)

#frame3
frame_baix3 = Frame(frame_baix, width="140", height="400")
frame_baix3.grid(row=0, column=2, sticky=W)

photo = PhotoImage(file="imatges/logos_aplicacions/aplicacio_3.gif")
w3 = Label(frame_baix3, image=photo)
w3.photo = photo
w3.grid(row=0, sticky=N)

boto3 = Button(frame_baix3, text='Abrir programa', command=InsertarIncidencia)
boto3.grid(row=1, column=0, pady=30)

#frame4
frame_baix4 = Frame(frame_baix, width="140", height="400")
frame_baix4.grid(row=0, column=3, sticky=W)

photo = PhotoImage(file="imatges/logos_aplicacions/aplicacio_4.gif")
w4 = Label(frame_baix4, image=photo)
w4.photo = photo
w4.grid(row=0, sticky=N)

boto4 = Button(frame_baix4, text='Abrir programa', command=ObrimWebSEpam)
boto4.grid(row=1, column=0, pady=30)

#######################################################################
# Endavant!
#######################################################################	
root.mainloop()
