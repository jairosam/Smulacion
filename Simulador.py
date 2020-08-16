#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 11:17:31 2020

@author: buitrago
"""


import pandas as pd
import numpy as np
import random

def generar_aleatorios():
    aleatorios = []
    for i in range(1,1001):
        aleatorios.append(random.random())
    return aleatorios

minimo = 4.3 #float(input("Ingrese el valor minimo (min/und): "))
maximo = 7.1 #float(input("Ingrese el valor maximo (min/und): "))

costo = 78 #float(input("Ingrese el costo ($/min): "))

pc = 840 #int(input("Ingrese el producto conforme estimado: ")) #Producto Conforme
desecho = 29 #int(input("Ingrese el producto desechable estimado: "))
reproceso = 131 #int(input("Ingrese el producto para reproceso estimado: "))
pnc = desecho + reproceso #producto no conforme
total = pc + pnc 

pr_pc = pc / total #probabilidad de producto conforme 
pr_pnc = pnc / total #probabilidad de producto no conforme
pr_desecho = desecho / pnc #probabilidad de producto desecho
pr_reproceso = reproceso / pnc #probabilidad de producto para reproceso

replicas = 5

for i in range(1,replicas+1):

    oper1 = pd.DataFrame()
    aleatorio = generar_aleatorios() #clasifica los productos en conformes y no conformes
    clas_producto = [] #almacena la clasificación de los productos 
    
    for probabilidad in aleatorio:
        if probabilidad > pr_pc:
            clas_producto.append("PNC")
        else:
            clas_producto.append("PC")
    
    oper1["prProducto"] = aleatorio
    oper1["clasProducto"] = clas_producto
    
    aleatorio = generar_aleatorios()
    oper1["tiempoAleatorio"] = aleatorio
    oper1["tiempo"] = minimo+(maximo-minimo)*oper1.tiempoAleatorio
    oper1["costo1"] = oper1.tiempo * costo
    
    aleatorio = generar_aleatorios()
    
    oper1["aleatorioPNC"] = aleatorio
    clas_pnc = []
    contador = 0
    
    for probabilidad in oper1.aleatorioPNC:
        if oper1.clasProducto[contador] == "PNC":
            if probabilidad > pr_desecho:
                clas_pnc.append("Reproceso")
            else:
                clas_pnc.append("Desecho")
        else:
            clas_pnc.append("")
        contador += 1
    
    oper1["clasPNC"] = clas_pnc
    
    oper1.to_csv("replica " + str(i))