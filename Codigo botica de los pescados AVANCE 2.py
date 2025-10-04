#cantidad de productos inicial:
#estos son los articulos disponibles y su cantidad
#el avance es este diccionario, el profe me dijo que si contaba como avance de como lista
productos= {
"pomada":20,
"paracetamol":16,
"jabon":16,
"cerave":10,
"bloqueador":18
}


def cantidad_pomada(cantidad):
    pomadac=20+cantidad
    return pomadac

def cantidad_paracetamol(cantidad):
    paracetamolc=16+cantidad
    return paracetamolc

def cantidad_jabon(cantidad):
    jabonc=25+cantidad
    return jabonc

def cantidad_cerave(cantidad):
    ceravec=10+cantidad
    return ceravec

def cantidad_bloqueador(cantidad):
    bloqueadorc=18+cantidad
    return bloqueadorc

def ciclo_inicial():
    primero = input("Buen dia, escriba 'registro' para registrar productos en el sistema, escriba 'revision' para revisar disponibilidad de productos, escriba 'reporte' para hacer el reporte de ventas: ")
    while primero != 'registro' or primero !='revision' or primero !='reporte' or primero !='salir':
        if primero == "registro":
            p = input("Muy bien, por favor introduzca el nombre del articulo: ")
            x = int(input("Gracias, ahora introduzca la cantidad de '"+p+"' que se va a agregar al inventario: "))
            if p == "pomada":
                print ("¡Gracias!, ahora la cantidad actual de '"+p+"' es de ", (cantidad_pomada(x)), ".")
            elif p=="paracetamol":
                print ("¡Gracias!, ahora la cantidad actual de '"+p+"' es de ", (cantidad_paracetamol(x)), ".")
            elif p=="jabon":
                print ("¡Gracias!, ahora la cantidad actual de '"+p+"' es de ", (cantidad_jabon(x)), ".")
            elif p=="cerave":
                print ("¡Gracias!, ahora la cantidad actual de '"+p+"' es de ", (cantidad_cerave(x)), ".")
            elif p=="bloqueador":
                print ("¡Gracias!, ahora la cantidad actual de '"+p+"' es de ", (cantidad_bloqueador(x)), ".")
            else:
                print("hmm, no encuentro el articulo'"+p+"', revisa tu ortografia e intentalo de nuevo.")
            return ciclo_inicial()

        elif primero == "revision":
                q = input("Claro, introduzca el nombre del articulo: ")
                cantidad = productos.get(q)
                if cantidad==0:
                    print(q, "agotado.")
                elif cantidad > 0 and cantidad <=10:
                    print("Solo quedan", cantidad,"unidades, hacer pedido urgente.")
                elif cantidad>=11 and cantidad<=25:
                    print("Quedan", cantidad,"unidades, hacer pedido es recomendado.")
                elif cantidad>25:
                    print("Quedan", cantidad,"unidades. Hacer pedido no es necesario")
                else:
                    print("hmm, no encuentro el articulo'"+q+"', revisa tu ortografia e intentalo de nuevo.")
                return ciclo_inicial()
                
        elif primero == "reporte":
                pp = input("¡Claro!, por favor introduzca el nombre del articulo: ")
                xx = int(input("Gracias, ahora introduzca la cantidad de '"  + pp + "' que se vendio esta semana: "))
                cantidad = productos.get(pp)
                zz = cantidad - xx
                if zz < 0:
                    print ("Hmm, el numero de ventas es mayor al numero de articulos en el inventario. Revisa bien los datos e intentalo de nuevo.")
                elif zz==0:
                    print ("¡El producto '",pp,"' esta agotado! Es necesario hacer pedido.")
                elif zz > 0 and zz <=10:
                    print ("¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ", se requiere hacer pedido.")
                elif zz >=11 and zz <=20:
                    print ("¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ", hacer pedido es recomendado")
                elif zz>20:
                    print ("¡Gracias!, ahora la cantidad actual de '",pp,"' es de ", zz, ". Hacer pedido no es necesario.")
                return ciclo_inicial()
        elif primero == 'salir':
            print ('Gracias! Nos vemos pronto :)')
            break
            
        else:
            primero=input('Hmm, tal vez lo escribiste mal, revisa tu ortografia e intentalo de nuevo: ')          


(ciclo_inicial())

