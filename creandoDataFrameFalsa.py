
import pandas as pd
from faker import Faker

fake = Faker()

nombres = []
direcciones = []
empresas = []
trabajo = []

for x in range(101):
    nombres.append(fake.name())
    direcciones.append(fake.address())
    empresas.append(fake.company())
    trabajo.append(fake.job())

diccionario ={"NOMBRE" : nombres,
"DIRECCION" : direcciones,
"EMPRESA" : empresas,
"EMPLEO" : trabajo}

df = pd.DataFrame(diccionario)
