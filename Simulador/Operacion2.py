#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:18:32 2020

@author: buitrago
"""


from Operacion1 import Operacion1
import pandas as pd
import numpy as np
import random

class Operacion2:
    
    def __init__(self, mini, maxi, costo, pc, desecho, reproceso, reparacion,
                 reclasificacion, preventa, costo_reclasificacion):
        self.mini = mini
        self.maxi = maxi
        self.costo = costo
        self.pc = pc
        self.desecho = desecho
        self.reparacion = reparacion
        self.reclasificacion = reclasificacion
        self.preventa = preventa
        self.costo_reclasificacion = costo_reclasificacion
        self.pnc = desecho + reproceso + reparacion + reclasificacion
        self.total = self.pnc + pc
        self.pr_pc = pc / self.total
        self.pr_pnc = self.pnc / self.total
        self.pr_desecho = desecho / self.pnc
        self.pr_reproceso = reproceso / self.pnc
        self.pr_reparacion = reparacion / self.pnc
        self.pr_reclasificacion = reclasificacion / self.pnc
        self.df = pd.DataFrame()    
    
    def generar_aleatorios_1(self, oper1):
        aleatorios = []
        for i in range(len(oper1.df.muestreo)):
            aleatorios.append(random.random())
        return aleatorios
    
    def generar_aleatorios_2(self):
        aleatorios = []
        for i in range(len(self.df.prProducto)):
            aleatorios.append(random.random())
        return aleatorios
    
    def clasificar_productos(self, oper1):
        aleatorio = self.generar_aleatorios_1(oper1)
        self.df["prProducto"] = aleatorio
        clas_producto = []
        for probabilidad in self.df.prProducto:
            if probabilidad > self.pr_pc:
                clas_producto.append("PNC")
            else:
                clas_producto.append("PC")
        self.df["clasProducto"] = clas_producto
    
    def clasificar_pnc(self):
        aleatorio = self.generar_aleatorios_2()
        self.df["aleatorioPNC"] = aleatorio
        clasPNC = []
        contador = 0
        for probabilidad in self.df.aleatorioPNC:
            if self.df.clasProducto[contador] == "PNC":
                if probabilidad < self.pr_desecho:
                    clasPNC.append("Desecho")
                elif probabilidad < self.pr_reproceso+self.pr_desecho:
                    clasPNC.append("Reproceso")
                elif probabilidad < self.pr_reproceso+self.pr_desecho+self.pr_reparacion:
                    clasPNC.append("Reparacion")
                else:
                    clasPNC.append("Reclasificacion")
            else:
                clasPNC.append("")
            contador += 1
        self.df["clasPNC"] = clasPNC
    
    def calcular_costo(self):
        aleatorio = self.generar_aleatorios_2()
        self.df["tiempoAleatorio"] = aleatorio
        self.df["tiempo"] = self.mini+(self.maxi-self.mini)*self.df.tiempoAleatorio
        self.df["costo"] = self.df.tiempo * self.costo

    def costo_pnc(self):
        aleatorio = self.generar_aleatorios_2()
        self.df["prt_extra"] = aleatorio
        self.df["tiempo_extra"] = self.mini+(self.maxi-self.mini)*self.df.prt_extra
        self.df.tiempo_extra[self.df.clasPNC != "Reproceso"] = 0
        self.df.prt_extra[(self.df.clasPNC != "Reproceso") & 
                          (self.df.clasPNC != "Reparacion")] = 0
        self.df["costo_extra"] = 0
        self.df.costo_extra[self.df.clasPNC == "Reproceso"] = self.df.tiempo_extra * self.costo            
        self.df.costo_extra[self.df.clasPNC == "Reclasificacion"] = 1800
        self.df.costo_extra[self.df.clasPNC == "Desecho"] = -9
        
    
    def tecnico(self, min_tecnico, max_tecnico, costo_tecnico):
        #aleatorio = self.generar_aleatorios_2()
        #self.df["prTiempos_tecnico"] = aleatorio
        #self.df.prTiempos_tecnico[self.df.clasPNC != "Reparacion"] = 0
        self.df["tiempos_tecnico"] = min_tecnico+(max_tecnico-min_tecnico)*self.df.prt_extra
        self.df.tiempos_tecnico[self.df.clasPNC != "Reparacion"] = 0
        self.df.costo_extra[self.df.clasPNC == "Reparacion"] = self.df.tiempos_tecnico * costo_tecnico 
        
    def costo_total(self):
        self.df["costo_total"] = self.df.costo + self.df.costo_extra



oper1 = Operacion1(4.3,7.1,78,840,29,131)
oper2 = Operacion2(9.1,11.4,82,927,9,36,17,11,9,1800)
oper1.operar()
oper2.clasificar_productos(oper1)
oper2.calcular_costo()
oper2.clasificar_pnc()
oper2.costo_pnc()
oper2.tecnico(5.2,7.3,53)
oper2.costo_total()















