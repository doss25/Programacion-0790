#Proyecto 1. David Solorzano V-23.643.775

print("     Sistema de Administración - Inventario para Ferreterias     ")

nombre = []
codigo = []
precio = []
stock = []

while True:
    print ("(1) Agregar Producto")
    print ("(2) Eliminar Producto")
    print ("(3) Buscar Producto")
    print ("(4) Actualizar Inventario")
    print ("(5) Inventario")
    print ("(6) Salir")

    abc = int(input("Coloque el numero con la opcion a realizar:   "))
    
    if abc == 1:
        nombre_producto = input("Nombre del producto a agregar: ")
        codigo_producto = int(input("Codigo del producto: "))
        precio_producto = float(input("Precio del producto ($): "))
        stock_producto = int(input("Cantidad del producto: "))

        nombre.append(nombre_producto)
        codigo.append(codigo_producto)
        precio.append(precio_producto)
        stock.append(stock_producto)
        
    
    elif abc == 2:
        nombre_producto = input("Nombre del producto a eliminar: ")
        codigo_producto = int(input("Codigo del producto: "))
        stock_producto = int(input("Cantidad del producto: "))
        precio_producto = float(input("Precio del producto ($): "))

        nombre.remove(nombre_producto)
        codigo.remove(codigo_producto)
        stock.remove(stock_producto)
        precio.remove(precio_producto)

    elif abc == 3:
        busqueda = input(("Nombre del producto de desea buscar: "))
        buscador = nombre.index(busqueda)
        print ("El nombre del producto es, ", nombre[buscador])
        print ("El codigo del producto es, ", codigo[buscador])
        print ("El precio del producto es, ", precio[buscador])
        print ("El Stock del producto es, ", stock[buscador])

    elif abc == 4:
        busqueda = input(("Nombre del producto de desea actualizar: "))
        buscador = nombre.index(busqueda)
        nombre_producto = input("Nombre del producto para Actualizar: ")
        codigo_producto = int(input("Codigo del producto: "))
        stock_producto = int(input("Cantidad del producto: "))
        precio_producto = float(input("Precio del producto ($): "))

        nombre[buscador] = nombre_producto
        codigo[buscador] = codigo_producto
        stock[buscador] = stock_producto
        precio[buscador] = precio_producto

    elif abc == 5:
        print(f"{nombre} - Codigo: {codigo}, Precio ($): {precio}, Cantidad: {stock}")

    elif abc == 6:
        break
    else:
        print("Opcion invalida, Intentelo nuevamente")

print("Gracias por utilizar el sistema de Administración para inventario de una Ferreteria")