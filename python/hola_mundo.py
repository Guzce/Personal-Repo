"""
cambio para pull desde git
"""

saludo = 'Hola mundo desde Python'
saludo_persona = input('¿Como te llamas? ->  ')
print(saludo)
print(f'Bienvenido a Programación con Python {saludo_persona}')
"""
# A continuación creamos una funcion que permita calcular la suma de dos operadores
"""


def suma_calculator():
    print('Introduce dos valores a sumar: ')
    a = int(input('Digita el primer valor: '))
    b = int(input('Digita el segundo valor: '))
    result = a + b
    return print(f'El resultado de la operación(SUMA) es {result}')


suma_calculator()
"""
num = 0
while num <= 10:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1
