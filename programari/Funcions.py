#!/usr/bin/python

def SobreElPrograma():
    tkMessageBox.showinfo("Sobre el programa", "Aquest programa serveix als responsables tecnics del SEPAM - Diputacio de Castello.\n\nPer qualsevol incidencia escriviu a grupotic@dipcas.es")

def GestioAjuntaments():
        import subprocess
        subprocess.Popen('C:\Python24\python.exe ./programari/pyGestioAjuntaments.py')
        root.destroy()
	
def InsertarIncidencia():
	import subprocess
        subprocess.Popen('C:\Python24\python.exe ./programari/pyPOW.py')
        root.destroy()

def ResponsablesWeb():
	import subprocess
        subprocess.Popen('C:\Python24\python.exe ./programari/pyResponsablesWeb.py')
        root.destroy()

def ObrimWebSEpam():
	import subprocess
        subprocess.Popen('explorer http://sepam.dipcas.es')
        root.destroy()
        
	
def Eixir():
    #i eixim del programa.
    root.destroy()
