# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:51:01 2024

@author: Gebruiker
"""

import numpy as np
import pandas as pd
import csv 
import matplotlib.pyplot as plt

pressure = 'p'
temp = 'T'
velocity = 'U'

df_pres   = pd.read_csv(pressure)
df_temp   = pd.read_csv(temp)
df_velocity = pd.read_csv(velocity)


def calc_pT(var,graph,title,xlabel,ylabel):
    j = 0
    val = []
    for row in var.iterrows():
        if j >= 3:
            row[1].tolist()
            items = row[1][0].split()
            val.append(items)    
        j = j + 1
            
    val1 = []
    val2 = []
    val3 = []
    for i in val:
        val1.append(float(i[-3]))
        val2.append(float(i[-2]))
        val3.append(float(i[-1]))
    
    itt = np.arange(0,len(val),1)    

    plt.figure(graph)
    plt.plot(itt,val1,label = "Probe 1")
    plt.plot(itt,val2,label = "Probe 2")
    plt.plot(itt,val3,label = "Probe 3")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    

def calc_U(var,graph,title,xlabel,ylabel):
    j = 0
    val = []
    for row in var.iterrows():
        if j >= 3:
            row[1].tolist()
            items = row[1][0].split()
            val.append(items)    
        j = j + 1
            
    val1 = []
    val2 = []
    val3 = []
    for i in val:
        
        val1.append(float(i[-9][1:]))
        val2.append(float(i[-6][1:]))
        val3.append(float(i[-3][1:]))
    
    itt = np.arange(0,len(val),1)
    plt.figure(graph)
    plt.plot(itt,val1,label = "Probe 1")
    plt.plot(itt,val2,label = "Probe 2")
    plt.plot(itt,val3,label = "Probe 3")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()    
    
calc_pT(df_pres,0,"Convergence of pressure","itteration","Pressure [Pa]")
calc_pT(df_temp,1,"Convergence of temperature","itteration","Temperature [K]")
calc_U(df_velocity,3,"Convergence of velocity","itteration","Velocity [m/s]")