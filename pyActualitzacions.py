#!/usr/bin/python
# -*- encoding: utf-8 -*-
# Responsables: SEPAM <grupotic@dipcas.es>
#
# Actualitzacions automàtiques de "pyGestioAjuntaments.py"
# -------------------------------------------------------------------
#
# Comprovem si existeix el fitxer actualitzacio-SI.txt a Wofima
# Inmediatament després comprova si el programa està a la última versió (v0.x.txt).
# Si està a la última no fa res, però si no es sincronitza automàticament amb la versió última de Wofima.
#
# PER A PRÒXIMES VERSIONS: CAL CANVIAR EL FITXER AMB EL NOM DE LA NOVA VERSIO


from Tkinter import *
import os

def Actualizar():
    os.system("//wofima/sepam/scentrales/0_GENERAL/PKG/pyApps/actualizador.bat")

def HayActualizaciones():

    if os.path.isfile("C:/pyApps/versio.txt"):
        print "existe"
        f1 = open("C:/pyApps/versio.txt")
        contenido1 = f1.readline()
        print contenido1

        f2 = open("//wofima/sepam/scentrales/general/PKG/pyApps/versio.txt")
        contenido2 = f2.readline()
        print contenido2

        if contenido1 < contenido2:
            print "ES MENOR"
            Actualizar()
            f3=open("C:/pyApps/versio.txt","w")
            f3.write(contenido2)
            f3.close()
            print "tras la actualizacion acabamos de crear C:\pyApps\versio.txt"
            return
            
        else:
            print "NO, es igual"

    else:
        
        print "no existe"
        f2 = open("//wofima/sepam/scentrales/general/PKG/pyApps/versio.txt")
        contenido2 = f2.readline()

        
        f3=open("C:/pyApps/versio.txt","w")
        f3.write(contenido2)
        f3.close()
        print "como no existia lo acabamos de crear C:\pyApps\versio.txt"
        Actualizar()

        
#
# INICI
#

HayActualizaciones()

