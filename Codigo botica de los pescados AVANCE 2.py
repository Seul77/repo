primero = input("Buen dia, escriba 'registro' para registrar productos en el sistema, escriba 'revision' para revisar disponibilidad de productos, escriba 'reporte' para hacer el reporte de ventas: ")

##en el avance anterior me confundi, puse condicionales en lugar de funciones, para cuando entregue el avance final ya tendra las funciones pero por ahora tengo los condicionales de if.


        
if primero == "registro":
    p = input("Muy bien, por favor introduzca el nombre del articulo: ")
    prod = input("Ok, presione '5' si este articulo ya estaba en el inventario, presione '6' si es nuevo y no habia en inventario: ")
    if prod == "5":
        vi = int(input ("Por favor introduzca la cantidad que ya estaba en inventario: "))
        x = int(input("Gracias, ahora introduzca la cantidad de '"+p+"' que se va a agregar al inventario: "))
        z = vi + x
    elif prod == "6":
        vi = 0
        x = int(input("Gracias, ahora introduzca la cantidad de '"+p+"' que se va a agregar al inventario: "))
        z = vi + x
    print ("¡Gracias!, ahora la cantidad actual de '"+p+"' es de ", z, ".")

elif primero == "revision":

        q = input("Claro, introduzca el nombre del articulo: ")
        qq=10
        if qq==0:
            print(q, "agotado.")
        elif qq > 0 and qq <=10:
            print("Solo quedan", qq,"unidades, hacer pedido urgente.")
        elif qq>=11 and qq<=25:
            print("Quedan", qq,"unidades, hacer pedido es recomendado.")
        elif qq>25:
            print("Quedan", qq,"unidades. Hacer pedido no es necesario")
        
elif primero == "reporte":
        z = 10
        pp = input("¡Claro!, por favor introduzca el nombre del articulo: ")
        xx = int(input("Gracias, ahora introduzca la cantidad de '"  + pp + "' que se vendio esta semana: "))
        zz = z - xx
        if zz < 0:
            print ("Hmm, el numero de ventas es mayor al numero de articulos en el inventario. Revisa bien los datos e intentalo de nuevo.")
        elif zz==0:
            print ("¡El producto '",pp,"' esta agotado! Solo hay ", zz, ",es necesario hacer pedido.")
        elif zz > 0 and zz <=10:
            print ("¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ", se requiere hacer pedido.")
        elif zz >=11 and z <=20:
            print ("¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ", hacer pedido es recomendado")
        elif zz>20:
            print ("¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ". Hacer pedido no es necesario.")
        

else:
    print ('Hmm, tal vez lo escribiste mal, revisa tu ortografia e intentalo de nuevo.')


