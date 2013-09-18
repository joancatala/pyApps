#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Responsables: SEPAM <grupotic@dipcas.es>
#
#

from Tkinter import *
import tkMessageBox, os, datetime, MySQLdb

root = Tk()
root.geometry('600x560+350+150')
root.title('Responsables de las Webs Municipales')
root.resizable(0,0)

# Configuracio basica de la base de dades del POW
#
SERVIDOR = '192.168.5.3'
USUARI = 'root'
CONTRASENYA = 'lacasitos'
BASE_DE_DADES = 'ofisam'


def Eixir():
    #i eixim del programa.
    root.destroy()

def SobreElPrograma():
    tkMessageBox.showinfo("Sobre el programa", "Aquest programa serveix als responsables tecnics del SEPAM - Diputacio de Castello.\n\nPer qualsevol incidencia escriviu a grupotic@dipcas.es")
	      
def EnviaMail(): 
    win = Tk()
    win.geometry('500x100+700+300')
    win.title('Responsables web')
    Label(win,  text='Vols desar la informacio dels responsables?').pack()          
    Button(win, text='Guarda i ix').pack(side=LEFT)
    Button(win, command=Eixir, text='Eixir sense guardar').pack(side=RIGHT)
    win.mainloop()


def NetejarCamps():
    #Primer de tot borrarem els camps de text
    entry0.delete(0,END)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    text1.delete(1.0,END)
	 # el frame_dreta2 donde incluimos las fotos
    frame_dreta2 = Frame(frame_dreta, width=70, height=200)
    frame_dreta2.grid(row=0, column=1, sticky=E, pady=5)
    photo = PhotoImage(file="imatges/responsables/sin_foto.gif")
    w = Label(frame_dreta2, image=photo)
    w.photo = photo
    w.grid(row=0, column=0, padx=0, pady=0, sticky=N)

def InfoResponsable():
    # Esborrem tots els camps aixi podrem introduir els nous
    # 
    NetejarCamps()
	
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT CODIGO, telefon_responsable, web, nom_responsable, email_responsable, comentaris FROM responsables_web where CODIGO='"+llista.get(ACTIVE)[0:4] +"'"
    cursor.execute(sql)
    resultado=cursor.fetchall()
	
    #fiquem a una sola tupla el resultat del SELECT
    nom_responsable = resultado[0]
	
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT web, CODIGO FROM ayuntamientos where CODIGO='"+llista.get(ACTIVE)[0:4] +"'"
    cursor.execute(sql)
    resultado2=cursor.fetchall()
	
    #fiquem a una sola tupla el resultat del SELECT i enmagatzenem la url de la web
    datos_url = resultado2[0]	

    # Pista per saber si ja ha passat per aci
    # 
    #print nom_responsable
    #print "ja ha passat el nom_responsable!!!"
        
    #I ara extraem els tres diferents camps d'aquesta trupla
    #
    camp_codi = nom_responsable[0]
    camp_telf = nom_responsable[1]
    camp_web = datos_url[0]
    camp_nom = nom_responsable[3]
    camp_email = nom_responsable[4]
    camp_notes = nom_responsable[5]

    entry0.insert(0,camp_codi)
    entry1.insert(0,camp_nom)
    entry2.insert(0,camp_email)
    entry3.insert(0,camp_telf)
    entry4.insert(0,camp_web)
    text1.insert(1.0,camp_notes)
    # el frame_dreta2 donde incluimos las fotos
    frame_dreta2 = Frame(frame_dreta, width=70, height=200)
    frame_dreta2.grid(row=0, column=1, sticky=E, pady=5)
    photo = PhotoImage(file="imatges/responsables/" + camp_codi + ".gif")
    w = Label(frame_dreta2, image=photo)
    w.photo = photo
    w.grid(row=0, column=0, padx=0, pady=0, sticky=N)
	
def GuardarCanvis():
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    sql1="UPDATE responsables_web SET nom_responsable='" + entry1.get() + "' where CODIGO='" + entry0.get() + "'"
    sql2="UPDATE responsables_web SET email_responsable='" + entry2.get() + "' where CODIGO='" + entry0.get() + "'"
    sql3="UPDATE responsables_web SET telefon_responsable='" + entry3.get() + "' where CODIGO='" + entry0.get() + "'"
    sql4="UPDATE ayuntamientos SET web='" + entry4.get() + "' where CODIGO='" + entry0.get() + "'"
    sql5="UPDATE responsables_web SET comentaris='" + text1.get(1.0,END) + "' where CODIGO='" + entry0.get() + "'"

    cursor.execute(sql1)
    resultado1=cursor.fetchall()

    cursor.execute(sql2)
    resultado2=cursor.fetchall()

    cursor.execute(sql3)
    resultado3=cursor.fetchall()

    cursor.execute(sql4)
    resultado4=cursor.fetchall()

    cursor.execute(sql5)
    resultado5=cursor.fetchall()
    tkMessageBox.showinfo('Dades guardades', 'Els canvis han segut guardats correctament.')
	
#######################################################################    
# El menu del programa
#######################################################################
menubar = Menu(root)
filemenu1 = Menu(menubar, tearoff= 0)
filemenu2 = Menu(menubar, tearoff= 0)
filemenu3 = Menu(menubar, tearoff= 0)

filemenu1.add_command(label="Consultar el responsable", command=InfoResponsable)
filemenu1.add_command(label="Guardar canvis", command=GuardarCanvis)
filemenu1.add_separator()
filemenu1.add_command(label="Eixir del programa", command=Eixir)

filemenu2.add_command(label="Copiar")
filemenu2.add_command(label="Tallar")
filemenu2.add_command(label="Enganxar")
filemenu2.add_separator()
filemenu2.add_command(label="Neteja els camps", command=NetejarCamps)

filemenu3.add_command(label="Sobre el programa", command=SobreElPrograma)

menubar.add_cascade(label="Arxiu", menu = filemenu1)
menubar.add_cascade(label="Editar", menu = filemenu2)
menubar.add_cascade(label="Ajuda", menu = filemenu3)
root.config(menu=menubar)


#######################################################################
# Frame de dalt
#######################################################################
# Frame superior: Afegim la imatge de l'aplicacio
frame_logo = Frame(root)
frame_logo.grid(row=0, column=0, sticky=W, columnspan=2)

photo = PhotoImage(file="imatges/logo.gif")
w = Label(frame_logo, image=photo)
w.photo = photo
w.grid(row=1, sticky=N+W)

#######################################################################
# Frames de baix on afegim els widgets
#######################################################################
frame_contenedor = Frame(root, height=550)
frame_contenedor.grid(row=1, column=1, sticky=W, pady=20)

#######################################################################
# Frame esquerra
#######################################################################
frame_esquerra = Frame(frame_contenedor, width=250, height=200)
frame_esquerra.grid(row=1, column=0, sticky=W)

frame_llista = Frame(frame_esquerra)
frame_llista.pack()
scroll = Scrollbar(frame_llista, bg='grey')
scroll.pack(side=RIGHT, fill=Y)

llista = Listbox(frame_llista, yscrollcommand=scroll.set, height="31", width="34", bg='white')
llista.pack()

db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
cursor=db.cursor()
sql='SELECT CODIGO, MUNICIPIO From ayuntamientos ORDER BY CODIGO'
cursor.execute(sql)
resultado=cursor.fetchall()

for i in resultado:
    llista.insert(END, i[0] + " - " + i[1])

scroll.config(command=llista.yview, relief=SUNKEN)

#######################################################################
# Frame dreta
#######################################################################
frame_dreta = Frame(frame_contenedor, height=200)
frame_dreta.grid(row=1, column=1, padx=10)

# el frame_dreta1 donde incluimos los labels y entrys
frame_dreta1 = Frame(frame_dreta, height=200)
frame_dreta1.grid(row=0, column=0, sticky=W)

entry0 = Entry(frame_dreta1, bg='white', width=22)
label1 = Label(frame_dreta1, text='Responsable: ')
label1.grid(row=1, column=0, sticky=W)
entry1 = Entry(frame_dreta1, font = '{MS Sans Serif} 10', bg='white', width=24)
entry1.grid(row=2, column=0, sticky=W, pady=5)

label2 = Label(frame_dreta1, text='Correu: ')
label2.grid(row=3, column=0, sticky=W)
entry2 = Entry(frame_dreta1, font = '{MS Sans Serif} 10', bg='white', width=24)
entry2.grid(row=4, column=0, sticky=W, pady=5)

label3 = Label(frame_dreta1, text='Telf.: ')
label3.grid(row=5, column=0, sticky=W)
entry3 = Entry(frame_dreta1, font = '{MS Sans Serif} 10', bg='white', width=24)
entry3.grid(row=6, column=0, sticky=W, pady=5)

label4 = Label(frame_dreta1, text='Web: ')
label4.grid(row=7, column=0, sticky=W)
entry4 = Entry(frame_dreta1, font = '{MS Sans Serif} 10', bg='white', width=24)
entry4.grid(row=8, column=0, sticky=W, pady=5)

# el frame_dreta2 donde incluimos las fotos
frame_dreta2 = Frame(frame_dreta, height=200, )
frame_dreta2.grid(row=0, column=1, pady=5)

photo = PhotoImage(file="imatges/responsables/sin_foto.gif")
w = Label(frame_dreta2, image=photo)
w.photo = photo
w.grid(row=0, column=0, padx=0, pady=0, sticky=N)

# el frame_dreta3 donde incluimos el textarea
frame_dreta3 = Frame(frame_dreta, height=200)
frame_dreta3.grid(row=2, column=0, sticky=W, columnspan=2)

# el textarea
label5 = Label(frame_dreta3, text='Comentaris: ')
label5.grid(row=0, column=0, sticky=W)
frame_text = Frame(frame_dreta3)
frame_text.grid(row=1, column=0, sticky=W)
scrolltext = Scrollbar(frame_text, bg='grey')
scrolltext.pack(side=RIGHT, fill=Y)
text1 = Text(frame_text, font = '{MS Sans Serif} 10', width=43, height=11, yscrollcommand=scrolltext.set, bg= 'white')
text1.pack(side=BOTTOM)
scrolltext.config(command=text1.yview, relief=SUNKEN)

# el frame_dreta4 donde incluimos los botones
frame_dreta4 = Frame(frame_dreta, width=270, height=55)
frame_dreta4.grid(row=3, column=0, sticky=E)

boto1 = Button(frame_dreta4, fg="blue", text='Consultar responsable', command=InfoResponsable)
boto1.grid(row=0, column=0, sticky=W, pady=10, padx=5)
boto2 = Button(frame_dreta4, text='Guardar canvis', command=GuardarCanvis)
boto2.grid(row=0, column=1, sticky=W, pady=10)


#Endavant!
root.mainloop()
