# -*- coding: utf-8 -*-


calificaciones = {}

calificaciones['algoritmos'] = 9
calificaciones['matematicas'] = 10
calificaciones['web'] = 8
calificaciones['bases_de_datos'] = 10

print(calificaciones)

print("Recorriendo 'for' las llaves 'key'")
print('')

for key in calificaciones:
    print(key)

print('')
print("Recorriendo 'for' los valores 'value'")
print('')

for value in calificaciones.values():
    print(value)

print('')
print("Imprimiendo las llaves y los valores")
print('')

for key, value in calificaciones.items():
    print(key, value)


print('')
print('Sumando las calificaciones')
print('')

suma_calificaciones = 0

for calificacion in calificaciones.values():
    suma_calificaciones += calificacion

print("Suma calificaciones es igual a {}".format(suma_calificaciones))

promedio = suma_calificaciones / len(calificaciones.values())

print('El promedio fue {}.'.format(promedio))
