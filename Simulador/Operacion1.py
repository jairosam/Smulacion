#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:09:23 2020

@author: buitrago
"""


import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

class Operacion1:
    
    def __init__(self, mini, maxi, costo, pc, desecho, reproceso):
        self.mini = mini
        self.maxi = maxi
        self.costo = costo
        self.pc = pc
        self.desecho = desecho
        self.reproceso = reproceso
        self.pnc = desecho + reproceso
        self.total = pc+self.pnc
        self.pr_pc = pc/self.total
        self.pr_pnc = self.pnc/self.total
        self.pr_desecho = self.desecho/self.pnc
        self.pr_reproceso = self.reproceso/self.pnc
        self.df = pd.DataFrame()
    
    def generar_aleatorios(self):
        aleatorios = [random.uniform(0,1) for i in range(1000)]
        return aleatorios
    
    def clasificar_productos(self):
        aleatorio = self.generar_aleatorios()
        clas_producto = []
        self.df["prProducto"] = aleatorio
        for probabilidad in aleatorio:
            if probabilidad > self.pr_pc:
                clas_producto.append("PNC")
            else:
                clas_producto.append("PC")
        self.df["clasProducto"] = clas_producto

    def calcular_costo(self):
        aleatorio = self.generar_aleatorios()
        self.df["tiempoAleatorio"] = aleatorio
        self.df["tiempo"] = self.mini+(self.maxi-self.mini)*self.df.tiempoAleatorio
        self.df["costo"] = self.df.tiempo * self.costo

    def clasificar_pnc(self):
        aleatorio = self.generar_aleatorios()
        self.df["aleatorioPNC"] = aleatorio
        clas_pnc = []
        contador = 0
        for probabilidad in self.df.aleatorioPNC:
            if self.df.clasProducto[contador] == "PNC":
                if probabilidad > self.pr_desecho:
                    clas_pnc.append("Reproceso")
                else:
                    clas_pnc.append("Desecho")
            else:
                clas_pnc.append("")
            contador += 1
        self.df["clasPNC"] = clas_pnc
    
    def costo_pnc(self):
        aleatorio = self.generar_aleatorios()
        self.df["prt_extra"] = aleatorio
        self.df["tiempo_extra"] = self.mini+(self.maxi-self.mini)*self.df.prt_extra
        self.df.prt_extra[(self.df.clasPNC == "Desecho") | (self.df.clasPNC == "")] = 0
        self.df.tiempo_extra[(self.df.clasPNC == "Desecho") | (self.df.clasPNC == "")] = 0
        self.df["costo_extra"] = self.df.tiempo_extra * self.costo
            
    def muestreo(self, mini, maxi, costo):
        aleatorio = self.generar_aleatorios()
        self.df["aleatorio_muestreo"] = aleatorio
        muestra = []
        for probabilidad in self.df.aleatorio_muestreo:
            if probabilidad > 0.5:
                muestra.append(True)
            else:
                muestra.append(False)
        self.df["muestreo"] = muestra
        aleatorio_tiempo_muestreo = self.generar_aleatorios()
        self.df["aleatorio_tiempo_muestreo"] = aleatorio_tiempo_muestreo
        self.df["tiempos_muestreo"] = mini+(maxi-mini)*self.df.aleatorio_tiempo_muestreo
        for i in range(len(self.df.muestreo)):
            if self.df.muestreo[i] == False and self.df.clasPNC[i] == "Reproceso":
                self.df.prt_extra[i], self.df.tiempo_extra[i], self.df.costo_extra[i] = 0,0,0
            if self.df.muestreo[i] == False:
                self.df.tiempos_muestreo[i], self.df.aleatorio_tiempo_muestreo[i] = 0,0
            if self.df.muestreo[i] == True and self.df.clasPNC[i] == "Desecho":
                self.df = self.df.drop([i])
        self.df = self.df.reset_index(drop=True)
        self.df["costo_muestreo"] = costo*self.df.tiempos_muestreo        
    
    def costo_total(self):
        self.df["costo_total"] = self.df.costo + self.df.costo_extra + self.df.costo_muestreo  
 
    
    
    
    
    
    
    