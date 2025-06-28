# -*- coding: utf-8 -*-
"""
Created on Sat May 31 12:31:44 2025

@author: osgos
"""

#IMPORTAR LIBRERÍA PANDAS AL ARCHIVO.
import pandas as pd

#PARTE 3 DEL EJERCICIO
#Función para convertir la fecha de lanzamiento a formato DateTime
def date_convert(df, columna='release_date'):
    df[columna] = pd.to_datetime(df[columna])
    return df

#CÁLCULO DE DOS COLUMNAS NUEVAS EN DONDE EL PRESUPUESTO Y LA UTILIDAD SEAN MAYORES A CERO.
def limpiar_presupuesto_ingresos(df):
    df['presupuesto_conocido'] = df['budget'] > 0
    df['ingresos_conocidos'] = df['revenue'] > 0
    return df

#CÁLCULO DE "RETORNO DE INVERSIÓN" O MARGEN DE UTILIDAD DE LA PELÍCULA.
def calculate_roi(df):
    df['roi'] = df.apply(lambda fila: fila['revenue']/fila['budget'] if fila['budget']>0 else 0, axis=1)
        #df['roi'] =df['revenue']/df['budget']
    return df

#SE EXTRAE ÚNICAMENTE EL AÑO PARA AGRUPAR MÁS FÁCILMENTE.
def extraer_año(df):
    df['year'] = df['release_date'].dt.year
    return df