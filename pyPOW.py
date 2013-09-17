#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Responsables: SEPAM <grupotic@dipcas.es>
#
#

from Tkinter import *
import tkMessageBox, os, datetime, MySQLdb, smtplib

root = Tk()
#root.geometry('600x480+400+200')
root.geometry('600x560+350+150')
root.title('Incidencias del POW')
root.resizable(0,0)


# Configuracio basica de la base de dades del POW
SERVIDOR = '192.168.5.3'
USUARI = 'root'
CONTRASENYA = 'lacasitos'
BASE_DE_DADES = 'ofisam'


def SobreElPrograma():
    tkMessageBox.showinfo("Sobre el programa", "Aquest programa serveix als responsables tecnics del SEPAM - Diputacio de Castello.\n\nPer qualsevol incidencia escriviu a grupotic@dipcas.es")
 
def NetejarCamps():
    #Primer de tot borrarem els camps de text
    #textusuario.delete(0,END)
    #textpassword.delete(0,END)
    textresponsable.delete(0,END)
    textobservacions.delete(1.0,END)

def MissatgeConfirmacio():
    tkMessageBox.showinfo("Incidencia registrada", "La incidencia ha sigo guardada correctamente.")

def QueMunicipio(variable):
	# Generamos el select para obtener los datos de la ofisam
	db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor=db.cursor()
	sql="SELECT CODIGO, MUNICIPIO FROM ayuntamientos WHERE CODIGO='"+ variable + "'"
	cursor.execute(sql)
	resultado2=cursor.fetchall()

	nom_del_poble = resultado2[0]
	return nom_del_poble[1]
	
def InsertaIncidencia():
	c_usuario = textusuario.get()
	c_password = textpassword.get()
	c_categoria = llista1.get(ACTIVE)[0:2]
	c_entidad = llista2.get(ACTIVE)[0:4]
	c_responsable = textresponsable.get()
	c_observacions = textobservacions.get(1.0,END)
	c_estatincidencia = '1'
	fecha= datetime.date.today()
	c_data_avui = fecha.strftime("%Y-%m-%d")
	nombre_del_municipio = QueMunicipio(c_entidad)
	
	# Primer comprobarem que el usuari i contrasenya introduits son correctes
	db2=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
	cursor2=db2.cursor()
	sql2="SELECT usuario, clave FROM seguridad where usuario='" + c_usuario + "' AND clave='" + c_password + "'"

	cursor2.execute(sql2)
	resultado2=cursor2.fetchall()
	#print "Number of rows updated: %d" % cursor2.rowcount <---- aci contem el numero de files obtingudes

	if (cursor2.rowcount != 1):            
		# Si eixe usuari no te eixa contrasenya, mostrem el seguent error
		tkMessageBox.showinfo("Error en les credencials", "Comprova que l'usuari i la contrasenya són correctes")
	else:
	    # Com les credencials son correctes, ara anirem deixant totes les dades per consola i 
		# tambe les afegim a la base de dades del POW
		# print 'Credencials correctes'

		# Traurem els resultats per la consola per tal d'anar mirant els resultats
		print "------------" + nombre_del_municipio + "-------------"
		print "Avui estem a: " + c_data_avui + "\n"
		print "Usuari: " + c_usuario + "\n"
		print "Contrasenya: " + c_password + "\n"
		print "Responsable: " + c_responsable + "\n"
		print "Observacions: " + c_observacions
		print "Categoria: " + c_categoria + "\n"
		print "Entidad: " + c_entidad + "\n \n \n"
		db1=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
		cursor1=db1.cursor()
		sql1="INSERT INTO incidencia (persona_sepam, data_inici, categoriaIncidencia, entitat, persona_entitat, descripcio, estat_Incidencia) VALUES ('" + c_usuario + "', '" + c_data_avui + "', '" + c_categoria + "', '" + c_entidad + "', '" + c_responsable + "', '" + c_observacions + "', '1')"
		#sql1="INSERT INTO incidencia (persona_sepam, data_inici, categoriaIncidencia, entitat, persona_entitat, descripcio, estat_Incidencia) VALUES ('joan', '2012-02-16', '01' , '033' , 'Amparo', 'Test de Joan', '1')"	

		cursor1.execute(sql1)
		resultado1=cursor1.fetchall()
		
		var.get()
		if (var.get() == 1):
		    # el checkbox esta clicat, aleshores ara enviarem un correu electronic
			# print 'es 1'    # <----- el checkbox esta checked
			
			# Anem a veure qui es el destinatari (la variable to)
			if (c_categoria == '01') or (c_categoria == '02') or (c_categoria == '03') or (c_categoria == '04 ') or (c_categoria == '05') or (c_categoria == '07') or (c_categoria == '08') or (c_categoria == '09') or (c_categoria == '15') or (c_categoria == '16') or (c_categoria == '28'): 
				to = 'grupotic@dipcas.es' # <---- Correu de la Seccio Informatica
			elif (c_categoria == '06') or (c_categoria == '12') or (c_categoria == '13') or (c_categoria == '14') or (c_categoria == '17') or (c_categoria == '18') or (c_categoria == '19') or (c_categoria == '20') or (c_categoria == '21') or (c_categoria == '22') or (c_categoria == '23') or (c_categoria == '24') or (c_categoria == '25') or (c_categoria == '27') or (c_categoria == '29'):
				to = 'testrela@dipcas.es' # <---- Correu de la Seccio Jurídico-Administrativa
			else:
				to = 'ccolas@dipcas.es'  # <---- Correu de la Seccio Economica (que nomes fan les categores 10 i 11)
				
			mail_user = 'pow'
			mail_pwd = 'Cambiar05'
			smtpserver = smtplib.SMTP("smtp.dipcas.es")
			smtpserver.ehlo()
			smtpserver.starttls()
			smtpserver.ehlo
			smtpserver.login(mail_user, mail_pwd)
			header = 'To:' + to + '\n' + 'From: ' + 'no_respondas' + '\n' + 'Subject:Nova incidencia al POW \n'
			print header
			msg = header + 'Hola,\n\n' + c_usuario.upper() + ' ha afegit una nova incidencia al POW. \n\nData inici: ' + c_data_avui + '\nEntitat: ' + nombre_del_municipio + '\nPersona de contacte de la Entitat: ' + c_responsable.upper() + '\nDescripcio: ' + c_observacions.upper() + '\n\nAccedeix directament des de http://sepam.dipcas.es/pow'

			smtpserver.sendmail(mail_user, to, msg)
			print '\n\n---------CORREU ELECTRONIC ENVIAT!-----------'
			smtpserver.close()

			NetejarCamps()
			MissatgeConfirmacio()
			
		else:
		    # el checkbox no esta clicat, no farem res mes aci.
			print 'es 0'   # <----- el checkbox esta checked


def Eixir():
    #i eixim del programa.
    root.destroy()	

#######################################################################
# PANTALLA1: Pantalla on afegim les incidencies
#######################################################################	

# El menu del programa
menubar = Menu(root)
filemenu1 = Menu(menubar, tearoff= 0)
filemenu2 = Menu(menubar, tearoff= 0)
filemenu3 = Menu(menubar, tearoff= 0)

filemenu1.add_command(label="Inserta Incidencia", command=InsertaIncidencia)
filemenu1.add_separator()
filemenu1.add_command(label="Eixir de les incidencias", command=Eixir)

filemenu2.add_command(label="Copiar")
filemenu2.add_command(label="Tallar")
filemenu2.add_command(label="Enganxar")
filemenu2.add_separator()
filemenu2.add_command(label="Netejar tots els camps", command=NetejarCamps)

filemenu3.add_command(label="Sobre el programa", command=SobreElPrograma)

menubar.add_cascade(label="Arxiu", menu = filemenu1)
menubar.add_cascade(label="Editar", menu = filemenu2)
menubar.add_cascade(label="Ajuda", menu = filemenu3)
root.config(menu=menubar)


# Frame superior: Afegim la imatge de l'aplicacio
frame_logo = Frame(root)
frame_logo.grid(row=0, column=1, sticky=N)

photo = PhotoImage(file="imatges/logo.gif")
w = Label(frame_logo, image=photo)
w.photo = photo
w.grid(row=0, sticky=N)

# Frames de baix on afegim els widgets
frame_baix = Frame(root)
frame_baix.grid(row=2, column=1, pady=52)

# frame esquerra 
frame_esquerra = Frame(frame_baix)
frame_esquerra.grid(row=1, column=1)

# frame dreta
frame_dreta = Frame(frame_baix)
frame_dreta.grid(row=1, column=2)

#camp del nom d'usuari
grupo1 = LabelFrame(frame_esquerra, text="Usuari")
grupo1.grid(row=1, column=1)
textusuario = Entry(grupo1, bg='white', width=38)
textusuario.grid(row=1, column=1, pady=5)

#camp de la contrasenya d'usuari
grupo2 = LabelFrame(frame_dreta, text="Contrasenya")
grupo2.grid(row=1, column=1)
textpassword = Entry(grupo2, bg='white', width=38)
textpassword.grid(row=1, column=1, pady=5)

# frame baix esquerra
frame_baixesquerra = Frame(frame_baix, width=300, height=100)
frame_baixesquerra.grid(row=2, column=1)

# frame baix dreta
frame_baixdreta = Frame(frame_baix, width=300, height=100)
frame_baixdreta.grid(row=2, column=2)

# llistat noms de les categories
frame_llista1 = Frame(frame_baixesquerra)
frame_llista1.pack()
scroll1 = Scrollbar(frame_llista1, bg='grey')
scroll1.pack(side=RIGHT, fill=Y)

llista1 = Listbox(frame_llista1, exportselection=0, yscrollcommand=scroll1.set, height="10", width="36", bg='white')
llista1.pack()

db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
cursor_llista1=db.cursor()
sql_llista1='SELECT codi, descripcio From categoriaIncidencia ORDER BY codi'
cursor_llista1.execute(sql_llista1)
resultado_llista1=cursor_llista1.fetchall()

for i in resultado_llista1:
    llista1.insert(END, i[0] + " - " + i[1])

scroll1.config(command=llista1.yview, relief=SUNKEN)

# llistat nom dels ajuntaments
frame_llista2 = Frame(frame_baixdreta)
frame_llista2.pack()
scroll2 = Scrollbar(frame_llista2, bg='grey')
scroll2.pack(side=RIGHT, fill=Y)

llista2 = Listbox(frame_llista2, exportselection=0, yscrollcommand=scroll2.set, height="10", width="36", bg='white')
llista2.pack()

db=MySQLdb.connect(host=SERVIDOR,user=USUARI, port=4406, passwd=CONTRASENYA,db=BASE_DE_DADES)
cursor_llista2=db.cursor()
sql_llista2='SELECT CODIGO, MUNICIPIO From ayuntamientos ORDER BY CODIGO'
cursor_llista2.execute(sql_llista2)
resultado_llista2=cursor_llista2.fetchall()

for i in resultado_llista2:
    llista2.insert(END, i[0] + " - " + i[1])

scroll2.config(command=llista2.yview, relief=SUNKEN)

# frame baix esquerra 2
frame_baixesquerra2 = Frame(frame_baix, width=300, height=100)
frame_baixesquerra2.grid(row=4, column=1, pady=30, sticky=W)

# frame baix dreta 2
frame_baixdreta2 = Frame(frame_baix, width=100)
frame_baixdreta2.grid(row=4, column=2, pady=24, sticky=N)

grupo1 = LabelFrame(frame_baixesquerra2, text="Persona de contacte")
grupo1.grid(row=1, column=1)
textresponsable = Entry(grupo1, bg='white', width=33)
textresponsable.grid(row=1, column=2, pady=5)

labelobservacions = Label(frame_baixdreta2, text='Descripcio: ')
labelobservacions.grid(row=2, column=1, sticky=W)
textobservacions = Text(frame_baixdreta2, width=25, height=3, bg= 'white', font= "size=38")
textobservacions.grid(row=3, column=1)

var = IntVar() #pasem la variable que deixem al checkbox a un intenger, perque dalt fem un if (1 is checked, 0 is unchecked)
checkemail = Checkbutton(frame_baixdreta2, text="Enviar e-mail a l'area corresponent del SEPAM", variable=var)
checkemail.grid(row=4, column=1, pady=5, sticky=W)

# Els dos botons al frame baix esquerra 2
frame_botons1 = Frame(frame_baixesquerra2)
frame_botons1.grid(row=5, column=1, sticky=W)

boto1 = Button(frame_botons1, text='Insertar Incidencia', fg="blue", command=InsertaIncidencia)
boto2 = Button(frame_botons1, text="Eixir", command=Eixir)
boto1.grid(row=1, column=1, pady=20)
boto2.grid(row=1, column=2, pady=20)

#######################################################################
# Endavant!
#######################################################################	
root.mainloop()
