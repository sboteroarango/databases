import pandas as pd
import matplotlib.pyplot as plt
#se cargó la base de datos de precios del oro de https://www.kaggle.com/odins0n/monthly-gold-prices
df = pd.read_csv(ruta)
df = pd.DataFrame(df)
print(df.columns)
#convertir objeto date a datetime
df['Date'] = pd.to_datetime(df['Date'])
#agregar la columna año para mejor visualización
df['Año'] =df['Date'].dt.year
print(df.dtypes)
#plot
plt.plot(df['Año'],df['United States(USD)'],label = 'precio del oro en USD')
plt.plot(df['Año'],df['Europe(EUR)'],label = 'precio del oro en EUR')

plt.legend()
plt.show()
