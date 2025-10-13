import numpy as np
import pandas as pd
import duckdb as dd
#%% limpieza de codigo
columnas_ee = 'A:C,G,L,N,V:Y'

df_ee_padron = pd.read_excel('TP\\2022_padron_oficial_establecimientos_educativos.xlsx', sheet_name='padron2022', skiprows=6, usecols=columnas_ee)
df_ep_datos = pd.read_csv('TP\Datos_por_departamento_actividad_y_sexo.csv')

print(df_ee_padron.head())
#%%
