# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('A continuacion, le solicitamos que ingrese dos numeros')
num_1 = float(input('Ingrese el primer numero: '))
num_2 = float(input('Ingrese el segundo numero: '))

resta = num_1 - num_2

if resta > 0:
    print('El resultado de la diferencia es positivo (', resta, ').')
elif resta < 0:
    print('El resultado de la diferencia es negativo (', resta, ').')
else:
    print('El resultado de la diferencia es cero.')
