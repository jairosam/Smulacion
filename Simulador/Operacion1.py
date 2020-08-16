#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:09:23 2020

@author: buitrago
"""


import pandas as pd
import numpy as np
import random

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
        aleatorios = []
        for i in range(1,1001):
            aleatorios.append(random.random())
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
    
    def clasificar_costo_pnc(self):
        aleatorio = self.generar_aleatorios()
        self.df["prt_extra"] = aleatorio
        self.df["tiempo_extra"] = self.mini+(self.maxi-self.mini)*self.df.prt_extra
        contador = 0
        for clase in self.df.clasPNC:
            if clase == "Desecho" or clase == "":
                self.df.prt_extra[contador], self.df.tiempo_extra[contador] = 0,0
            contador += 1
        self.df["costo_extra"] = self.df.tiempo_extra * self.costo
            
    def muestreo(self):
        aleatorio = self.generar_aleatorios()
        self.df["aleatorio_muestreo"] = aleatorio
        muestra = []
        for probabilidad in self.df.aleatorio_muestreo:
            if probabilidad > 0.5:
                muestra.append(True)
            else:
                muestra.append(False)
        self.df["muestreo"] = muestra
        for i in range(len(self.df.muestreo)):
            if self.df.muestreo[i] == True and self.df.clasPNC[i] == "Desecho":
                self.df = self.df.drop([i])
    
    def costo_total(self):
        self.df["costo_total"] = self.df.costo + self.df.costo_extra   
    
    def operar(self):
        self.clasificar_productos()
        self.calcular_costo()
        self.clasificar_pnc()
        self.clasificar_costo_pnc()
        self.muestreo()
        self.costo_total()
    
op = Operacion1(4.3,7.1,78,840,29,131)

op.operar()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    