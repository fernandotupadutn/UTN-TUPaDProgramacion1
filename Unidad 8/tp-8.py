import os
lista_pro={}

if not os.path.exists('productos.txt'):
   with open('productos.txt','w') as archivo_add:
    archivo_add.write("Lapicera,120.5,30\n")
    archivo_add.write("Cuaderno,350.0,20\n")
    archivo_add.write("Goma de borrar,80.75,20\n")  


def nuevo_elemento(nombre,precio,cantidad):
   lista_nueva={
      'nombre':nombre,
      'precio':precio,
      'cantidad':cantidad
   }
   return lista_nueva

def lista_diccionario():
   productos=[]
   with open('productos.txt','r') as archivo_leer:
    for linea in archivo_leer:
        linea_limpia=linea.strip().split(',')
        productos.append(nuevo_elemento(linea_limpia[0],linea_limpia[1],linea_limpia[2]))
    return productos
   
productos=lista_diccionario()
   
def mostar_datos(datos):
   for datos_crudos in datos:
      print(f'Producto:{datos_crudos['nombre']} | Precio:${datos_crudos['precio']} | Cantidad: {datos_crudos['cantidad']}')
  

mostar_datos(productos)
nuevos_producto=input('ingrese el producto: ')
nuevo_precio=input('ingrese el precio: ')
nuevo_stock=input('ingrese la cantidad: ')
agregar_ultimo=(nuevos_producto,nuevo_precio,nuevo_stock)
productos.append(nuevo_elemento(nuevos_producto,nuevo_stock,nuevo_stock))
agregar_al_txt=f"{nuevos_producto},{nuevo_precio},{nuevo_stock}\n"
with open('productos.txt','a') as archivo_add:
     archivo_add.write(agregar_al_txt)




lista_diccionario()

print(productos)

# mostar_datos(productos)

buscar=input('buscar producto')
encontrado=False


for producto in productos:
   if producto['nombre']==buscar:
      print('Producto encontrado: ',producto)
      nombre_nuevo  =input('actualizar nombre: ')
      precio_nuevo  =input('actualizar precio: ')
      cantidad_nuevo=input('actualizar cantidad: ')
      producto['nombre']=nombre_nuevo   
      producto['precio']=precio_nuevo   
      producto['cantidad']=cantidad_nuevo
      encontrado=True

if encontrado:
   with open('productos.txt','w') as actualizar:
      
    for pro in productos:
      actualizacion=f'{pro['nombre']},{pro['precio']},{pro['cantidad']}\n'
      actualizar.write(actualizacion)

if encontrado==False:
      print('producto no encontrado')


mostar_datos(productos)
