"""
la seccion de agregados de frutas y verduras utilizan un metodo similar
// (funcion que reciba un set) y en funcion de este proceda
agregar metodo para agregar multiples unidades de un mismo producto
// busqueda en listaalmacenado para coincidencia y modificacion de unidades (incorporar concepto de unidad)
// en funcion de unidades modificar el valor de precio
para agregar por kilaje metodo ramdom que varie y valor de precio en funcion de este
"""


def presentacion():
    print('*******************************************')
    print('*****     VERDULERIA de DON JUAN    *****')
    print('*******************************************')


dic_frutas = {1: ("Manzanas", 75), 2: ("Bananas", 65),
              3: ("Naranjas", 50), 4: ("Durazno", 70),
              5: ("Frambuesa", 90)}
dic_verduras = {1: ("Zanahoria", 75), 2: ("Zapallo", 65),
                3: ("Papa", 50), 4: ("Camote", 70)}
carrito = []        # lista usada como almacenamiento
total_carrito = 0   # variable para llevar la cuenta de venta

presentacion()
var_tres = None        # variable
while var_tres != 3:
    print('***********************************************')
    print('Para comprar >> FRUTAS <<   >> OPRIME ( 1 ) <<\n' '***********************************************\n'
          'Para comprar >> VERDURAS << >> OPRIME ( 2 ) <<\n***********************************************\n'
          'Para >> QUITAR ELEMENTOS << >> OPRIME ( 3 ) <<\n***********************************************')
    var_uno = int(input('Que deseas comprar: '))
    if var_uno == 1:            # *1 mismo proceso usado en var_dos
        for opcion, fruta in dic_frutas.items():        # Muestro las distintas opciones de compra
            print(f'{opcion}\t{fruta}')
        print("Si deseas finalizar tus compras presiona Cero > 0 <")
        # Pido un valor de los observados en opcion/fruta
        opcion_elegida = int(input("¿Que deseas agregar al carrito? : "))
        if opcion_elegida == 0:
            print("Saliendo de la sección de frutas")
            print("Saliendo de la tienda")
            break
        while 0 <= opcion_elegida <= len(dic_frutas):    # Este len condice una numeracion contigua en el set
            # Itero nuevamente pero esta vez para comparar con que elemento del set coincide
            # Extraigo datos a una lista que funciona como almacen
            # Modifico la variable que lleva la cuenta / adición
            if opcion_elegida == 0:
                print("Saliendo de la sección de frutas")
                break
            for opcion, fruta in dic_frutas.items():
                if opcion_elegida == opcion:
                    carrito.append((fruta[0], fruta[1]))
                    total_carrito = total_carrito + fruta[1]
                    break
            print(carrito)
            print(f"Total: $ {total_carrito}")
            opcion_elegida = int(input("¿Que deseas agregar al carrito? : "))
        else:
            print("No se hallo tu producto\nIntenta nuevamente con una opción valida")
    elif var_uno == 2:      # Repetimos el mismo procedimiento *1 pero esta vez con una lista diferente
        for opcion, verdura in dic_verduras.items():
            print(f'{opcion}\t{verdura}')
        opcion_elegida = int(input("¿Que deseas agregar al carrito? : "))
        if opcion_elegida == 0:
            print("Saliendo de la sección de frutas")
            print("Saliendo de la tienda")
            break
        for opcion, verdura in dic_verduras.items():
            if opcion_elegida == opcion:
                carrito.append((verdura[0], verdura[1]))
                total_carrito = total_carrito + verdura[1]
                break
        else:
            print("No se hallo tu producto\nIntenta nuevamente con una opción valida")
        print(carrito)
        print(f"Total: $ {total_carrito}")

        for opcion, verdura in dic_verduras.items():        # Muestro las distintas opciones de compra
            print(f'{opcion}\t{verdura}')
        print("Si deseas finalizar tus compras presiona Cero > 0 <")
        # Pido un valor de los observados en opcion/verdura
        opcion_elegida = int(input("¿Que deseas agregar al carrito? : "))
        if opcion_elegida == 0:
            print("Saliendo de la sección de verduras")
            print("Saliendo de la tienda")
            break
        while 0 <= opcion_elegida <= len(dic_verduras):    # Este len condice una numeracion contigua en el set
            # Itero nuevamente pero esta vez para comparar con que elemento del set coincide
            # Extraigo datos a una lista que funciona como almacen
            # Modifico la variable que lleva la cuenta / adición
            if opcion_elegida == 0:
                print("Saliendo de la sección de Verduras")
                break
            for opcion, verdura in dic_verduras.items():
                if opcion_elegida == opcion:
                    carrito.append((verdura[0], verdura[1]))
                    total_carrito = total_carrito + verdura[1]
                    break
            print(carrito)
            print(f"Total: $ {total_carrito}")
            opcion_elegida = int(input("¿Que deseas agregar al carrito? : "))
        else:
            print("No se hallo tu producto\nIntenta nuevamente con una opción valida")

    elif var_uno == 3:
        if len(carrito) != 0:
            i = 0
            print("Sacando Productos del carrito")
            # Iteramos productos en nuestra lista almacen
            # y le asignamos un valor de referencia para el usuario
            for producto in carrito:
                i = i + 1
                print(f"{i} {producto}")
            # Solicitamos un valor de referencia mostrado para realizar operación de limpieza
            opcion_quitar = int(input("¿Que deseas quitar del carrito?: "))
            # Mostramos y preparamos el elemento almacenado que sera removido
            opcion_quitar = opcion_quitar - 1
            elim_carrito = carrito[opcion_quitar]
            print(f"Ha quitado {elim_carrito}")
            # Eliminamos el producto de la lista almacen y modificamos importe de la variable cuenta
            total_carrito = total_carrito - elim_carrito[1]
            carrito.remove(carrito[opcion_quitar])

            print(carrito)
            print(f"Total: $ {total_carrito}")
        else:
            print("CARRITO VACIO\nAhun no has agregado nada al carrito")
    else:
        print('La opción que ha introducido no es valida')
    # Mostramos posibles valores para proceder con acción asociada
    # Este valor definira la repetición o finalización de nuestro bucle recursivo
    # El bloque recursivo evita finalizar el programa en caso de no coincidir con la sentencia de quiebre
    print('***********************************************')
    print('Productos en carrito: ')
    print('1 - Realizar compras')
    print('    Quitar del carrito')
    print('3 - Salir de la tienda')

    var_tres = int(input('Que deseas hacer: '))
# Jugaremos un poco con la presentación en consola
presentacion()
print('Ha comprado:')
for i in carrito:
    print(f"{i[0]}".ljust(15)+f"{i[1]}".rjust(15))
print(f'Total:'.ljust(15)+f'$ {total_carrito}'.rjust(15))

print('')
print(' Gracias por la visita '.center(30, "-"))
print('Esperamos verte nuevamente'.center(30))
print('***************************************')
