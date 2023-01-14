'''
KPI'S DEBEN SER 8
ELIMINAR LOS DATOS QUE NO TIENEN HORARIO O NA EN OTRA COLUMNA

#* 1 LISTA DE NOMBRES DE RESTAURANTES
#* 2 NUMERO DE LOCALES POR EMPRESA
#* 3 TIPO DE RESTAURANTE
#* 4 ESTADO MAS REPETIDO
#* 5 CIUDAD MAS REPEITDA E ID DE CADA CIUDAD
#? 6 SABER CUANTOS SUPERAN LOS 100 LOCALES
#? 7 SABER CUANTOS TIENEN 1 LOCAL
#* 8 SUBWAYS EN NY
#* 9 CUANTOS LOCALES HAN CERRADO (SIN HORARIO)
#* 10 Frecuencia de tipos de Restuarante
#? 11 Restaurantes por coordenadas
'''

import pandas as pd
import matplotlib.pyplot as plt


dc = pd.read_csv("chainness_point_2021_part1.csv", encoding = "latin-1")
df = dc.dropna()

df.to_csv("df_Limpio.csv", index=False)

print(df.describe())

#*1 - Lista de nombres de Restaurante
Restaurante = df["RestaurantName"].drop_duplicates()
RestauranteLista = Restaurante.tolist()
Restaurante.to_csv("Nombres_Restaurante.csv", index=False)
print(RestauranteLista)

#*2 - Numero de locales por empresas
occur2 = df.groupby("RestaurantName")["RestaurantName"].count()
occurP = occur2.sort_values(ascending= False).head(10)
occurP.plot(kind="bar", x="Empresa", y="Numero de locales")
plt.show()
occur2.to_csv("LocalxEmpresa.csv")

print(occur2)

#*3 - Tipos de Restaurante
Cuisine = df["Cuisine"].drop_duplicates()
Cuisinelist = Cuisine.tolist()
Cuisine.to_csv("Type_Cuisine.csv", index=False)
print(Cuisinelist)

#*4 - Estados mas repetidos
occurEN = df.groupby("State")["State"].count()
occurE = occurEN.sort_values(ascending= False).head(10)
occurE.plot(kind="bar", x="Estado", y="Repeticiones")
plt.show()
occurEN.to_csv("Estados.csv")

print(occurEN)

#*5 - Condados mas repetidas
df["County_State"] = df["CNTY_NAME"].str.cat(df["State"], sep = ", ")
occurCN = df.groupby("County_State")["CNTY_GEOID"].count()
occurC = occurCN.sort_values(ascending= False).head(10)
occurC.plot(kind="bar", x="Condados", y="Repeticiones")
plt.show()
occurCN.to_csv("Condados.csv")
print(occurCN)

#?6 - 100 locales
a = df.RestaurantName.value_counts().loc[lambda x: x>=100]
a.to_csv("Cien.csv")
print(a)

#?7 - 1 local
b = df.RestaurantName.value_counts().loc[lambda x: x==1]
b.to_csv("Indies.csv")
print(b)

#*8 - New York
subways = df[(df['RestaurantName'] == 'Subway') & (df['State'] == 'NY')]
subways.to_csv("NYSubways.csv")
print(f"\nEn Nueva York hay: {subways['RestaurantName'].count()} subways")

#*9 - Locales sin horario
clausurados = dc['OpenHours'].isnull().sum()
print(f'Se han registrados {clausurados} sucursales sin horario')

#*10 - Frecuencia de Restaurantes
df["Cuisine"]=df["Cuisine"].str.lstrip()
occurR = df.groupby("Cuisine")["RestaurantName"].count()
occurPR = occurR.sort_values(ascending = False).head(10)
occurR.to_csv("Cuisine_Restaurant.csv")
print(occurPR)
occurPR.plot(kind="bar", x="Cuisine", y="RestaurantName")
plt.show()

#*11 - Coordenadas
west = df[df['Lon'] <= -111]
east = df[df['Lon'] >= -84]
center = df[(df['Lon'] > -111) & (df['Lon'] < -84)]

print(f"Del lado oeste hay: {west['RestaurantName'].count()} locales")
print(f"Del lado este hay: {east['RestaurantName'].count()} locales")
print(f"En el centro hay: {center['RestaurantName'].count()} locales")

countRestWest = west.groupby('RestaurantName')['RestaurantName'].count()
countRestEast = east.groupby('RestaurantName')['RestaurantName'].count()
countRestCenter = center.groupby('RestaurantName')['RestaurantName'].count()

ordCountRestWest = countRestWest.sort_values(ascending= False).head(5)
ordCountRestEast = countRestEast.sort_values(ascending= False).head(5)
ordCountRestCenter = countRestCenter.sort_values(ascending= False).head(5)

countRestWest.to_csv("West_Restaurant.csv")
countRestEast.to_csv("East_Restaurant.csv")
countRestCenter.to_csv("Center_Restaurant.csv")

print(ordCountRestWest)
print(ordCountRestEast)
print(ordCountRestCenter)

ordCountRestWest.plot(kind="bar", x="Local", y="Cantidad", title="Restaurants West")
plt.show()
ordCountRestEast.plot(kind="bar", x="Local", y="Cantidad", title="Restaurants East")
plt.show()
ordCountRestCenter.plot(kind="bar", x="Local", y="Cantidad", title="Restaurants Center")
plt.show()