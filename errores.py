# -*- coding: utf-8 -*-

countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru': 31
}

while True:
    country = input('Escribe el nombre de un país: ').lower()

    try:
        print('La población de {} es: {} millones'.format(country,
                                                          countries[country]))
    except KeyError:  # Es el tipo de error como NameError
        print('No tenemos el dato de la población de {}'.format(country))
