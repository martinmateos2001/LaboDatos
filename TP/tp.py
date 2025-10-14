# %%
import numpy as np
import pandas as pd
import duckdb as dd

ruta = 'C:\\Users\\Mario\\OneDrive\\Documentos\\Marton\\LaboDatos\\TP\\'
# %%== limpieza del padron de establecimientos educativos
columnas_ee = 'A:C,G,L,N,V:Y'
df_ee_padron = pd.read_excel(ruta + '2022_padron_oficial_establecimientos_educativos.xlsx', sheet_name='padron2022', skiprows=6, usecols=columnas_ee)

query_solo_comunes = """
                        SELECT *
                        FROM df_ee_padron
                        WHERE "Común" = '1'
                    """

df_ee_padron = dd.sql(query_solo_comunes).df()

#verifico que borra todos los EE que no son comunes
#selecciono la columna Común y veo que todos las filas sean unos
df_comunes = df_ee_padron.loc[:, ['Común']]
print(df_comunes.head())
res:bool = False
#for index_row in df_comunes:
#    if
# %% limpieza de datos de establecimientos por departamentos, actividad y genero
df_ep_datos = pd.read_csv(ruta + 'Datos_por_departamento_actividad_y_sexo.csv', usecols=[0,1,2,5,8,9,10,11])

#obtengo solo los datos del año 2022
query_datos_2022 = """
                    SELECT *
                    FROM df_ep_datos
                    WHERE anio = 2022
                """
df_ep_datos = dd.sql(query_datos_2022).df()
print(df_ep_datos.head())


# %% limpieza del padron poblacional
df_padron_poblacional = pd.read_excel(ruta + 'padron_poblacion.xlsX', sheet_name=None, skiprows=13, usecols='A:C')

# %%
