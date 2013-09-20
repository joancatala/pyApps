#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Responsables: SEPAM <grupotic@dipcas.es>
#
#

from Tkinter import *
import tkMessageBox, os, datetime, MySQLdb, smtplib, tkFileDialog


# Configurem el formulari (Altura + Amplada + Possició vertical i horitzonal)

root = Tk()
root.geometry('600x560+350+150')
root.title('Ajuntaments')
root.resizable(0,0)

# Configuracio basica de la base de dades del POW

SERVIDOR = '192.168.5.3'
USUARI = 'root'
CONTRASENYA = 'lacasitos'
BASE_DE_DADES = 'ofisam'

varnombre = StringVar()
varescudo = StringVar()
varincidencias = StringVar()       

  
def Actualitzacions():
  
    os.system("//wofima/sepam/scentrales/general/PKG/pyApps/pyActualitzacions.bat")


def SobreElPrograma():
    
    # Missatge del Acerca de
    
    tkMessageBox.showinfo("Sobre el programa", "Aquest programa serveix als responsables tècnics del SEPAM - Diputació de Castelló.\n\nPer qualsevol incidència escriviu a grupotic@dipcas.es")
 
def Eixir():
    
    # Eixim del programa
    
    root.destroy()

def ExportFitxaEntitat():
    
        if len(varnombre.get()) == 0:
            tkMessageBox.showinfo("Imposible generar TXT", "No es pot generar el TXT perquè no has seleccionat cap entidad.")
            return
  
	# Obrim el fitxer de text
	#Així es com estava abans quan el ficava a /exportacions ----> f=open("exportacions/fitxa-" + varnombre.get() + ".txt","w")
	fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.txt|*.*", filetypes=[('Fitxer TXT','*.txt'),('Tots els fitxers','*.*')])
	f = open(fitxer, "w")

	f.write("-------------------------------------------------------------------\n")
	f.write(varnombre.get() + "\n\n")
	f.write("Direccio: " + textdireccion.get() + "\n")
	f.write("Codi Postal: " + textcp.get() + "\n")
	f.write("Telf: " + texttelefono.get() + "\n")
	f.write("FAX: " + textfax.get() + "\n")
	f.write("E-mail: " + textmail.get() + "\n")
	f.write("Web: " + textweb.get() + "\n")	
	f.write("Secretari: " + textsecretario.get() + "\n")
	f.write("Alcalde: " + textalcalde.get() + "\n")
	f.write("Ofisam: " + textofisam.get() + "\n")
	f.write("-------------------------------------------------------------------\n")
		
	# Tanquem el fitxer
	
	f.close()
    
        if len(fitxer) > 0:
            tkMessageBox.showinfo("TXT Generat", "S'ha generat el document a " + fitxer)
        else:
            return


def Export1():
    
    if len(varnombre.get()) == 0:
            tkMessageBox.showinfo("Imposible generar PDF", "No es pot generar el PDF perquè no has seleccionat cap entidad.")
            return

    #Exportem les dades de l'Ajuntament actual
        
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch

    #Abans ho tenia com les següents línies i ho deixava a /exportacions
    #doc = SimpleDocTemplate("exportacions/fitxa-" + varnombre.get() + ".pdf",pagesize=A4,
                            #rightMargin=72,leftMargin=72,
                            #topMargin=72,bottomMargin=18)

    fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.pdf|*.*", filetypes=[('Fitxer PDF','*.pdf'),('Tots els fitxers','*.*')])
    doc = SimpleDocTemplate (fitxer,pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

	
    #Creem la llista "Story" i iniciem la variable "styles"
    
    Story=[]
    styles=getSampleStyleSheet()	
    
    ptext = unicode("<font size=17>" + varnombre.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext.strip(), styles["Normal"]))
    Story.append(Spacer(1, 14))

    ptext = unicode("<font size=10>Direccion: " + textdireccion.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    ptext = unicode("<font size=10>CP: " + textcp.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    ptext = unicode("<font size=10>Telf: " + texttelefono.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    ptext = unicode("<font size=10>FAX: " + textfax.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    ptext = unicode("<font size=10>E-mail: " + textmail.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    ptext = unicode("<font size=10>Web: " + textweb.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    ptext = unicode("<font size=10>Secretari: " + textsecretario.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    ptext = unicode("<font size=10>Alcalde: " + textalcalde.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    ptext = unicode("<font size=10>Ofisam: " + textofisam.get() + "</font>", "iso-8859-1")
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 6))

    #Finalment creem el document PDF
    
    doc.build(Story)
    
    if len(fitxer) > 0:
        tkMessageBox.showinfo("PDF Generat", "S'ha generat el document a " + fitxer)
    else:
        return
    

def Export2():

    #Exportamos los datos de todas las entidades
    
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
 
    #Abans ho tenia com les següents línies i ho deixava a /exportacions
    #doc = SimpleDocTemplate("exportacions/totes-les-fitxes.pdf",pagesize=A4,
                            #rightMargin=72,leftMargin=72,
                            #topMargin=72,bottomMargin=18)

    fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.pdf|*.*", filetypes=[('Fitxer PDF','*.pdf'),('Tots els fitxers','*.*')])
    doc = SimpleDocTemplate (fitxer,pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    
    
    #Creem la llista "Story" i iniciem la variable "styles"
    
    Story=[]
    styles=getSampleStyleSheet()


    # Generamos el select para obtener los datos de la ficha
    
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT CODIGO, MUNICIPIO, DOMICILIO, CP, TELEFONO, FAX, email, web, SECRETARIO, ALCALDE FROM ayuntamientos ORDER BY CODIGO"
    cursor.execute(sql)
    resultado=cursor.fetchall()
	
    for i in resultado:	
    
        ptext = unicode("<font size=17>" + str(i[1]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext.strip(), styles["Normal"]))
        Story.append(Spacer(1, 14))

        ptext = unicode("<font size=10>Direccion: " + str(i[2]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

        ptext = unicode("<font size=10>CP: " + str(i[3]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

        ptext = unicode("<font size=10>Telf: " + str(i[4]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

        ptext = unicode("<font size=10>FAX: " + str(i[5]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

        ptext = unicode("<font size=10>E-mail: " + str(i[6]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

        ptext = unicode("<font size=10>Web: " + str(i[7]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

        ptext = unicode("<font size=10>Secretari: " + str(i[8]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

        ptext = unicode("<font size=10>Alcalde: " + str(i[9]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

        ptext = unicode("<font size=10>- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 20))

    #Finalment creem el document PDF
    
    doc.build(Story)
    
    if len(fitxer) > 0:
        tkMessageBox.showinfo("PDF Generat", "S'ha generat la fitxa de totes les entitats a " + fitxer)
    else:
        return
    

def Export3():

    #Exportem els codis INE
    
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
 
    #doc = SimpleDocTemplate("exportacions/codis-INE.pdf",pagesize=A4,
                            #rightMargin=72,leftMargin=72,
                            #topMargin=72,bottomMargin=18)

    fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.pdf|*.*", filetypes=[('Fitxer PDF','*.pdf'),('Tots els fitxers','*.*')])
    doc = SimpleDocTemplate (fitxer,pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    
    #Creem la llista "Story" i iniciem la variable "styles"
    
    Story=[]
    styles=getSampleStyleSheet()


    # Generem el select para obtenir els codis INE i nom de les entitats
    
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT CODIGO, MUNICIPIO FROM ayuntamientos ORDER BY CODIGO"
    cursor.execute(sql)
    resultado=cursor.fetchall()
	
    for i in resultado:	

        ptext = unicode("<font size=10>" + str(i[0]) + "\t - \t" + str(i[1]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

    #Finalment creem el document PDF
    
    doc.build(Story)
    
    if len(fitxer) > 0:
        tkMessageBox.showinfo("PDF Generat", "S'ha generat la fitxa amb tots els codis INE a " + fitxer)
    else:
        return

    
def Export4():

    #Exportem els telefons de tots els ajuntaments
    
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
 
    #doc = SimpleDocTemplate("exportacions/telefons-ajuntaments.pdf",pagesize=A4,
                            #rightMargin=72,leftMargin=72,
                            #topMargin=72,bottomMargin=18)

    fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.pdf|*.*", filetypes=[('Fitxer PDF','*.pdf'),('Tots els fitxers','*.*')])
    doc = SimpleDocTemplate (fitxer,pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    
    
    #Creem la llista "Story" i iniciem la variable "styles"
    
    Story=[]
    styles=getSampleStyleSheet()


    # Generem el select para obtenir els telefons de les entitats
    
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT MUNICIPIO, TELEFONO FROM ayuntamientos ORDER BY CODIGO"
    cursor.execute(sql)
    resultado=cursor.fetchall()
	
    for i in resultado:	

        ptext = unicode("<font size=10>" + str(i[0]) + " \t - \t " + str(i[1]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))


    #Finalment creem el document PDF
    
    doc.build(Story)

    if len(fitxer) > 0:
        tkMessageBox.showinfo("PDF Generat", "S'ha generat la fitxa amb el telèfons a " + fitxer)
    else:
        return
    

def ExportTotesEntitats():
    
       	# Obrim el fitxer de text
	#Així es com estava abans quan el ficava a /exportacions ---->   f=open("exportacions/totes-les-fitxes.txt","w")
	fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.txt|*.*", filetypes=[('Fitxer TXT','*.txt'),('Tots els fitxers','*.*')])
	f = open(fitxer, "w")
	

	# Generamos el select para obtener los datos de la ficha
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT CODIGO, MUNICIPIO, DOMICILIO, CP, TELEFONO, FAX, email, web, SECRETARIO, ALCALDE, OFISAM FROM ayuntamientos ORDER BY CODIGO"
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	for i in resultado:
		f.write(str(i[1]) + '\n\n')
		f.write(str(i[2]) + '\n')
		f.write(str(i[3]) + '\n')
		f.write(str(i[4]) + '\n')
		f.write(str(i[5]) + '\n')
		f.write(str(i[6]) + '\n')
		f.write(str(i[7]) + '\n')
		f.write(str(i[8]) + '\n')
		f.write("\n\n-------------------------------------------------------------------\n\n")
			
	#tanquem el fitxer
		
	f.close()

        if len(fitxer) > 0:
        	tkMessageBox.showinfo("TXT Generat", "S'ha generat la fitxa de totes les entitats a C:/pyApps/exportacions/totes-les-fitxes.txt")
        else:
            return
                                                    
def ExportCodigosINE():
    
	# Obrim el fitxer de text
	#Així es com estava abans quan el ficava a /exportacions ----> f=open("exportacions/codis-INE.txt","w")
	fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.txt|*.*", filetypes=[('Fitxer TXT','*.txt'),('Tots els fitxers','*.*')])
	f = open(fitxer, "w")
    
	# Generamos el select para obtener los datos de la ficha
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT CODIGO, MUNICIPIO, DOMICILIO, CP, TELEFONO, FAX, email, web, SECRETARIO, ALCALDE, OFISAM FROM ayuntamientos ORDER BY CODIGO"
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	for i in resultado:
		f.write(str(i[0]) + ' - ' + str(i[1]) + '\n')

	#tanquem el fitxer
		
	f.close()

        if len(fitxer) > 0:
        	tkMessageBox.showinfo("TXT Generat", "S'ha generat la fitxa amb tots els codis INE a " + fitxer)
        else:
            return
	
def ExportCorreusEntitats():
    
	# Obrim el fitxer de text
	#Així es com estava abans quan el ficava a /exportacions ---->   f=open("exportacions/emails-ajuntaments.txt","w")
	fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.txt|*.*", filetypes=[('Fitxer TXT','*.txt'),('Tots els fitxers','*.*')])
	f = open(fitxer, "w")

	

	# Generem el select para obtenir els emails de les entitats
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT MUNICIPIO, email FROM ayuntamientos ORDER BY CODIGO"
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	for i in resultado:
		f.write(str(i[0]) + ' - ' + str(i[1]) + '\n')

	#tanquem el fitxer
		
	f.close()

        if len(fitxer) > 0:
        	tkMessageBox.showinfo("TXT Generat", "S'ha generat la fitxa amb el e-mails a " + fitxer)
        else:
            return


def Export5():

    #Exportem els e-mails de totes les entitats
    
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
 
    #doc = SimpleDocTemplate("exportacions/emails-ajuntaments.pdf",pagesize=A4,
                            #rightMargin=72,leftMargin=72,
                            #topMargin=72,bottomMargin=18)

    fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.pdf|*.*", filetypes=[('Fitxer PDF','*.pdf'),('Tots els fitxers','*.*')])
    doc = SimpleDocTemplate (fitxer,pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    
    #Creem la llista "Story" i iniciem la variable "styles"
    
    Story=[]
    styles=getSampleStyleSheet()


    # Generem el select para obtenir els emails de les entitats
    
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT MUNICIPIO, email FROM ayuntamientos ORDER BY MUNICIPIO"
    cursor.execute(sql)
    resultado=cursor.fetchall()
	
    for i in resultado:	

        ptext = unicode("<font size=10>" + str(i[0]) + " \t - \t " + str(i[1]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

    #Finalment creem el document PDF
    
    doc.build(Story)


    if len(fitxer) > 0:
        tkMessageBox.showinfo("PDF Generat", "S'ha generat la fitxa amb el e-mails a " + fitxer)
    else:
        return


def ExportTelefonsEntitats():
    
	# Obrim el fitxer de text
	#Així es com estava abans quan el ficava a /exportacions ---->   f=open("exportacions/telefons-ajuntaments.txt","w")
	fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.txt|*.*", filetypes=[('Fitxer TXT','*.txt'),('Tots els fitxers','*.*')])
	f = open(fitxer, "w")
    
	

	# Generamos el select para obtener los datos de la ficha
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT CODIGO, MUNICIPIO, DOMICILIO, CP, TELEFONO, FAX, email, web, SECRETARIO, ALCALDE, OFISAM FROM ayuntamientos ORDER BY CODIGO"
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	for i in resultado:
		f.write(str(i[1]) + ' - ' + str(i[4]) + '\n')

	#tanquem el fitxer
		
	f.close()

        if len(fitxer) > 0:
        	tkMessageBox.showinfo("TXT Generat", "S'ha generat la fitxa amb el telèfons a " + fitxer)
        else:
            return
	
	
def ExportDominisEntitats():
    
	# Obrim el fitxer de text
	#Així es com estava abans quan el ficava a /exportacions ---->   f=open("exportacions/dominis-ajuntaments.txt","w")
	fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.txt|*.*", filetypes=[('Fitxer TXT','*.txt'),('Tots els fitxers','*.*')])
	f = open(fitxer, "w")

	# Generamos el select para obtener los datos de la ficha
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT MUNICIPIO, web FROM ayuntamientos ORDER BY MUNICIPIO"
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	for i in resultado:
		f.write(str(i[0]) + ' - ' + str(i[1]) + '\n')

	#tanquem el fitxer
		
	f.close()

        if len(fitxer) > 0:
        	tkMessageBox.showinfo("TXT Generat", "S'ha generat la fitxa amb el dominis a " + fitxer)
        else:
            return


def Export6():

    #Exportem els dominis de totes les entitats
    
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
 
    #doc = SimpleDocTemplate("exportacions/dominis-ajuntaments.pdf",pagesize=A4,
                            #rightMargin=72,leftMargin=72,
                            #topMargin=72,bottomMargin=18)

    fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.pdf|*.*", filetypes=[('Fitxer PDF','*.pdf'),('Tots els fitxers','*.*')])
    doc = SimpleDocTemplate (fitxer,pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    
    #Creem la llista "Story" i iniciem la variable "styles"
    
    Story=[]
    styles=getSampleStyleSheet()


    # Generem el select per a obtenir els dominis de totes les entitats
    
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT MUNICIPIO, web FROM ayuntamientos ORDER BY MUNICIPIO"
    cursor.execute(sql)
    resultado=cursor.fetchall()
	
    for i in resultado:	

        ptext = unicode("<font size=10>" + str(i[0]) + " \t - \t " + str(i[1]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

    #Finalment creem el document PDF
    
    doc.build(Story)

    if len(fitxer) > 0:
        tkMessageBox.showinfo("PDF Generat", "S'ha generat la fitxa amb el dominis a " + fitxer)
    else:
        return


def ExportAlcaldes():
    
	# Obrim el fitxer de text
	#Així es com estava abans quan el ficava a /exportacions ----> f=open("exportacions/alcaldes-ajuntaments.txt","w")
	fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.txt|*.*", filetypes=[('Fitxer TXT','*.txt'),('Tots els fitxers','*.*')])
	f = open(fitxer, "w")
    
	

	# Generamos el select para obtener los datos de la ficha
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT MUNICIPIO, ALCALDE FROM ayuntamientos ORDER BY MUNICIPIO"
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	for i in resultado:
		f.write(str(i[0]) + ' - ' + str(i[1]) + '\n')

	#tanquem el fitxer
		
	f.close()

	if len(fitxer) > 0:
        	tkMessageBox.showinfo("TXT Generat", "S'ha generat la fitxa amb els alcaldes a " + fitxer)
        else:
            return


def Export7():

    #Exportem els alcaldes de totes les entitats
    
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
 
    #doc = SimpleDocTemplate("exportacions/alcaldes-ajuntaments.pdf",pagesize=A4,
                            #rightMargin=72,leftMargin=72,
                            #topMargin=72,bottomMargin=18)

    fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.pdf|*.*", filetypes=[('Fitxer PDF','*.pdf'),('Tots els fitxers','*.*')])
    doc = SimpleDocTemplate (fitxer,pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)

    
    #Creem la llista "Story" i iniciem la variable "styles"
    
    Story=[]
    styles=getSampleStyleSheet()


    # Generem el select per a obtenir els alcaldes de totes les entitats
    
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT MUNICIPIO, ALCALDE FROM ayuntamientos ORDER BY MUNICIPIO"
    cursor.execute(sql)
    resultado=cursor.fetchall()
	
    for i in resultado:	

        ptext = unicode("<font size=10>" + str(i[0]) + " \t - \t " + str(i[1]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

    #Finalment creem el document PDF
    
    doc.build(Story)
    
    if len(fitxer) > 0:
        tkMessageBox.showinfo("PDF Generat", "S'ha generat la fitxa amb els alcaldes a " + fitxer)
    else:
        return



def ExportSecretaris():
    
	# Obrim el fitxer de text
	#Així es com estava abans quan el ficava a /exportacions ----> f=open("exportacions/secretaris-ajuntaments.txt","w")
	fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.txt|*.*", filetypes=[('Fitxer TXT','*.txt'),('Tots els fitxers','*.*')])
	f = open(fitxer, "w")

	# Generamos el select para obtener los datos de la ficha
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT MUNICIPIO, SECRETARIO FROM ayuntamientos ORDER BY MUNICIPIO"
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	for i in resultado:
		f.write(str(i[0]) + ' - ' + str(i[1]) + '\n')

	#tanquem el fitxer
		
	f.close()

	if len(fitxer) > 0:
        	tkMessageBox.showinfo("TXT Generat", "S'ha generat la fitxa amb els secretaris a " + fitxer)
        else:
            return


def Export8():

    #Exportem els secretaris de totes les entitats
    
    from reportlab.lib.pagesizes import A4
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
 
    #doc = SimpleDocTemplate("exportacions/secretaris-ajuntaments.pdf",pagesize=A4,
                            #rightMargin=72,leftMargin=72,
                            #topMargin=72,bottomMargin=18)

    fitxer = tkFileDialog.asksaveasfilename(defaultextension="*.pdf|*.*", filetypes=[('Fitxer PDF','*.pdf'),('Tots els fitxers','*.*')])
    doc = SimpleDocTemplate (fitxer,pagesize=A4,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    
    #Creem la llista "Story" i iniciem la variable "styles"
    
    Story=[]
    styles=getSampleStyleSheet()


    # Generem el select per a obtenir els secretaris de totes les entitats
    
    db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
    cursor=db.cursor()
    sql="SELECT MUNICIPIO, SECRETARIO FROM ayuntamientos ORDER BY MUNICIPIO"
    cursor.execute(sql)
    resultado=cursor.fetchall()
	
    for i in resultado:	

        ptext = unicode("<font size=10>" + str(i[0]) + " \t - \t " + str(i[1]) + "</font>", "iso-8859-1")
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 6))

    #Finalment creem el document PDF
    
    doc.build(Story)

    if len(fitxer) > 0:
        tkMessageBox.showinfo("PDF Generat", "S'ha generat la fitxa amb els secretaris a " + fitxer)
    else:
        return

	
def InsertarIncidencia():
    
	os.system('C:\Python24\python.exe software/pyPOW.py')

def ResponsablesWeb():
    
	os.system('C:\Python24\python.exe software/pyResponsablesWeb.py')
	
def QueOfisam(variableofisam):
    
	# Generamos el select para obtener los datos de la ofisam
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT CODIGO, MUNICIPIO FROM CENTROS WHERE CODIGO='"+ variableofisam + "'"
	cursor.execute(sql)
	resultado2=cursor.fetchall()

	datos_ofisam = resultado2[0]
	return datos_ofisam[1]

def ContadorIncidencias(variablecontador):
    
	# Generamos el select para obtener el total de incidencies del municipi passat
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT COUNT(*) FROM incidencia where estat_Incidencia='1' AND entitat='" + variablecontador + "'"
	cursor.execute(sql)
	resultado3=cursor.fetchall()
	
	# Aci estic passant el resultat del count(*) que es un long (2L) a un integer short
	
	datos_contador = resultado3[0]
	sumadortotal = reduce(lambda x, y: (x<<8) + y, datos_contador)
	
	# Este es el numero de incidencias
	
	return str(sumadortotal)

def GuardarCambios():
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql1="UPDATE ayuntamientos SET DOMICILIO='" + textdireccion.get() + "' where CODIGO='" + entry0.get() + "'"
	sql2="UPDATE ayuntamientos SET CP='" + textcp.get() + "' where CODIGO='" + entry0.get() + "'"
	sql3="UPDATE ayuntamientos SET TELEFONO='" + texttelefono.get() + "' where CODIGO='" + entry0.get() + "'"
	sql4="UPDATE ayuntamientos SET FAX='" + textfax.get() + "' where CODIGO='" + entry0.get() + "'"
	sql5="UPDATE ayuntamientos SET email='" + textmail.get() + "' where CODIGO='" + entry0.get() + "'"
	sql6="UPDATE ayuntamientos SET web='" + textweb.get() + "' where CODIGO='" + entry0.get() + "'"
	sql7="UPDATE ayuntamientos SET SECRETARIO='" + textsecretario.get() + "' where CODIGO='" + entry0.get() + "'"
	sql8="UPDATE ayuntamientos SET ALCALDE='" + textalcalde.get() + "' where CODIGO='" + entry0.get() + "'"

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

	cursor.execute(sql6)
	resultado6=cursor.fetchall()

	cursor.execute(sql7)
	resultado7=cursor.fetchall()

	cursor.execute(sql8)
	resultado8=cursor.fetchall()

	print "\nAhora, tras el borrado, el ENTRY0 ES: " + entry0.get() 
	print "\n\n-----GUARDADO---\n\n"
	tkMessageBox.showinfo("Dades guardades", "Els canvis han segut guardats correctament.")
	
def LimpiarCampos():
    
	photo = PhotoImage(file="")
	textdireccion.delete(0,END)
	texttelefono.delete(0,END)
	textcp.delete(0,END)
	texttelefono.delete(0,END)
	textfax.delete(0,END)
	textmail.delete(0,END)
	textweb.delete(0,END)
	textalcalde.delete(0,END)
	textsecretario.delete(0,END)
	textofisam.delete(0,END)
			
def MuestraDatos():
    
	# Esborrem els camps dels entrys
	
	LimpiarCampos()
	
	# Generem el select per obtenir les dades de la fitxa
	
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT CODIGO, MUNICIPIO, DOMICILIO, CP, TELEFONO, FAX, email, web, SECRETARIO, ALCALDE, escut, OFISAM FROM ayuntamientos where Codigo='"+llista1.get(ACTIVE)[0:4] +"'"
	cursor.execute(sql)
	resultado=cursor.fetchall()
	
	#fiquem a una sola tupla el resultat del SELECT
	
	datos_ayuntamiento = resultado[0]
	
	print '\n\n\n' 
	print datos_ayuntamiento
	campo_codigo = datos_ayuntamiento[0]
	campo_nombre = datos_ayuntamiento[1]
	campo_direccion= datos_ayuntamiento[2]
	campo_cpostal = datos_ayuntamiento[3]
	campo_telefono = datos_ayuntamiento[4]
	campo_fax = datos_ayuntamiento[5]
	campo_mail = datos_ayuntamiento[6]
	campo_web = datos_ayuntamiento[7]
	campo_secretario = datos_ayuntamiento[8]
	campo_alcalde = datos_ayuntamiento[9]
	campo_escut = datos_ayuntamiento[10]
	campo_ofisam = datos_ayuntamiento[11]
	QueOfisam(campo_ofisam)
	campo_ofisam_comprensible = QueOfisam(campo_ofisam)
	campo_contadorincidencias = ContadorIncidencias(campo_codigo)
	
		
	# Vamos poniendo los datos
	
	entry0.delete(0,END)
	entry0.insert(0, campo_codigo)
	photo = PhotoImage(file="imatges/escuts/" + campo_escut)
	w = Label(frame_nomajunt, image=photo)
	w.photo = photo
	w.grid(row=1, column=0, sticky=W)
	varnombre.set(campo_nombre)
	textdireccion.insert(0, campo_direccion)
	textcp.insert(0, campo_cpostal)
	texttelefono.insert(0, campo_telefono)
	textfax.insert(0, campo_fax)
	textmail.insert(0, campo_mail)
	textweb.insert(0, campo_web)
	textalcalde.insert(0, campo_alcalde)
	textsecretario.insert(0, campo_secretario)
	textofisam.insert(0, campo_ofisam_comprensible)

	varescudo.set("Ruta del logo/escut: escuts/" + campo_escut)
	varincidencias.set("Incidències obertes al POW: " + str(campo_contadorincidencias))
	
#
#
# INICI
#
#
#
# Aci iniciem l'aplicacio i lo primer que mirarem es si existeixen actualitzacions
# Per a aixo, el que fem es comprovar si existeix el fitxer "actualitzacio-SI.txt"
# al repositori pyApps de Wofima.
#
#

Actualitzacions()


#######################################################################
# PANTALLA1: Pantalla principal
#######################################################################	

# El menu del programa

menubar = Menu(root)
filemenu1 = Menu(menubar, tearoff= 0)
filemenu2 = Menu(menubar, tearoff= 0)
filemenu3 = Menu(menubar, tearoff= 0)
filemenu4 = Menu(menubar, tearoff= 0)

filemenu1.add_command(label="Insertar Incidència", command=InsertarIncidencia)
filemenu1.add_command(label="Gestió Responables Webs Municipals", command=ResponsablesWeb)
filemenu1.add_separator()
filemenu1.add_command(label="Eixir del programa", command=Eixir)

filemenu2.add_command(label="Copiar")
filemenu2.add_command(label="Tallar")
filemenu2.add_command(label="Enganxar")
filemenu2.add_separator()
filemenu2.add_command(label="Guardar els canvis", command=GuardarCambios)

filemenu3.add_command(label="Fitxa de l'entitat actual (TXT)", command=ExportFitxaEntitat)
filemenu3.add_command(label="Fitxa de l'entitat actual (PDF)", command=Export1)
filemenu3.add_command(label="Fitxa de totes las entidats (TXT)", command=ExportTotesEntitats)
filemenu3.add_command(label="Fitxa de totes las entidats (PDF)", command=Export2)
filemenu3.add_command(label="Codi INE de las entidats (TXT)", command=ExportCodigosINE)
filemenu3.add_command(label="Codi INE de las entidats (PDF)", command=Export3)
filemenu3.add_command(label="Telèfons de las entitats (TXT)", command=ExportTelefonsEntitats)
filemenu3.add_command(label="Telèfons de las entitats (PDF)", command=Export4)
filemenu3.add_command(label="Emails de les entidats (TXT)", command=ExportCorreusEntitats)
filemenu3.add_command(label="Emails de les entidats (PDF)", command=Export5)
filemenu3.add_command(label="Dominis web de les entidats (TXT)", command=ExportDominisEntitats)
filemenu3.add_command(label="Dominis web de les entidats (PDF)", command=Export6)
filemenu3.add_command(label="Tots els Alcaldes (TXT)", command=ExportAlcaldes)
filemenu3.add_command(label="Tots els Alcaldes (PDF)", command=Export7)
filemenu3.add_command(label="Tots els Secretaris (TXT)", command=ExportSecretaris)
filemenu3.add_command(label="Tots els Secretaris (PDF)", command=Export8)

filemenu4.add_command(label="Sobre el programa", command=SobreElPrograma)

menubar.add_cascade(label="Arxiu", menu = filemenu1)
menubar.add_cascade(label="Editar", menu = filemenu2)
menubar.add_cascade(label="Exportar", menu = filemenu3)
menubar.add_cascade(label="Ajuda", menu = filemenu4)
root.config(menu=menubar)

# Frame superior: Afegim la imatge de l'aplicacio

frame_logo = Frame(root)
frame_logo.grid(row=0, column=1, sticky=W)

photo = PhotoImage(file="imatges/logo.gif")
w = Label(frame_logo, image=photo)
w.photo = photo
w.grid(row=1, sticky=N+W)

# Frames de baix on afegim els widgets

frame_contenedor = Frame(root, height=550)
frame_contenedor.grid(row=1, column=1)

# Frames de baix on afegim els widgets

frame_esquerra = Frame(frame_contenedor, height=450, width=200)
frame_esquerra.grid(row=1, column=1)

# llistat noms de les categories

frame_llista1 = Frame(frame_esquerra)
frame_llista1.pack(fill=Y)
scroll1 = Scrollbar(frame_llista1, bg='grey')
scroll1.pack(side=RIGHT, fill=Y)

llista1 = Listbox(frame_llista1, exportselection=0, yscrollcommand=scroll1.set, height="31", width="36", bg='white')
llista1.pack()

db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
cursor_llista1=db.cursor()
sql_llista1='SELECT CODIGO, MUNICIPIO From ayuntamientos ORDER BY CODIGO'
cursor_llista1.execute(sql_llista1)
resultado_llista1=cursor_llista1.fetchall()

for i in resultado_llista1:
    llista1.insert(END, i[0] + " - " + i[1])

scroll1.config(command=llista1.yview, relief=SUNKEN)

# Frames de baix on afegim els widgets

frame_dreta = Frame(frame_contenedor, height=450, width=400)
frame_dreta.grid(row=1, column=2, padx=20)

# Frames del nom del Ajuntament

frame_nomajunt = Frame(frame_dreta, height=50, width=350)
frame_nomajunt.grid(row=0, column=1, columnspan=3, sticky=W)

# ------------------  aci comencen els camps ---------------

entry0 = Entry(frame_nomajunt, bg='white', width=25)	
labelNombre=Label(frame_nomajunt, textvariable=varnombre, font = '{MS Sans Serif} 12')
labelNombre.grid(row=1, column=1, pady=35, sticky=E)

#Activem este camp nomes per saber la variable del CODIGO de l'ajuntament
#entry0.grid(row=2, column=2, sticky=E)
	
labeldireccion=Label(frame_dreta, text='Direcció')
labeldireccion.grid(row=2, column=1, sticky=W)
textdireccion=Entry(frame_dreta, width=30, font = '{MS Sans Serif} 10')
textdireccion.grid(row=2, column=2, sticky=W)

labelcp=Label(frame_dreta, text='CP')
labelcp.grid(row=3, column=1, sticky=W)
textcp=Entry(frame_dreta, width=8, font = '{MS Sans Serif} 10')
textcp.grid(row=3, column=2, sticky=W)

labeltelefono=Label(frame_dreta, text='Telèfon')
labeltelefono.grid(row=4, column=1, sticky=W)
texttelefono=Entry(frame_dreta, width=13, font = '{MS Sans Serif} 10')
texttelefono.grid(row=4, column=2, sticky=W)

labelfax=Label(frame_dreta, text='FAX')
labelfax.grid(row=5, column=1, sticky=W)
textfax=Entry(frame_dreta, width=13, font = '{MS Sans Serif} 10')
textfax.grid(row=5, column=2, sticky=W)

labelemail=Label(frame_dreta, text='Correu')
labelemail.grid(row=6, column=1, sticky=W)
textmail=Entry(frame_dreta, width=25, font = '{MS Sans Serif} 10')
textmail.grid(row=6, column=2, sticky=W)

labelWeb=Label(frame_dreta, text='Web')
labelWeb.grid(row=7, column=1, sticky=W)
textweb=Entry(frame_dreta, width=25, font = '{MS Sans Serif} 10')
textweb.grid(row=7, column=2, sticky=W)

# Frame dades administratives

frame_administrativo = Frame(frame_dreta, height=100, width=350)
frame_administrativo.grid(row=8, column=0, columnspan=3, pady=15, sticky=W)

grupo2 = LabelFrame(frame_administrativo, text="Dades administratives")
grupo2.grid(row=1, column=0, columnspan=3, padx=10)

labelAlcalde=Label(grupo2, text='Alcalde')
labelAlcalde.grid(row=1, column=1, sticky=W)
textalcalde=Entry(grupo2, width=30, font = '{MS Sans Serif} 10')
textalcalde.grid(row=1, column=2, sticky=W)

labelSecretario=Label(grupo2, text='Secretari')
labelSecretario.grid(row=2, column=1, sticky=W)
textsecretario=Entry(grupo2, width=30, font = '{MS Sans Serif} 10')
textsecretario.grid(row=2, column=2, sticky=W)

labelOfisam=Label(grupo2, text='OFISAM')
labelOfisam.grid(row=3, column=1, sticky=W)
textofisam=Entry(grupo2, width=30, font = '{MS Sans Serif} 10')
textofisam.grid(row=3, column=2, sticky=W)

# Frame dades adicionals

frame_adicionales = Frame(frame_dreta, height=100, width=350)
frame_adicionales.grid(row=9, column=0, columnspan=3, pady=10, sticky=W)

grupo3 = LabelFrame(frame_adicionales, text="Dades addicionals")
grupo3.grid(row=2, column=0, columnspan=3, padx=10)

labelescudo=Label(grupo3, textvariable=varescudo)
labelescudo.grid(row=1, column=1, sticky=W)

labelincidencias=Label(grupo3, textvariable=varincidencias)
labelincidencias.grid(row=2, column=1, sticky=W)

# Frame botons

frame_botons = Frame(frame_dreta, height=100, width="500")
frame_botons.grid(row=10, column=0, columnspan=5, pady=10, sticky=E)

boto1 = Button(frame_botons, text='Mostrar dades', fg="blue", command=MuestraDatos)
boto2 = Button(frame_botons, text="Guardar canvis", command=GuardarCambios)
boto1.grid(row=1, column=1, sticky=E, pady=10)
boto2.grid(row=1, column=2, padx=5, sticky=E, pady=10)

MuestraDatos()

#######################################################################
# Endavant!
#######################################################################
root.mainloop()
