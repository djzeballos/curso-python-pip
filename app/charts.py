
"""
Graficas en Python PIP
Clase 8/20  Curso de Python: PIP y Entornos virtuales
"""

# https://platzi.com/blog/matplotlib/
# https://platzi.com/cursos/matplotlib-seaborn/
# https://matplotlib.org/

import matplotlib.pyplot  as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    #plt.show()
    #plt.savefig('bar.png')
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    #plt.show()
    plt.savefig('../app/pie.png')
    plt.close()

# para ejecutar como script o desde la consola
if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
