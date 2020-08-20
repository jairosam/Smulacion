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

class cliente:
    
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
    
    def generar_aleatorios(self,oper2):
        aleatorio = [random.uniform(0,1) for i in range(len(oper2.df.prProducto))]
        return aleatorio
    
        
        
        

        
