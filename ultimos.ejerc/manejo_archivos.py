opcion = input("Ingrese la opción deseada: ")
bucle = True
while bucle:
    if opcion == "si":
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            cantidad = int(input("¿Cuántos productos desea ingresar? "))
            for i in range(cantidad):
                producto = str(input(f"Ingrese el nombre del producto {i+1}: ")).lower()
                precio = float(input(f"Ingrese el precio del producto {i+1}: "))
                cantidad = int(input(f"Ingrese la cantidad del producto {i+1}: "))
                archivo.write(f"{producto},${precio},{cantidad}\n")
        print("Productos guardados exitosamente.")
        opcion = input("¿Desea ingresar más productos? (si/no): ")
        if opcion == "si":
            continue
        else:
            bucle = False
            print("\nPrograma finalizado.\n")
    elif opcion == "no":
        bucle = False
    else:
        print("Opción no válida. Por favor, ingrese 'si' o 'no'.")