
#Validaciones diccionario Productos

def validar_codigo(codigo):
    if codigo and codigo.strip():
        return True
    return False

def validar_nombre(nombre):
    if nombre and nombre.strip():
        return True
    return False

def validar_categoria(categoria):
    if categoria and categoria.strip():
        return True
    return False

def validar_marca(marca):
    if marca and marca.strip():
        return True
    return False

def validar_peso (peso_kg):
    if peso_kg > 0:
        return True
    return False

def validar_importacion(importado):
    if importado == "s":
        return True
    elif importado == "n":
        return False
    else:
        print ("Seleccione una opcion entre (s/n).")

def validar_cachorro(cachorro):
    if cachorro == "s":
        return True
    elif cachorro == "n":
        return False
    else:
        print ("Seleccione una opcion entre (s/n).")

#Validaciones diccionario Stock

def validar_precio (precio):
    if precio > 0:
        return True
    return False

def validar_unidades (unidades):
    if unidades >= 0:
        return True
    return False

def mostrar_menu ():
    print ("""
    ========== MENÚ PRINCIPAL ==========
    1. Unidades por categoría
    2. Búsqueda de productos por rango de precio
    3. Actualizar precio de producto
    4. Agregar producto
    5. Eliminar producto
    6. Salir
    =====================================
    """)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion (1-6): "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: Opcion fuera de rango. Intente nuevamente.")
        except ValueError:
            print("Error: Debe ingresar un número entero valido.")

def busqueda_precio(p_min, p_max):
    if p_min > p_max:
        return False 
    elif p_min < 0 and p_max < 0:
        return False
    return True

def buscar_codigo(stock, codigo):
    for i in range(len(stock)):
        if stock[i]["codigo"] == codigo:
            return True
    return False

def actuaclizar_precio(codigo, nuevo_precio, productos):
    buscar_codigo(codigo)
    if buscar_codigo:
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio: \n"))
            productos["precio"] == nuevo_precio
        except ValueError:
            print("Ingrese un precio valido.")
    else: 
        print("El codigo ingresado no existe.")

def agregar_producto(productos, stock):
    print("\nRegistrar Nuevo Producto")

    codigo = input("Ingrese el código del producto: ").strip()
    if not validar_codigo(codigo):
        print("Error: El código no puede estar vacío.")
        return

    if buscar_codigo(productos, codigo) != False:
        print("Error: El código ya se encuentra registrado.")
        return

    nombre = input("Ingrese nombre del producto: ").strip()
    if not validar_nombre(nombre):
        print("Error: El nombre no puede estar vacío.")
        return

    categoria = input("Ingrese la categoria del producto: ").strip().lower()
    if not validar_categoria(categoria):
        print("La categoria no puede estar vacia.")
        return
    
    marca = input("Ingrese la marca del producto: ").strip().lower()
    if not validar_marca(marca):
        print("La categoria no puede estar vacia.")
        return

    try:
        peso_kg = float(input("Ingrese el peso del producto: "))
        if not validar_peso(peso_kg):
            print("ERROR: El peso no puede ser menor a 0.")
            return
    except ValueError:
        print("Error: Debe ingresar un número mayor a cero.")
        return

    try:
        importado = input("¿Es importado? (s/n): ")
        if not validar_importacion(importado):
            print("Error: Seleccione s o n segun corresponda.")
            return
    except ValueError:
        print("Error: No puede ingresar numeros")
        return
    
    try:
        cachorro = input("¿Es para cachorro? (s/n): ")
        if not validar_cachorro(cachorro):
            print("Error: Seleccione s o n segun corresponda.")
            return
    except ValueError:
        print("Error: No puede ingresar numeros")
        return
    
    try:    
        precio = int(input("Ingrese el precio del prducto: "))
        if not validar_precio(precio):
            print ("ERROR: El precio no puede ser menor a cero.")
            return
    except ValueError:
        print("Solo se pueden ingresar numeros enteros")
        return
    
    try:
        unidades= int(input("Por favor inrese las unidades del producto: "))
        if not validar_unidades(unidades):
            print("Las unidades no pueden ser menor a cero.")
            return
    except ValueError:
        print("Solo se pueden ingresar numeros enteros.")
        return

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "marca": marca,
        "peso": peso_kg,
        "importado": importado,
        "cachorro": cachorro,
        "precio": precio,
        "unidades": unidades
    }

    productos.append(nuevo_producto)
    print(f"¡Producto {codigo} registrado con éxito!")

def eliminar_producto(productos, codigo):
    posicion = buscar_codigo(productos, codigo)

    if posicion != False:
        productos.pop(posicion)
        print(f"¡El producto {codigo} fue eliminado exitosamente!")
    else:
        print("Error: El producto no se encuentra registrado.")

def buscar_categoria (categoria, productos):
    for categoria in productos:
        if categoria == productos["categoria"]:
            productos[categoria]
        else:
            print("No tenemos esa categoria.")

def main():
    productos = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 4:
            agregar_producto(productos)

        elif opcion == 3:
            print("Actualizar precio poructo")
            codigo = input("Ingrese el código a buscar: ").strip()
            pos = buscar_codigo(productos, codigo)
            if pos != False:
                print("\¡Producto Encontrado!")
                nuevo_precio = int(input("Ingrese el nuevo precio del producto"))
                if actuaclizar_precio(codigo, nuevo_precio, productos):
                    print("El precio ha sido actualizado.")
            else:
                print("El producto con ese código no existe.")

        elif opcion == 5:
            print("\n--- Eliminar producto ---")
            codigo = input("Ingrese el código del producto a eliminar: ").strip()
            eliminar_producto(productos, codigo)

        elif opcion == 1:
            print("\n--- Busqueda por categoria ---")
            categoria = input("Ingrese la categoria: ").strip()
            buscar_categoria(categoria, productos)

        elif opcion == 2:
            p_min = int(input("Ingrese el precio minimo: "))
            p_max = int(input("Ingrese el precio maximo: "))
            busqueda_precio(p_min, p_max)

        elif opcion == 6:
            print("\nprograma finalizado")
            break

if __name__ == "__main__":
    main()