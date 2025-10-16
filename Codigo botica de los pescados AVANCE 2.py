import sys
import time

productos = {
    "pomada": {"cantidad": 20, "precio": 55.00},
    "paracetamol": {"cantidad": 16, "precio": 12.50},
    "jabon": {"cantidad": 16, "precio": 35.00},
    "cerave": {"cantidad": 20, "precio": 250.00},
    "bloqueador": {"cantidad": 18, "precio": 150.00},
    "shampoo": {"cantidad": 10, "precio": 80.00},
}


stock_minimo = 10
stock_ideal = 25


def registro_de_productos(inventario, nombre_articulo, cantidad_a_agregar):
    if nombre_articulo not in inventario:
        return '\n'"Hmm, no encuentro el producto "+str(nombre_articulo)+", revisa tu ortografia e intentalo de nuevo."'\n'
    inventario[nombre_articulo]["cantidad"] += cantidad_a_agregar
    nueva_cantidad = inventario[nombre_articulo]["cantidad"]
    return '\n'"¡Gracias!, ahora la cantidad actual de '"+str(nombre_articulo)+"' es de " +str(productos[nombre_articulo]['cantidad'])+ '.\n'


def revision_de_productos(inventario, nombre_articulo):
    if nombre_articulo not in inventario:
        return '\n'"Hmm, no encuentro el producto "+str(nombre_articulo)+", revisa tu ortografia e intentalo de nuevo."'\n'

    cantidad = inventario[nombre_articulo]["cantidad"]

    if cantidad == 0:
        return '\n'+str(nombre_articulo)+ " agotado.\n"
    elif cantidad <= stock_minimo:
        return "Solo quedan " +str(productos[nombre_articulo]['cantidad'])+ " unidades de " +str(nombre_articulo)+". Pedido urgente."
    elif cantidad < stock_ideal:
        return "Quedan "+str(productos[nombre_articulo]['cantidad'])+" unidades de " +str(nombre_articulo)+". Pedido recomendable."
    elif cantidad >= stock_ideal:    
        return "Quedan "+str(productos[nombre_articulo]['cantidad'])+" de " +str(nombre_articulo)+". Pedido no necesario."

def reporte_de_ventas(inventario, nombre_articulo, cantidad_vendida):
    if nombre_articulo not in inventario:
        return '\n'"Hmm, no encuentro el producto "+str(nombre_articulo)+", revisa tu ortografia e intentalo de nuevo."'\n'
    
    cantidad_disponible = inventario[nombre_articulo]["cantidad"]
    cantidad_actual = cantidad_disponible - cantidad_vendida

    if cantidad_actual < 0:
        return '\n'"Hmm, el numero de ventas es mayor al numero de articulos en el inventario. Revisa bien los datos e intentalo de nuevo."'\n'

    inventario[nombre_articulo]["cantidad"] = cantidad_actual

    if cantidad_actual == 0:
        return str(nombre_articulo)+" se ha agotado. Pedido necesario."
    elif cantidad_actual <= stock_minimo:
        return str(nombre_articulo)+" tiene "+str(cantidad_actual)+ " unidades. Pedido recomendable."
    elif cantidad_actual <= stock_ideal:
        return str(nombre_articulo)+" tiene "+str(cantidad_actual)+ " unidades. Pedido puede ser recomendable."
    elif cantidad_actual >= stock_ideal:
        return str(nombre_articulo)+" tiene "+str(cantidad_actual)+ " unidades. Pedido no necesario."


def actualizar_precio(inventario, nombre_articulo, nuevo_precio):
    if nombre_articulo not in inventario:
        return '\n'"No encuentro el producto "+str(nombre_articulo)+", revisa tu ortografia e intentalo de nuevo."'\n'
    else:
        inventario[nombre_articulo]["precio"] = nuevo_precio
        precio_actual=productos[nombre_articulo]["precio"]
        return '\n'"El nuevo precio de "+str(nombre_articulo)+ " es de: $"+str(nuevo_precio)+"MXN"'\n'



def ciclo_inicial(inventario):
    print("Buen dia,")
    while True:
        time.sleep(0.8)
        opcion = input("Escriba 'registro' para registrar productos en el sistema," '\n'
                        "Escriba 'revision' para revisar disponibilidad de productos,"'\n'
                        "Escriba 'reporte' para hacer el reporte de ventas,"'\n'
                        "Escriba 'actualizar' para actualizar el precio de algun articulo"'\n'
                        "O escriba 'salir' si quiere concluir con el programa: ")

        if opcion == "registro":
            nombre = input("Muy bien, por favor introduzca el nombre del articulo para registrar:"'\n'
                           "Lista de artículos:"'\n'
                           "- pomada"'\n'
                           "- paracetamol"'\n'
                           "- jabon" '\n'
                           "- cerave"'\n'
                           "- bloqueador"'\n'
                           "- shampoo"'\n')
            cantidad = int(input("Gracias, ahora introduzca la cantidad de '"+str(nombre)+"' que se va a agregar al inventario: "))
            mensaje = registro_de_productos(inventario, nombre, cantidad)
            print("\n"+mensaje+"\n")

        elif opcion == "revision":
            nombre = input("Por supuesto, introduzca el nombre del articulo: "'\n'
                           "Lista de artículos:"'\n'
                           "- pomada"'\n'
                           "- paracetamol"'\n'
                           "- jabon" '\n'
                           "- cerave"'\n'
                           "- bloqueador"'\n'
                           "- shampoo"'\n')
            mensaje = revision_de_productos(inventario, nombre)
            print("\n",mensaje,"\n")

        elif opcion == "reporte":
            nombre = input("¡Claro!, por favor introduzca el nombre del articulo que se vendió: "'\n'
                           "Lista de artículos:"'\n'
                           "- pomada"'\n'
                           "- paracetamol"'\n'
                           "- jabon" '\n'
                           "- cerave"'\n'
                           "- bloqueador"'\n'
                           "- shampoo"'\n')
            cantidad = int(input("Gracias, ahora introduzca la cantidad vendida: "))
            mensaje = reporte_de_ventas(inventario, nombre, cantidad)
            print("\n",mensaje,"\n")

        elif opcion == "actualizar":
            nombre_articulo = input("Introduzca el nombre del articulo cuyo precio desea actualizar: "'\n'
                                    "Lista de artículos:"'\n'
                           "- pomada"'\n'
                           "- paracetamol"'\n'
                           "- jabon" '\n'
                           "- cerave"'\n'
                           "- bloqueador"'\n'
                           "- shampoo"'\n')
            precio_actual=productos[nombre_articulo]["precio"]
            print ('\n'"Su precio actual es de $"+str(precio_actual)+"MXN,"'\n')
            precio = float(input("Nuevo precio: "))
            mensaje = actualizar_precio(inventario, nombre_articulo, precio)
            print("\n",mensaje,"\n")

        elif opcion == "salir":
            print ('\n''Gracias!')
            time.sleep(0.6)
            print('Nos vemos pronto :)''\n')
            time.sleep(0.5)
            sys.exit()

        else:
            print('Hmm,')
            time.sleep(0.5)
            print('tal vez lo escribiste mal.')
            time.sleep(1)
            print('Revisa tu ortografia e intentalo de nuevo.''\n')


ciclo_inicial(productos)

