def calcular_imc(peso, altura):
    IMC = float(peso/(altura**2))
    return IMC

peso = float(input("Ingrese su peso corporal en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
IMC = calcular_imc(peso, altura)
print(f"Su Indice de Masa Corporal (IMC) es de: {IMC}")