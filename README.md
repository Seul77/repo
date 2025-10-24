# Sistema de inventario "La Botica de los Pescados"

## Contexto:
La Botica de los Pescados es una farmacia naturista que se encuentra en un pequeño pueblo de Jalisco, es un negocio familiar que ha pasado de un pariente a otro. Hoy, tienen un sistema el cual les marca los productos que les indica solamente los productos que ya se vendieron. El problema es que los trabajadores manualmente tienen que hacer pedido de los productos que estan agotados o proximos a acodarse. Por esto los errores son comunes, por ejemplo no compran los suficientes productos necesarios para venderse, o compran productos de mas pensando que no habia en inventario. 

Para resolver este problema, mi programa va a estar al tanto de los productos que esten proximos a agotarse, y cuando lo esten notificar que hay productos que necesitan comprarse. Tambien, cuando se haga un pedido para comprar productos, registrara la cantidad de productos comprados y conforme se vayan vendiendo el programa los descontara del sistema, asi se podra tener un control sobre ellos y no se va a tener que estar revisando fisicamente el inventario cada que se tenga la duda de la disponibilidad de un articulo. Esto dara facilidad y eficiencia al vendedor para brindar un servicio mas rapido y estar al tanto del inventario de la farmacia. 

## Instrucciones: 
1. Descarga el codigo
2.     Codigo botica de los pescados.py
3. Corre el codigo en la terminal
4. Primero que nada, ingresa la cantidad de producto para cada uno usando 'registro', ya que la cantidad inicial de todos es 0 (ej. pomada, cantidad a agregar: 30, paracetamol, cantidad a agregar: 25,...)
5. Ya que tienes eso, puedes hacer libremente las siguientes operaciones (registro, revision, reporte, actualizar)
6. Cuando hayas terminado, escribe 'salir' para terminar el programa.

## Algoritmo: 

En el registro:

Producto x tiene 0 de cantidad inicial.

Para registrar, cantidad de producto x + cantidad a agregar
Ahora esa cantidad se hace la cantidad actual.


En revision:

si producto x tiene menos de la cantidad ideal, notificar pedido
si producto x tiene mas de la cantidad ideal, notificar que pedido es opcional


En reporte:

Si producto x tuvo 5 (por ejemplo) ventas en la semana, se le resta a la cantidad que se tenia, y dependiendo de su cantidad final, notificar pedido necesario o no.


En actualizar:

Si producto x tiene un precio inicial de 40 (por ejemplo), actualizar su precio y que ahora su precio actual sea el que se le da.


##### Bibliotecas:

La biblioteca sys me ayuda a que, cuando se le indique el mensaje, el programa termine despues de la indicacion. La biblioteca time, me ayuda a hacer el codigo mas amigable con el usuario, para darle un toque humano y un poco mas lento para que el usuario pueda procesar facilmente lo que pasa. 
