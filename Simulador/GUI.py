from Operacion2 import Operacion2
from Operacion1 import Operacion1
from Cliente import Cliente

import numpy as np

from tkinter import *
from tkinter import ttk

window = Tk()

title_label = Label(window)

op1_frame = Frame(window)
op2_frame = Frame(window)
sim_frame = Frame(window)

op1_label = Label(op1_frame)
op1_label_min = Label(op1_frame)
op1_label_max = Label(op1_frame)
op1_label_costo = Label(op1_frame)
op1_label_und = Label(op1_frame)

op2_label = Label(op2_frame)
op2_label_min = Label(op2_frame)
op2_label_max = Label(op2_frame)
op2_label_costo = Label(op2_frame)
op2_label_und = Label(op2_frame)

sim_replicas_label = Label(sim_frame)
sim_replicas = ttk.Combobox(sim_frame)
sim_button = Button(sim_frame)

matriz_media = []
matriz_mediana = []
matriz_desv_est = []
matriz_var = []

#Interfaz con posiciones absolutas
def interfaz():
    # Titulo y tamaño
    window.title("Simulacion de Monte Carlo")
    window.resizable(0,0)
    window.geometry("600x500")
    window.config(bg = "#F9F9F9")

    title_label.config(text = "Simulacion de Monte Carlo", font = ("Candara", 28), bg = "#F9F9F9")
    title_label.place(x = 80, y = 10)

    op_frame()
    simulation_frame()
        

def op_frame():
    op1_frame.config(width = 180, height = 180, bg = "white", highlightbackground = "#B6B6B6", highlightthickness = 1)
    op1_frame.place(x = 100, y = 80)
    
    op2_frame.config(width = 180, height = 180, bg = "white", highlightbackground = "#B6B6B6", highlightthickness = 1)
    op2_frame.place(x = 300, y = 80)
        

def labels_op1(mini, maxi, costo, und):
    op1_label.config(text = "Operacion 1", font = ("Verdana", 16), bg = "white")
    op1_label.place(x = 25, y = 2)

    time_label = Label(op1_frame, text = "Tiempo", font = ("Cambria"), bg = "white")
    time_label.place(x = 10, y = 40)
    costo_label = Label(op1_frame, text = "Costo $/Min", font = ("Cambria"), bg = "white")
    costo_label.place(x = 10, y = 115)
    und_label = Label(op1_frame, text = "Unidades", font = ("Cambria"), bg = "white")
    und_label.place(x = 10, y = 140)

    min_label = Label(op1_frame, text = "Min M/U", font = ("Cambria"), bg = "white")
    min_label.place(x = 30, y = 65)
    max_label = Label(op1_frame, text = "Max M/U", font = ("Cambria"), bg = "white")
    max_label.place(x = 30, y = 90)
    
    op1_label_min.config(text = mini, font = ("Cambria"), bg = "white")
    op1_label_min.place(x = 120, y = 65)
    op1_label_max.config(text = maxi, font = ("Cambria"), bg = "white")
    op1_label_max.place(x = 120, y = 90)
    op1_label_costo.config(text = costo, font = ("Cambria"), bg = "white")
    op1_label_costo.place(x = 120, y = 115)
    op1_label_und.config(text = und, font = ("Cambria"), bg = "white")
    op1_label_und.place(x = 120, y = 140)
        

def labels_op2(mini, maxi, costo, und):
    op2_label.config(text = "Operacion 2", font = ("Verdana", 16), bg = "white")
    op2_label.place(x = 25, y = 2)

    time_label = Label(op2_frame, text = "Tiempo", font = ("Cambria"), bg = "white")
    time_label.place(x = 10, y = 40)
    costo_label = Label(op2_frame, text = "Costo $/Min", font = ("Cambria"), bg = "white")
    costo_label.place(x = 10, y = 115)
    und_label = Label(op2_frame, text = "Unidades", font = ("Cambria"), bg = "white")
    #und_label.place(x = 10, y = 140)

    min_label = Label(op2_frame, text = "Min M/U", font = ("Cambria"), bg = "white")
    min_label.place(x = 30, y = 65)
    max_label = Label(op2_frame, text = "Max M/U", font = ("Cambria"), bg = "white")
    max_label.place(x = 30, y = 90)
    
    op2_label_min.config(text = mini, font = ("Cambria"), bg = "white")
    op2_label_min.place(x = 120, y = 65)
    op2_label_max.config(text = maxi, font = ("Cambria"), bg = "white")
    op2_label_max.place(x = 120, y = 90)
    op2_label_costo.config(text = costo, font = ("Cambria"), bg = "white")
    op2_label_costo.place(x = 120, y = 115)
    op2_label_und.config(text = und, font = ("Cambria"), bg = "white")
    #op2_label_und.place(x = 120, y = 140)

def simulation_frame():
    sim_frame.config(width = 380, height = 120, bg = "white", highlightbackground = "#B6B6B6", highlightthickness = 1)
    sim_frame.place(x = 100, y = 300)
    
    sim_replicas_label.config(text = "Numero de replicas", font = ("Calibri"), bg = "white")
    sim_replicas_label.place(x = 10, y = 10)
    sim_replicas.config(values = [5], width = 10, font = ("Calibri", 12))
    sim_replicas.place(x = 160, y = 10)
    sim_replicas.current(0)

    sim_button.config(text = "Iniciar Simulacion", font = ("Verdana", 12, "bold"), fg = "#F8F8F8", bg = "#1A63F5", command = iniciar_simulacion)
    sim_button.place(x = 100, y = 50)
    
def post_simulation():
    sim_finished = Label(sim_frame, text = "Simulacion Finalizada", font = ("Verdana", 16), bg = "white")
    sim_finished.place(x = 70, y = 10)
    
    sim_button.config(text = "Ver Estadisticas", font = ("Verdana", 12, "bold"), fg = "#F8F8F8", bg = "#1A9E50", command = ventana_estadisticas)
    sim_button.place(x = 110, y = 60)
    
def ventana_estadisticas():
    newWindow = Toplevel(window)
    newWindow.title("Estadisticas") 
    newWindow.geometry("1100x850")
    
    st_title = Label(newWindow, text = "Estadisticas de las Replicas", font = ("Candara", 28))
    st_title.place(x = 60, y = 20)
    
    # Media
    media_label = Label(newWindow, text = "Media", font = ("Verdana", 14))
    media_frame = Frame(newWindow, bg = "white", highlightbackground = "#B6B6B6", highlightthickness = 1)
    media_label.place(x = 50, y = 100)
    media_frame.place(x = 50, y = 140)
    
    total_rows = len(matriz_media) 
    total_columns = len(matriz_media[0]) 
    
    for i in range(total_rows): 
        for j in range(total_columns): 
            if i == 0:
                st_table_media = Entry(media_frame, width = 20, font=("Arial", 11, "bold"))
            else:
                st_table_media = Entry(media_frame, width = 23, font=("Arial", 10)) 
            st_table_media.grid(row=i, column=j) 
            st_table_media.insert(END, matriz_media[i][j])
            
    # Mediana
    mediana_label = Label(newWindow, text = "Mediana", font = ("Verdana", 14))
    mediana_frame = Frame(newWindow, bg = "white", highlightbackground = "#B6B6B6", highlightthickness = 1)
    mediana_label.place(x = 50, y = 280)
    mediana_frame.place(x = 50, y = 320)
    
    total_rows = len(matriz_mediana) 
    total_columns = len(matriz_mediana[0]) 
    
    for i in range(total_rows): 
        for j in range(total_columns): 
            if i == 0:
                st_table_mediana = Entry(mediana_frame, width = 20, font=("Arial", 11, "bold"))
            else:
                st_table_mediana = Entry(mediana_frame, width = 23, font=("Arial", 10)) 
            st_table_mediana.grid(row=i, column=j) 
            st_table_mediana.insert(END, matriz_mediana[i][j])
            
    # Desviacion Estandar
    desv_est_label = Label(newWindow, text = "Desviacion Estandar", font = ("Verdana", 14))
    desv_est_frame = Frame(newWindow, bg = "white", highlightbackground = "#B6B6B6", highlightthickness = 1)
    desv_est_label.place(x = 50, y = 460)
    desv_est_frame.place(x = 50, y = 500)
    
    total_rows = len(matriz_desv_est) 
    total_columns = len(matriz_desv_est[0]) 
    
    for i in range(total_rows): 
        for j in range(total_columns): 
            if i == 0:
                st_table_desv_est = Entry(desv_est_frame, width = 20, font=("Arial", 11, "bold"))
            else:
                st_table_desv_est = Entry(desv_est_frame, width = 23, font=("Arial", 10)) 
            st_table_desv_est.grid(row=i, column=j) 
            st_table_desv_est.insert(END, matriz_desv_est[i][j])
            
    # Varianza
    var_label = Label(newWindow, text = "Varianza", font = ("Verdana", 14))
    var_frame = Frame(newWindow, bg = "white", highlightbackground = "#B6B6B6", highlightthickness = 1)
    var_label.place(x = 50, y = 640)
    var_frame.place(x = 50, y = 680) 
    
    total_rows = len(matriz_var) 
    total_columns = len(matriz_var[0]) 
    
    for i in range(total_rows): 
        for j in range(total_columns): 
            if i == 0:
                st_table_var = Entry(var_frame, width = 20, font=("Arial", 11, "bold"))
            else:
                st_table_var = Entry(var_frame, width = 23, font=("Arial", 10)) 
            st_table_var.grid(row=i, column=j) 
            st_table_var.insert(END, matriz_var[i][j])

        
def iniciar_simulacion():
    matriz_media.append(
        ["Replica",
         "Costo Operacion 1",
         "Costo Operacion 2",
         "Costo Total Produccion",
         "Costo proceso",
         "Ganancia Proceso"])
    matriz_mediana.append(
        ["Replica",
         "Costo Operacion 1",
         "Costo Operacion 2",
         "Costo Total Produccion",
         "Costo proceso",
         "Ganancia Proceso"])
    matriz_desv_est.append(
        ["Replica",
         "Costo Operacion 1",
         "Costo Operacion 2",
         "Costo Total Produccion",
         "Costo proceso",
         "Ganancia Proceso"])
    matriz_var.append(
        ["Replica",
         "Costo Operacion 1",
         "Costo Operacion 2",
         "Costo Total Produccion",
         "Costo proceso",
         "Ganancia Proceso"])
    for i in range(int(sim_replicas.get())):
        # Operaciones
        oper1 = Operacion1(op1_min, op1_max, op1_costo, op1_pc, op1_desecho, op1_reproceso)
        oper2 = Operacion2(op2_min, op2_max, op2_costo, op2_pc, op2_desecho, op2_reproceso, op2_reparacion, op2_reclasificacion, op2_preventa, op2_reclasificacion_precio)
        cliente = Cliente(cliente_vuelve, cliente_no_vuelve, cliente_reclama, cliente_no_reclama)
        
        #operacion 1
        oper1.clasificar_productos()
        oper1.calcular_costo()
        oper1.clasificar_pnc()
        oper1.costo_pnc()
        oper1.muestreo(op1_muestra_min, op1_muestra_max, op1_muestra_costo)
        oper1.costo_total()
        #operacion 2 
        oper2.clasificar_productos(oper1)
        oper2.calcular_costo()
        oper2.clasificar_pnc()
        oper2.costo_pnc()
        oper2.tecnico(op2_tecnico_min, op2_tecnico_max, op2_tecnico_costo)
        oper2.muestreo(op2_muestra_min, op2_muestra_max, op2_muestra_costo)
        oper2.costo_total()
        
        cliente.asignar_productos(oper1,oper2)
        cliente.clasificar_llegada(oper2)
        cliente.filtrar_productos(oper1,oper2)      
        cliente.vuelta_clientes()
        cliente.reclamo_clientes()        
        cliente.calculo_costo_clientes()        
        cliente.costo_total_proceso()
        cliente.ganancia_proceso() 
        
        #cliente.df.to_excel("Replicas/Replica_cliente_{}.xlsx".format(i), sheet_name="Replica")
        
        matriz_media.append(
            [str(i+1),
             round(cliente.df.costo_operacion1.mean(), 3),
             round(cliente.df.costo_operacion2.mean(), 3),
             round(cliente.df.costo_total_produccion.mean(), 3),
             round(cliente.df.costo_proceso.mean(), 3),
             round(cliente.df.ganancia_proceso.mean(), 3)])
        
        matriz_mediana.append(
            [str(i+1),
             round(cliente.df.costo_operacion1.median(), 3),
             round(cliente.df.costo_operacion2.median(), 3),
             round(cliente.df.costo_total_produccion.median(), 3),
             round(cliente.df.costo_proceso.median(), 3),
             round(cliente.df.ganancia_proceso.median(), 3)])
        
        matriz_desv_est.append(
            [str(i+1),
             round(cliente.df.costo_operacion1.std(), 3),
             round(cliente.df.costo_operacion2.std(), 3),
             round(cliente.df.costo_total_produccion.std(), 3),
             round(cliente.df.costo_proceso.std(), 3),
             round(cliente.df.ganancia_proceso.std(), 3)])
        
        matriz_var.append(
            [str(i+1),
             round(cliente.df.costo_operacion1.var(), 3),
             round(cliente.df.costo_operacion2.var(), 3),
             round(cliente.df.costo_total_produccion.var(), 3),
             round(cliente.df.costo_proceso.var(), 3),
             round(cliente.df.ganancia_proceso.var(), 3)])
        
        op2_label_und.config(text = len(oper1.df.muestreo))
        
    #sim_button.config(state=DISABLED, disabledforeground = "#CCCCCC",)
    sim_replicas_label.place_forget()
    sim_replicas.place_forget()
    sim_button.place_forget()
    
    post_simulation()
                

# Main

# Variables Operacion 1
op1_min = 4.3
op1_max = 7.1
op1_costo = 78
op1_pc = 840
op1_desecho = 29
op1_reproceso = 131
op1_unidades = op1_pc + op1_desecho + op1_reproceso

op1_muestra_min = 2.5
op1_muestra_max = 3.2
op1_muestra_costo = 7

# Variables Operacion 2
op2_min = 9.1
op2_max = 11.4
op2_costo = 82
op2_pc = 927
op2_desecho = 9
op2_reproceso = 36
op2_reparacion = 17
op2_reclasificacion = 11
op2_preventa = 9
op2_reclasificacion_precio = 1800

op2_muestra_min = 3.7
op2_muestra_max = 9.9
op2_muestra_costo = 7

op2_tecnico_min = 5.2
op2_tecnico_max = 7.3
op2_tecnico_costo = 53

# Variables Cliente
cliente_vuelve = 103
cliente_no_vuelve = 35
cliente_reclama = 29
cliente_no_reclama = 4

# Interfaz
interfaz()
labels_op1(op1_min, op1_max, op1_costo, op1_unidades)
labels_op2(op2_min, op2_max, op2_costo, 0)

window.mainloop()
