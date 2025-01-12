"""
¿Que es PIP?
Clase 7/20  Curso de Python: PIP y Entornos virtuales
"""

import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('../charts/pie.png')
    plt.close()
