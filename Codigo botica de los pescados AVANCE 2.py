


input("Buen dia, escriba 'registro' para registrar productos en el sistema, escriba 'cantidad' para revisar disponibilidad de productos, escriba 'reporte' para hacer el reporte de ventas: ")

    #aqui irian funciones de if, else y etc para que el programa despliegue distintas opciones segun quiera el usuario
    #como aun no hemos visto este tema, para este avance 2 solo pondre los operadores.
#por si tiene errores de ortografia:
input("Hmm, tal vez lo escribiste mal, revisa tu ortografia e intentalo de nuevo.")
    #si viene a registrar un producto
p = input("Muy bien, por favor introduzca el nombre del articulo: ")

x = int(input("Gracias, ahora introduzca la cantidad de '"  + p + "' que se va a agregar al inventario: "))
y = 0
z = x + y
print ("¡Gracias!, ahora la cantidad actual de '",p,"' es de ", z, ".")
######termina esta seccion del programa, pero si va a hacer otras opciones en lugar de esta de arriba se despliega cualquiera de las otras 2####

#si viene a consultar la cantidad de otro producto

q = input("Claro, introduzca el nombre del articulo: ")
#aqui van funciones de if, else, por ejemplo, si busca paracetamol que despliegue cuanta cantidad hay
    #si el producto = 0:
print(q, "agotado.")

    #si producto >0 y <= 10:
print("Solo quedan", z,"unidades, hacer pedido urgente.")

    #si producto >=11 y <=25:
print("Quedan", z,"unidades, hacer pedido es recomendado.")

    #si producto >25:
print("Quedan", z,"unidades. Hacer pedido no es necesario")
######termina esta seccion del programa, pero si va a hacer otras opciones en lugar de esta de arriba se despliega cualquiera de las otras 2####


#si viene a reportar las ventas (aqui es donde se aplican los operadores para mi avance 2):
p = input("¡Claro!, por favor introduzca el nombre del articulo: ")
xx = int(input("Gracias, ahora introduzca la cantidad de '"  + p + "' que se vendio esta semana: "))
zz = z - xx

#si por alguna razon pone mal el numero de ventas y da un numero negativo:
print ("Hmm, el numero de ventas es mayor al numero de articulos en el inventario. Revisa bien los datos e intentalo de nuevo.")
#si zz == 0:
print ("¡El producto '",p,"' esta agotado! Solo hay ", zz, ",es necesario hacer pedido.")
#si zz > 0 and z <= 10:
print ("¡Gracias!, ahora la cantidad actual de '",p,"' es de ", zz, ", se requiere hacer pedido.")
#si zz >= 11 and z <= 20:
print ("¡Gracias!, ahora la cantidad actual de '",p,"' es de ", zz, ", hacer pedido es recomendado")
#si zz >20:
print ("¡Gracias!, ahora la cantidad actual de '",p,"' es de ", zz, ". Hacer pedido no es necesario.")
