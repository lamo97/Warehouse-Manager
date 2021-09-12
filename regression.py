from random import randint
import pandas as pd
import numpy as np
from sklearn import linear_model

def seleziona_mezzo():
    van={}
    van_list = ['Ford Transit','Fiat Ducato','Citroen Jumper', 'Iveco Daily']
    id = [0,1,2,3]

    choice = randint(0,3)
   
    van['modello'] = van_list[choice]
    van['id'] = id[choice]

    return van

def simula_orario():
    return (randint(5,17))

def simula_cond_atmosferiche():
    return (randint(0,1))

def predizione(id, carico, wind, orario):
    df = pd.read_csv('dataset/storico_consumi.csv')
    reg = linear_model.LinearRegression()
    reg.fit(df[['id','carico','vento','orario',]], df.L100KM)
    pred = reg.predict([[id,carico,wind,orario]])

    predizione = round(pred[0], 1)
    return predizione

def calcolo_costo(km,pred):
    kml = 100/pred
    return km/kml

def costo_consegna(distanza, media_carburante):
    kml = 100/media_carburante
    val = (distanza/1000)/kml
    return val*1.491
    
