
"""
Proyecto final python
Registro de inventario "Botica de los Pescados"
El programa tiene articulos registrados en el sistema, el usuario puede
ir actualizando su cantidad y precio con forme a las ventas y a la 
compra de productos
"""

"""
Bibliotecas
"""

import sys
import time

"""
La biblioteca sys me ayuda a que cuando escriba el mensaje de salir, el
programa se cierra y se termina con la operación. La biblioteca time 
ayuda a hacer ver el programa  un poco mas amigable, humano e 
interactivo con el usuario, mostrando algunos mensajes linea por linea
"""

"""
Diccionario 
"""

productos = {
    "pomada": {"cantidad": 0, "precio": 55.00},
    "paracetamol": {"cantidad": 0, "precio": 12.50},
    "jabon": {"cantidad": 0, "precio": 35.00},
    "cerave": {"cantidad": 0, "precio": 250.00},
    "bloqueador": {"cantidad": 0, "precio": 150.00},
    "shampoo": {"cantidad": 0, "precio": 80.00},
}

"""
Constantes
"""

stock_minimo = 10
stock_ideal = 25

"""
Muestran la cantidad minima e ideal que debe haber de cada articulo, 
para despues ser usadas en las funciones revision y reporte
"""

"""
================ Funciones ================================
"""

def registro_de_productos(inventario, nombre_articulo, cantidad_a_agregar):
    
    """    
    (Uso de operadores, uso de funciones, uso de variables, uso de
    condicionales, uso de diccionario)
    Recibe inventario, lista anidada, nombre_articulo, string, 
    cantidad_a_agregar valor numerico. 
    La funcion resgistro recibe el nombre (string) de un articulo que 
    vaya a ser registrado, si no esta en el inventario, devuelve un  
    string que describe que no se encontro y regresa al menu principal.
    Si el articulosi existe dentro de la lista, devuelve un mensaje 
    pidiendo la cantidad que se desea sumar, y se suma a la cantidad  
    inicial del producto, convirtiendo esa cantidad en la cantidad 
    actual de ese articulo. Al final devuelve un mensaje especificando
    la cantidad actual del producto.
    """ 
    
    if nombre_articulo not in inventario:
        return (f'\nHmm, no encuentro el producto {nombre_articulo}, '
                f'revisa tu ortografia e intentalo de nuevo.\n')
    inventario[nombre_articulo]["cantidad"] += cantidad_a_agregar
    nueva_cantidad = inventario[nombre_articulo]["cantidad"]
   
    return (f'\n¡Gracias!, ahora la cantidad actual de '
            f'"{nombre_articulo}" es de '
            f'{productos[nombre_articulo]["cantidad"]}.\n')


def revision_de_productos(inventario, nombre_articulo):
    
    """
    (Uso de operadores, uso de funciones, uso de variables, uso de
    condicionales, uso de diccionarios)
    Recibe inventario, lista anidada, nombre_articulo, string
    La funcion revision recibe el nombre de un articulo, si no esta en el
    diccionario, devuelve un mensaje y regresa al menu (ciclo_inicial). si el
    articulo existe, devuelve la cantidad actual del articulo junto con un
    mensaje que segun las variables 'stock minimo' y 'stock ideal' muestra si
    es recomendado hacer restock de dicho producto.
    """
    
    if nombre_articulo not in inventario:
        return (f'\nHmm, no encuentro el producto {nombre_articulo}, '
                f'revisa tu ortografia e intentalo de nuevo.\n')

    cantidad = inventario[nombre_articulo]["cantidad"]
    
    if cantidad == 0:
        return f'\n{nombre_articulo} agotado.\n'
    
    elif cantidad <= stock_minimo:
        return (f'Solo quedan {productos[nombre_articulo]["cantidad"]} '
                f'unidades de {nombre_articulo}. Pedido urgente.')
    
    elif cantidad < stock_ideal:
        return (f'Quedan {productos[nombre_articulo]["cantidad"]} '
                f'unidades de {nombre_articulo}. Pedido recomendable.')
    
    elif cantidad >= stock_ideal:    
        return (f'Quedan {productos[nombre_articulo]["cantidad"]} '
                f'unidades de {nombre_articulo}. Pedido no necesario.')


def reporte_de_ventas(inventario, nombre_articulo, cantidad_vendida):
    
    """
    (Uso de operadores, uso de funciones, uso de variables, uso de 
    condicionales, uso de diccionarios)
    Recibe inventario, lista anidada, nombre_articulo, string,
    cantidad_vendida, valor numerico
    La funcion reporte de ventas recibe el nombre de un articulo para 
    registrar la cantidad vendida. Si no encuentra el producto descrito
    despliega un mensaje que dice que el articulo no existe y te manda
    al menu. Si existe, pide la cantidad que fue vendida y en el
    diccionario actualiza su cantidad actual, y a esta, le resta el 
    numero dado que representa las ventas y esa nueva cantidad la  
    convierte en la cantidad actual.
    """

    if nombre_articulo not in inventario:
        return (f'\nHmm, no encuentro el producto {nombre_articulo}, '
                f'revisa tu ortografia e intentalo de nuevo.\n')
    
    cantidad_disponible = inventario[nombre_articulo]["cantidad"]
    cantidad_actual = cantidad_disponible - cantidad_vendida

    if cantidad_actual < 0:
        return ('\nEl numero de ventas es mayor al numero de articulos en '
                'el inventario. Intentalo de nuevo.\n')

    inventario[nombre_articulo]["cantidad"] = cantidad_actual

    if cantidad_actual == 0:
        return f'{nombre_articulo} se ha agotado. Pedido necesario.'
    
    elif cantidad_actual <= stock_minimo:
        return (f'{nombre_articulo} tiene {cantidad_actual} unidades. '
                f'Pedido recomendable.')
    
    elif cantidad_actual <= stock_ideal:
        return (f'{nombre_articulo} tiene {cantidad_actual} unidades. '
                f'Pedido puede ser recomendable.')
    
    elif cantidad_actual >= stock_ideal:
        return (f'{nombre_articulo} tiene {cantidad_actual} unidades. '
                f'Pedido no necesario.')


def actualizar_precio(inventario, nombre_articulo, nuevo_precio):
    
    """
    (Uso de operadores, uso de funciones, uso de variables, uso de
    condicionales, uso de diccionarios)
    Recibe inventario, lista anidada, nombre_articulo, string, 
    nuevo_precio, valor numerico
    La funcion actualizar recibe el nombre del articulo cuyo precio
    quiere ser actualizado. Si el articulo no existe dentro de la lista
    de articulos devuelve un mensaje y te regresa al menu 
    (ciclo_inicial). Al contrario, si el articulo existe, te muestra
    el precio del articulo y pide el nuevo precio que se quiere para el
    articulo. Cuando lo recibe, actualiza el precio en la lista del 
    inventario y lo convierte en el precio actual.
    """

    if nombre_articulo not in inventario:
        return (f'\nNo encuentro el producto {nombre_articulo}, revisa tu '
                f'ortografia e intentalo de nuevo.\n')
    
    else:
        inventario[nombre_articulo]["precio"] = nuevo_precio
        precio_actual = productos[nombre_articulo]["precio"]
        return (f'\nEl nuevo precio de {nombre_articulo} es de: '
                f'${nuevo_precio}MXN\n')

"""
=============Ciclo inicial===============================
"""

def ciclo_inicial(inventario):
    """
    (uso de operadores, uso de inputs, uso de variables, uso de ciclos,
    uso de condicionales, uso de librerias, uso de inputs, uso de 
    funciones, uso de librerias)
    Recibe: inventario, lista anidada
    Devuelve varias opciones. Mientras sea verdadero, muestra el menu 
    de las opciones. Si se escribe registro, manda a llamar a la 
    funcion registro, y cuando termina la funcion, regresa a este mismo
    menu. Asi con todas las funciones, se repite y re repite el bucle 
    hasta que se escribe 'salir', la cual hace uso de la libreria sys
    y termina con el programa imprimiendo un mensaje final. Igualmente,
    si se escribe mal algunaa opcion por error de ortografia, imprime
    un mensaje y vuelve a correr el loop.
    """
    
    print("Buen dia,")
    while True:
        time.sleep(0.8)
        opcion = input(
            "Escriba 'registro' para registrar productos en el sistema,"'\n'
            "Escriba 'revision' para revisar disponibilidad de productos,"'\n'
            "Escriba 'reporte' para hacer el reporte de ventas,"'\n'
            "Escriba 'actualizar' para cambiar el precio de un articulo"'\n'
            "O escriba 'salir' si quiere concluir con el programa: ")

        if opcion == "registro":
            """
            Manda a llamar a la funcion registro
            """
            nombre = input(
                "Muy bien, por favor introduzca el nombre del articulo para"
                " registrar:"'\n'
                          "Lista de artículos:"'\n'
                           "- pomada"'\n'
                           "- paracetamol"'\n'
                           "- jabon" '\n'
                           "- cerave"'\n'
                           "- bloqueador"'\n'
                           "- shampoo"'\n')
            cantidad = int(input(
                f"Gracias, ahora introduzca la cantidad de '{nombre}' que se "
                f"va a agregar al inventario: "))
            mensaje = registro_de_productos(inventario, nombre, cantidad)
            print(f"\n{mensaje}\n")

        elif opcion == "revision":
            """
            Manda a llamar a la funcion revision
            """
            
            nombre = input("Por supuesto, introduzca el nombre del articulo:"
            " "'\n'
                           "Lista de artículos:"'\n'
                           "- pomada"'\n'
                           "- paracetamol"'\n'
                           "- jabon" '\n'
                           "- cerave"'\n'
                           "- bloqueador"'\n'
                           "- shampoo"'\n')
            mensaje = revision_de_productos(inventario, nombre)
            print(f"\n{mensaje}\n")

        elif opcion == "reporte":
            """
            Manda a llamar a la funcion reporte
            """
            
            nombre = input("¡Claro!, por favor introduzca el nombre del"
                           " articulo que se vendió: "'\n'
                           "Lista de artículos:"'\n'
                           "- pomada"'\n'
                           "- paracetamol"'\n'
                           "- jabon" '\n'
                           "- cerave"'\n'
                           "- bloqueador"'\n'
                           "- shampoo"'\n')
            cantidad = int(input(
                "Gracias, ahora introduzca la cantidad vendida: "))
            
            mensaje = reporte_de_ventas(inventario, nombre, cantidad)
        
            print(f"\n{mensaje}\n")
            
        elif opcion == "actualizar":
            """
            Manda a llamar a la funcion actualizar
            """
            
            nombre_articulo = input("Introduzca el nombre del articulo cuyo"
                           " precio desea actualizar: "'\n'
                           "Lista de artículos:"'\n'
                           "- pomada"'\n'
                           "- paracetamol"'\n'
                           "- jabon" '\n'
                           "- cerave"'\n'
                           "- bloqueador"'\n'
                           "- shampoo"'\n')
            precio_actual = productos[nombre_articulo]["precio"]
            print (f'\nSu precio actual es de ${precio_actual}MXN,\n')
            precio = float(input("Nuevo precio: "))
            mensaje = actualizar_precio(inventario, nombre_articulo, precio)
            print(f"\n{mensaje}\n")

        elif opcion == "salir":
            """
            Termina con el programa
            """
            print ('\n''Gracias!')
            time.sleep(0.6)
            print('Nos vemos pronto :)''\n')
            time.sleep(0.5)
            sys.exit()

        else:
            """
            Repite el bucle en caso de error en el mensaje
            """
            
            print('Hmm,')
            time.sleep(0.5)
            print('tal vez lo escribiste mal.')
            time.sleep(1)
            print('Revisa tu ortografia e intentalo de nuevo.''\n')


ciclo_inicial(productos)
