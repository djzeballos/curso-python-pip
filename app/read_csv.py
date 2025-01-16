# Leer un csv
"""
Graficas en Python PIP
Clase 8/20  Curso de Python: PIP y Entornos virtuales
"""

# https://www.kaggle.com/
# https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset
# https://www.w3schools.com/python/python_file_open.asp

import csv

def read_csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)   # obtengo los nombres del encabezado
        #print(header)
        data = []
        for row in reader:
            #print('-' * 40)
            #print(row)
            iterable = zip(header, row)  # obtengo una lista o array de tuplas (clave y valor)
            #print(list(iterable))
            country_dict = {key: value for key, value in iterable}  # obtiene un diccionario
            data.append(country_dict)
            #print(country_dict)
        return data

if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    #print(data)
    print(data[0])
    #print(data[1])
