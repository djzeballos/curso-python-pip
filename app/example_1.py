# Conoce otros proyectos de este curso

import utils
import read_csv
import charts

from matplotlib import pyplot as plt

def get_population_ratio(datos):
    continent = input('What continent are you interested in? Write your answer: ')
    datos = list(filter(lambda item: item['Continent'] == continent, datos))
    paises = [item['Country/Territory'] for item in datos]
    ratios = [float(item['World Population Percentage']) for item in datos]
    return paises, ratios

'''
En esta función se usa list comprehensions. Se está recorriendo a DATOS, que es
una lista compuesta de diccionarios, y cada uno de estos se denomina ITEM. Luego,
cada uno de estos ITEM se le solicita el valor asociado a la clave COUNTRY/TERRITORY o WORLD POPULATION PERCENTAGE. 
Otra solución:
def get_world_percentages(data):
    percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in data}

    names = percentages_dict.keys()
    per = percentages_dict.values()

    return names, per'''

def plot_pie(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.show()


if __name__ == '__main__':
    data = read_csv.read_csv('./app/data.csv')
    paises, ratios = get_population_ratio(data)
    #print(paises)
    #print(ratios)
    plot_pie(paises, ratios)
