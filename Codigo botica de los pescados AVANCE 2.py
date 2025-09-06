primero = input("Buen dia, escriba '1' para registrar productos en el sistema, escriba '2' para revisar disponibilidad de productos, escriba '3' para hacer el reporte de ventas: ")

if primero == "1":
    p = input("Muy bien, por favor introduzca el nombre del articulo: ")
    x = int(input("Gracias, ahora introduzca la cantidad de '"+p+"' que se va a agregar al inventario: "))
    y = 0
    z = x+y
    print ("¡Gracias!, ahora la cantidad actual de '"+p+"' es de ", z, ".")

elif primero == "2":
#en este paso aun no se como hacer para definir que "z" es el valor que se da antes
    q = input("Claro, introduzca el nombre del articulo: ")
    q =
#aqui igual no se como hacer para que con solo el nombre, el programa sepa que articulo es y con base a su nombre y los datos ya antes dados sepa cuanto queda y asi hacer las operaciones
    qq = z
    if qq==0:
        print(q, "agotado.")
    elif qq > 0 and qq <=10:
        print("Solo quedan", z,"unidades, hacer pedido urgente.")
    elif qq>=11 and qq<=25:
        print("Quedan", z,"unidades, hacer pedido es recomendado.")
    elif qq>25:
        print("Quedan", z,"unidades. Hacer pedido no es necesario")
    
elif primero == "3":
    pp = input("¡Claro!, por favor introduzca el nombre del articulo: ")
    xx = int(input("Gracias, ahora introduzca la cantidad de '"  + pp + "' que se vendio esta semana: "))
    zz = z - xx
#aqui tampoco se como hacer para que me defina que z ya la di antes, como un guardado de datos.
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
