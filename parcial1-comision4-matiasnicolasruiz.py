titulos_disponb = []
ejemplares = []
opcion = 0
bandera_ingresar_titulos = False
bandera_ingresar_ejemplares = False
print("\nBienvenido a la biblioteca escolar online, elija una opcion a continuación:\n")
print("Opcion 1 => Ingresar titulos nuevos.")
print("Opcion 2 => Ingresar ejemplares disponibles de libros.")
print("Opcion 3 => Mostrar el catalogo disponible actualmente.")
print("Opcion 4 => Mostrar disponibilidad de ejemplares.")
print("Opcion 5 => Consultar disponibilidad de ejemplares de los titulos.")
print("Opcion 6 => Listado de titulos agotados.")
print("Opcion 7 => Actualizar ejemplares (prestame/devolucion).")
print("Opcion 8 => Salir del programa.")
while opcion != 8:
    opcion = int(input("\nINGRESE la opcion que desee aquí: "))
    if opcion == 1:
        titulo = str(input("Ingrese el titulo a agregar: ")).lower()
        titulos_disponb.append(titulo)
        print("Titulo ingresado se ha guardado exitosamente. Para agregar otro más, vuelva a elegir la opcion 1.")
        bandera_datos_titulos = True
    elif opcion == 2:
        for ind in range(0, len(titulos_disponb)):
            agregar_ejemplar = int(input(f"Ingrese los ejemplares para el titulo {titulos_disponb[ind]}: "))
            if agregar_ejemplar < 0 or agregar_ejemplar >= 500:
                print("NO. Ingrese un valor igual o mayor a 0, o menor a 500 porque sinó se caen los servidores.")
            else:
                print("Se han guardado los ejemplares para el titulo respectivo.")
                ejemplares.append(agregar_ejemplar)
                bandera_datos_ejemplares = True
    elif opcion == 3:
        print("Se mostarán los titulos disponibles junto con sus ejemplares actuales...")
        if bandera_ingresar_titulos == False and bandera_ingresar_ejemplares == False:
            print("(No hay titulos ni ejemplares disponibles por el momento...)")
        for i in range(0, len(titulos_disponb)):
            print(f"Titulo: {titulos_disponb[i]}, ejemplares disponibles para éste: {ejemplares[i]}.")
        print("Eso es todo lo que hay hasta ahora en la biblioteca.")
    elif opcion == 4:
        if bandera_ingresar_titulos == False and bandera_ingresar_ejemplares == False:
            print("ERROR. No se han ingresado datos de titulos o ejemplares aún.")
        else:
            print("Consulte el titulo de un libro ingresado en específico para observar su cantidad de ejemplares disponibles")
            consulta_ejemplrs = str(input("AQUÍ: ")).lower()
            if consulta_ejemplrs in titulos_disponb:
                titulo_encontrado = titulos_disponb.index(consulta_ejemplrs)
            else:
                print("ERROR: El libro indicado no existe en la biblioteca.")
            print(f"El titulo {consulta_ejemplrs} tiene disponibles {ejemplares[titulo_encontrado]} ejemplares ;)")
    elif opcion == 5:
        print("Se mostrarán a continuación los titulos agotados.")
        titulo_agotado_encontrado = False
        for index in range(0, len(ejemplares)):
            if titulo_agotado_encontrado == False:
                if index == 0:
                    print(f"El titulo {titulos_disponb[index]}, tiene {index}. Por lo que está agotado.")
                    titulo_agotado_encontrado = True
            else:
                print("No se encontraron titulos agotados ;)")
    elif opcion == 7:
        if bandera_ingresar_titulos == False and bandera_ingresar_ejemplares == False:
            print("ERROR. No se han ingresado datos de titulos o ejemplares aún.")
        else:
            RTA_prestar_devolver = str(input("¿Desea llevarse una copia de en titulo o devolverla? (Ingrese P para llevar o D para devolver)")).lower()
            if RTA_prestar_devolver == "p":
                titulo_a_prestar = str(input("Ingrese el titulo para llevarse una copia de éste: "))
                if titulo_a_prestar in titulos_disponb:
                    indice_titulo_a_prestar = titulos_disponb.index(titulo_a_prestar)
                    ejemplares[indice_titulo_a_prestar] = ejemplares[indice_titulo_a_prestar - 1]
                    print(f"Usted se llevará una copia del libro {titulo_a_prestar}.")
                else:
                    print("Disculpe, no se ha encontrado el titulo en la biblioteca. Intentelo de nuevo.")
            elif RTA_prestar_devolver == "d":
                titulo_a_devolver = str(input("Ingrese el titulo a devolver: ")).lower()
                if titulo_a_devolver in titulos_disponb:
                    indice_titulo_a_devolver = titulos_disponb.index(titulo_a_devolver)
                    ejemplares[indice_titulo_a_devolver] = ejemplares[indice_titulo_a_devolver + 1]
                    print(f"Usted devolverá una copia prestada del libro {titulo_a_devolver}.")
                else:
                    print("Disculpe, no se ha encontrado el titulo en la biblioteca. intentelo de nuevo.")
            elif opcion == 8:
                print("Saliendo del programa... ")
            else:
                print("ERROR: Opcion no disponible. Por favor seleccione 1 de las opciones propuestas a la vez... ")