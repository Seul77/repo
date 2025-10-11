#cantidad de productos inicial y sus respectivos precios iniciales:
#para el nuevo avance, inclui esta matriz para poder tener tambien los precios de los productos
productos= {
"pomada": {"cantidad": 20, "precio": 55.00},
"paracetamol": {"cantidad": 16, "precio": 12.50},
"jabon": {"cantidad": 16, "precio": 35.00},
"cerave": {"cantidad": 20, "precio": 250.00},
"bloqueador": {"cantidad": 18, "precio": 150.00},
"shampoo": {"cantidad": 10, "precio": 80.00}
}


def ciclo_inicial():
    global productos #investigue por mi cuenta que el comando global hace que declara que una variable existe fuera de la funcion,
                     #haciendo que pueda modificar su valor y este guardado mientras el programa este operando.
    primero = input("Buen dia,"'\n'
                    "Escriba 'registro' para registrar productos en el sistema," '\n'
                    "Escriba 'revision' para revisar disponibilidad de productos,"'\n'
                    "Escriba 'reporte' para hacer el reporte de ventas,"'\n'
                    "Escriba 'actualizar' para actualizar el precio de algun articulo"'\n'
                    "O escriba 'salir' si quiere concluir con el programa: ")
    while primero != 'registro' or primero != 'revision' or primero != 'reporte' or primero != 'salir' or primero != 'actualizar':

        if primero == "registro":
            registro_de_productos()
        elif primero == "revision":
            revision_de_productos()
        elif primero == "reporte":
            reporte_de_ventas()
        elif primero == "actualizar":
            actualizar_precio()
        elif primero == 'salir':
            print ('\n''Gracias! Nos vemos pronto :)''\n')
            break
        else:
            primero=input('Hmm, tal vez lo escribiste mal, revisa tu ortografia e intentalo de nuevo: ')

        
def registro_de_productos():
    global productos
    p = input("Muy bien, por favor introduzca el nombre del articulo para registrar: ")
    if p in productos:
        x = int(input("Gracias, ahora introduzca la cantidad de '"+p+"' que se va a agregar al inventario: "))
        productos[p]["cantidad"] += x
        print ('\n'"¡Gracias!, ahora la cantidad actual de '"+p+"' es de " +str(productos[p]['cantidad'])+ ".\n")
    else:
        print ('\n'"Hmm, no encuentro el producto "+p+", revisa tu ortografia e intentalo de nuevo."'\n')
    return ciclo_inicial()    
    
        
def revision_de_productos():
    global productos
    q = input("Claro, introduzca el nombre del articulo: ")
    if q in productos:
        cantidad = productos.get(q)['cantidad']
        if cantidad==0:
            print('\n',q, "agotado.\n")
        elif cantidad > 0 and cantidad <=10:
            print('\n'"Solo quedan", cantidad,"unidades, hacer pedido urgente.\n")
        elif cantidad>=11 and cantidad<=25:
            print('\n'"Quedan", cantidad,"unidades de "+q+", hacer pedido es recomendado.\n")
        elif cantidad>25:
            print('\n'"Quedan", cantidad,"unidades. Hacer pedido no es necesario\n")
    else:
        print ('\n'"Hmm, no encuentro el producto "+q+", revisa tu ortografia e intentalo de nuevo."'\n')
    return ciclo_inicial()    

            
def reporte_de_ventas():
    global productos
    pp = input("¡Claro!, por favor introduzca el nombre del articulo que se vendió: ")
    if pp in productos:
        xx = int(input("Gracias, ahora introduzca la cantidad de "+pp+" que se vendio esta semana: ")) 
        cantidad_actual = productos[pp]["cantidad"]
        zz = cantidad_actual - xx
        if zz < 0:
            print ('\n'"Hmm, el numero de ventas es mayor al numero de articulos en el inventario. Revisa bien los datos e intentalo de nuevo.")
        else:
            productos[pp]["cantidad"] = zz 
            if zz == 0:
                print ('\n'"¡El producto '",pp,"' esta agotado! Es necesario hacer pedido.\n")
            elif zz > 0 and zz <=10:
                print ('\n'"¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ", se requiere hacer pedido.\n")
            elif zz >=11 and zz <=20:
                print ('\n'"¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ", hacer pedido es recomendado\n")
            elif zz>20:
                print ('\n'"¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ". Hacer pedido no es necesario.\n")
    else:
        print ('\n'"Hmm, no encuentro el producto "+pp+", revisa tu ortografia e intentalo de nuevo."'\n')
    return ciclo_inicial()    



def actualizar_precio():
    global productos
    jk=input("Introduzca el nombre del articulo cuyo precio desea actualizar: ")
    if jk in productos:
        precio_actual=productos[jk]["precio"]
        print ("Su precio actual es de",precio_actual,".")
        ok=input("Introduzca el nuevo precio: ")
        precio_nuevo=float(ok)
        productos[jk]['precio']=precio_nuevo
        print('\n'"El nuevo precio de ",jk, " es de: " ,precio_nuevo,'\n')
    else:
        print('\n'"No encuentro el articulo ", jk, ", revisa tu ortografia e intentalo nuevamente."'\n')
    return ciclo_inicial()

(ciclo_inicial())



