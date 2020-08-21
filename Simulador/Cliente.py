#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:52:11 2020

@author: buitrago
"""


from Operacion2 import Operacion2
from Operacion1 import Operacion1
import random
import pandas as pd
import numpy as np

class Cliente:
    
    def __init__(self, vuelve, no_vuelve, reclama, no_reclama):
        self.vuelve = vuelve
        self.no_vuelve = no_vuelve
        self.reclama = reclama
        self.no_reclama = no_reclama
        self.pr_vuelva = vuelve/(vuelve+no_vuelve)
        self.pr_no_vuelva = no_vuelve/(vuelve+no_vuelve)
        self.pr_reclama = reclama/(reclama+no_reclama)
        self.pr_no_reclama = no_reclama/(reclama+no_reclama)
        self.pr_reclama_vuelve = self.pr_reclama * self.pr_vuelva
        self.pr_no_reclama_vuelve = self.pr_no_reclama * self.pr_vuelva
        self.df = pd.DataFrame()
    
    def generar_aleatorios(self,numero):
        aleatorio = [random.uniform(0,numero) for i in range(len(self.df.clas_oper1))]
        return aleatorio
    
    # Un producto se considera no conforme si no cumple los requisitos de alguna de las
    # 2 operaciones

    def asignar_productos(self,oper1,oper2):
        self.df["clas_oper1"] = oper1.df.clasPNC.to_numpy()
        self.df["clas_oper2"] = oper2.df.clasPNC.to_numpy()
        self.df["costo_operacion1"] = oper1.df.costo_total.to_numpy()
        self.df["costo_operacion2"] = oper2.df.costo_total.to_numpy()
        self.df["costo_total_produccion"] = self.df.costo_operacion1 + self.df.costo_operacion2
         
        
    def filtrar_productos(self,oper1,oper2):
        conformidad = []
        for i in range(len(self.df.clas_oper1)):
            if self.df.clas_oper1[i] == "Desecho":
                conformidad.append("PNC")
            elif oper2.df.clasProducto[i] == "PNC" and oper2.df.muestreo[i] == False:
                conformidad.append("PNC")
            else:
                conformidad.append("PC")
        self.df["conformidad"] = conformidad
        
    
    def clasificar_llegada(self,oper2):
        llega = []
        for i in range(len(oper2.df.muestreo)):
            if oper2.df.muestreo[i] == True and oper2.df.clasPNC[i] == "Desecho":
                llega.append(False)
            else:
                llega.append(True)
        self.df["llega"] = llega
    
    def vuelta_clientes(self):
        aleatorio = self.generar_aleatorios(1)
        self.df["prVuelva"] = aleatorio
        vuelva = []
        for probabilidad in self.df.prVuelva:
            if probabilidad < self.pr_vuelva:
                vuelva.append(True)
            else:
                vuelva.append(False)
        self.df["vuelve"] = vuelva
        self.df.vuelve[self.df.conformidad == "PC"] = False    
    
    def reclamo_clientes(self):
        aleatorio = self.generar_aleatorios(self.pr_reclama_vuelve + self.pr_no_reclama_vuelve)
        self.df["prReclamo"] = aleatorio
        reclama = []
        for probabilidad in self.df.prReclamo:
            if probabilidad < self.pr_reclama_vuelve:
                reclama.append(True)
            else:
                reclama.append(False)
        self.df["Reclama"] = reclama
        self.df.Reclama[(self.df.conformidad == "PC") | (self.df.vuelve == False)] = False
    
    def calculo_costo_clientes(self):
        costo_cliente = []
        for i in range(len(self.df.Reclama)):
            if self.df.conformidad[i] == "PNC":
                if self.df.vuelve[i] == False:
                    costo_cliente.append(170000)
                if self.df.vuelve[i] == True and self.df.Reclama[i] == True:
                    costo_cliente.append(60000)
                if self.df.vuelve[i] == True and self.df.Reclama[i] == False:
                    costo_cliente.append(0)
            else:
                costo_cliente.append(0)
        self.df["costo_cliente"] = costo_cliente
    
    def costo_total_proceso(self):
        self.df["costo_proceso"] = self.df.costo_cliente + self.df.costo_total_produccion
    
    def ganancia_proceso(self):
        self.df["ganancia_proceso"] = 2800 - self.df.costo_proceso
    
    
#for i in range(20):
oper1 = Operacion1(4.3,7.1,78,840,29,131)
oper2 = Operacion2(9.1,11.4,82,927,9,36,17,11,9,1800)
#operacion 1
oper1.clasificar_productos()
oper1.calcular_costo()
oper1.clasificar_pnc()
oper1.costo_pnc()
oper1.muestreo(2.5,3.2,7)
oper1.costo_total()
#operacion 2 
oper2.clasificar_productos(oper1)
oper2.calcular_costo()
oper2.clasificar_pnc()
oper2.costo_pnc()
oper2.tecnico(5.2,7.3,53)
oper2.muestreo(3.7,9.9,7)
oper2.costo_total()
#    oper1.df.to_excel("Replica1/Replica_operacion_1_{}.xlsx".format(i), sheet_name="Replica")
#    oper2.df.to_excel("Replica2/Replica_operacion_2_{}.xlsx".format(i), sheet_name="Replica")
cliente = Cliente(103,35,29,4)
cliente.asignar_productos(oper1,oper2)
cliente.clasificar_llegada(oper2)
cliente.filtrar_productos(oper1,oper2)      
cliente.vuelta_clientes()
cliente.reclamo_clientes()        
cliente.calculo_costo_clientes()        
cliente.costo_total_proceso()
cliente.ganancia_proceso()        
                
        
import matplotlib.pyplot as plt
plt.title("Costo vs ganancia")
plt.xlabel("costo")
plt.ylabel("ganancia")
plt.plot(cliente.df.costo_proceso, cliente.df.ganancia_proceso)      
        
        
        
        
        
        
        
        
        

        
