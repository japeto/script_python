######################################
# Este script carga un csv de datos
# climaticos 
# author Jefferson Peña
######################################

# carga de librerias y modulos
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import statistics as st

data=pd.read_csv("/Users/Usuario/Desktop/archivos/Datos_Climaticos.csv")
data.columns
data.head()
data.tail()

humedad = data["Humedad (%)"]
viento = data["Vel Viento  (m/s)"]

# quitar los ND, convertirlos a 0
# humedad.replace("ND", 0, inplace=True)
# viento.replace("ND", 0, inplace=True)
humedad.replace("ND", np.NA, inplace=True)
viento.replace("ND", np.NA, inplace=True)

humedad = humedad.astype('float64')
viento = viento.astype(float)

## grafique el histograma, 
plt.hist(humedad)
plt.title("Histograma (Humedad %)")
#plt.legend()
plt.hist(viento)
plt.title("Histograma (Viento %)")
plt.show

humedad_noNA = humedad.dropna()
viento_noNA = viento.dropna()
humedad_noNA =  humedad_noNA.drop([2], axis=0)

humedad_noNA
## media
print("Media desde st %d " % st.mean(humedad_noNA))
print(f"Media desde np {np.mean(humedad_noNA)}")
## moda
## mediana
# mediana agrupada
print(f"Media desde st {st.median_grouped(humedad_noNA)}")
# rango
def get_rango(vector=[]):
	return max(vector) - min(vector)
print(f"rango {get_rango(humedad_noNA)}")
# varianza
print("varianza = ", st.variance(humedad_noNA))
# desviacion estandar   -- np.std
# covarianza   -- np.cov
# corelacion  np.corrcoef( (humedad_noNA, viento_noNA) )





data.plot(figsize=(20,15))
data.dtypes

data.columns
data["Fecha hora"] = pd.to_datetime(data["Fecha hora"])
data["Humedad (%)"].astype(float)
data["Vel Viento  (m/s)"].astype(float)
data.dtypes
















