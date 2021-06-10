import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

leer=pd.read_csv(r"C:\Users\FAMILIAR\Downloads\Amenazas_Polic_a_Nacional_de_Colombia.csv")
basededatos=pd.DataFrame(leer)

print((basededatos["MUNICIPIO"].value_counts()).shape)#encontrar los diferentes municipios

listadecapitales=[]
for x in basededatos["MUNICIPIO"]: #encontrar los que tienen 3 y 27 letras, y los que tienen (CT)
    if len(x)==27:
       print(x)
    if len(x)==3:
        print(x)
    if "(CT)" in x:
     listadecapitales.append(x)

listadecapitales = list( dict.fromkeys(listadecapitales) )#ver las capitales diferentes y cuantas son
print(listadecapitales)
print(len(listadecapitales))

for i in basededatos["FECHA HECHO"]:#encontrar hasta que año están las fechas
  print(i[-2],i[-1])
