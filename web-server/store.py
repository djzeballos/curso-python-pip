# Solicitudes HTTP con Requests

import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))

    categories = r.json()      # lo convierte en formato lista
    print(type(categories))
    for category in categories:
        #print(category)
        print(category['name'])
