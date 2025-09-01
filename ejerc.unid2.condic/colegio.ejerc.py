#Ejercicio práctico en clases:
dia_sem = input("Ingrese un dia laboral de la semana (en letras): ").lower()
dia_sem_num = int(input("Ingrese el dia de la fecha: "))
num_mes = int(input("Ingrese el número del mes: "))

print(dia_sem, "/", dia_sem_num, "/", num_mes)
dias_clases = ["lunes", "martes", "miercoles", "jueves", "viernes"]

if (dia_sem not in dias_clases) or (dia_sem_num < 1 or dia_sem_num > 31) or (num_mes < 1 or num_mes > 12):
    print("ERROR: Un dato o datos ingresados fueron incorrectos.")
elif (dia_sem in dias_clases) and (dia_sem_num <= 31 and dia_sem_num >= 1) and (num_mes >= 1 and num_mes <= 12):
    if dia_sem in ["lunes", "martes", "miercoles"]:
        toma_examen = str(input("¿Se tomaron exámenes? (si/no): ")).lower()
        if toma_examen == "si":
            cant_aprob = int(input("Ingrese la cantidad de alumnos aprobados: "))
            cant_desaprob = int(input("Ingrese la cantidad de alumnos reprobados: "))
            total = cant_aprob + cant_desaprob
            if total > 0:
                promedio_aprob = round(cant_aprob * 100 / total)
                print(f"Porcentaje de aprobados por promedio: {promedio_aprob}% .")
            else:
                print("No hay alumnos para calcular el porcentaje.")
        elif toma_examen == "no":
            print("No se tomaron exámenes.")
            print(" ")
        else:
            print("Opción no válida.")
    elif dia_sem in ["jueves"]:
        print("Los dias jueves hay clases de practica hablada.")
        print(" ")
        porcentaje_asist = int(input("Ingrese el porcentaje de alumnos que asistieron a la clase: "))
        if porcentaje_asist == 0:
            print("No asistieron alumnos a la clase.")
        elif porcentaje_asist == 100:
            print("Asistieron todos los alumnos.")
        elif porcentaje_asist < 50:
            print("No asistió la mayoría")
        elif porcentaje_asist > 50:
            print("Asistió la mayoría")
        elif porcentaje_asist == 50:
            print("Asistieron la mitad de los alumnos.")
        else:
            print("Porcentaje de asistencia invalido .")
    else:
        if dia_sem in ["viernes"] and dia_sem_num == 1 and (num_mes == 7 or num_mes == 1):
            print("Comienza un nuevo ciclo.")
            cant_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
            arancel = int(input("Ingrese el arancel para los alumnos: "))
            print(f"El total recaudado por el arancel es de: ${cant_alumnos * arancel}.")
        else:
            print("Los dias Viernes se dicta inglés para extranjeros.")
            print("NO comienza un nuevo ciclo :(")
#Hasta acá llega el ejercicio, GRACIAS.