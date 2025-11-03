def calcular_promedio(prom1, prom2, prom3):
    prom_final = float((prom1 + prom2 + prom3)/3)
    return prom_final

promedio1 = float(input("Ingrese el primer promedio: "))
promedio2 = float(input("Ingrese el segundo promedio: "))
promedio3 = float(input("Ingrese el tercer promedio: "))
if 0 <= promedio1 <= 10 and 0 <= promedio2 <= 10 and 0 <= promedio3 <= 10:
    prom_final = calcular_promedio(promedio1, promedio2, promedio3)
    print(f"El promedio final de los 3 promedios ingresados es de: {prom_final}")
    print(f"Mientras que el mismo pero redondeado sería de: {round(prom_final)}")
    print("\nGracias!")
else:
    print("ERROR: Ingresó un número fuera del rango de notas.")