def main():
    def operacionesnum(num1, num2):
    resultado1 = num1 + num2
    resultado2 = num1 - num2
    resultado3 = num1 * num2
    resultado4 = num1 / num2
    return resultado1, resultado2, resultado3, resultado4

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operacionesnum(num1, num2)