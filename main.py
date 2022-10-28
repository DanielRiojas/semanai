from statistics import covariance
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
    
# Importar datos de agua entubada desde archivo
agua_entubada = pd.read_csv('AguaEntubada.csv') 
agua_entubada_coah = pd.read_csv('AguaEntubadaCoahuila.csv') 
# Conservar solo columnas relevantes
agua_entubada = agua_entubada[['Municipio', 'Agua Entubada', 'Analfabetismo']]
#agua_entubada = agua_entubada[['Municipio', 'Agua Entubada', 'Analfabetismo', 'Sin Primaria', 'Sin Secundaria']]
agua_entubada_coah = agua_entubada_coah[['Municipio', 'Agua Entubada', 'Analfabetismo']]

agua_entubada_mun = agua_entubada[1:]
agua_entubada_mun_coah = agua_entubada_coah[1:]


graph = sns.lmplot(x ="Agua Entubada", y ="Analfabetismo", data = agua_entubada_mun, order = 1, ci = None)
graph.set(xlabel="Viviendas con agua entubada \n en un dado municipio de N.L (%)", ylabel="Población analfabeta de 15 años y más \n en el mismo municipio (%)")

#graph = sns.lmplot(x ="Agua Entubada", y ="Analfabetismo", data = agua_entubada_mun_coah, order = 1, ci = None)
#graph.set(xlabel="Viviendas con agua entubada \n en un dado municipio de Coahuila (%)", ylabel="Población analfabeta de 15 años y más \n en el mismo municipio (%)")

#graph = sns.lmplot(x ="Agua Entubada", y ="Sin Primaria", data = agua_entubada_mun, order = 1, ci = None)
#graph.set(xlabel="Viviendas con agua entubada \n en un dado municipio de N.L (%)", ylabel="Población sin primaria en el mismo municipio (%)")

#graph = sns.lmplot(x ="Agua Entubada", y ="Sin Secundaria", data = agua_entubada_mun, order = 1, ci = None)
#graph.set(xlabel="Viviendas con agua entubada \n en un dado municipio de N.L (%)", ylabel="Población sin secundaria en el mismo municipio (%)")

#plt.show()


x = np.array(agua_entubada_mun["Agua Entubada"]).reshape(-1,1)
y = np.array(agua_entubada_mun["Analfabetismo"]).reshape(-1,1)
x_coah = np.array(agua_entubada_mun_coah["Agua Entubada"]).reshape(-1,1)
y_coah = np.array(agua_entubada_mun_coah["Analfabetismo"]).reshape(-1,1)

mean_x = np.mean(x)
mean_y = np.mean(y)
desv_x = np.std(x)
desv_y = np.std(y)

regr = LinearRegression()
regr.fit(x,y)
intercept = regr.intercept_
slope = regr.coef_
