import sys
import os

print('''MENÚ:
1. Tabla de multiplicar
2. Ordenar 3 numeros
3. IMC ideal
4. Figuras geométricas
''')
opt = int(input("Selecciona una de las opciones del menú --> "))


def tabla():
    numero = int(input("Introduce número para calcular la tabla de multiplicar --> "))
    contador = 1
    while contador <= numero:
        resultado = numero * contador
        print("{} x {} = {}".format(numero, contador, resultado))
        contador = contador + 1


def mayor():
    num1 = int(input("Introduce número 1 --> "))
    num2 = int(input("Introduce número 2 --> "))
    num3 = int(input("Introduce número 3 --> "))
    while True:
        if num1 > num2 and num1 > num3:
            resultado = num1
        if num2 > num1 and num2 > num3:
            resultado = num2
        if num3 > num1 and num3 > num2:
            resultado = num3
        print("El número mayor introducido es: {}".format(resultado))
        break


def imc():
    peso = float(input("Introduce tu peso en kg --> "))
    estatura = float(input("Introduce tu estatura en m --> "))
    imc = peso/(estatura*estatura)
    print("Tu IMC ideal es: {}".format(imc))


def figuras():
    altura = int(input("Introduce la altura de la figura geométrica --> "))
    anchura = int(input("Introduce la anchura de la figura geométrica --> "))
    i = 0
    j = 0
    for i in range(altura):
        for j in range(anchura):
            print("*", end=" ")
        print(end="\n")
        i = i + 1
    print(end="\n")


while True:
    if opt == 1:
        tabla()
    if opt == 2:
        mayor()
    if opt == 3:
        imc()
    if opt == 4:
        figuras()
    if opt != 1 and opt != 2 and opt != 3 and opt != 4:
        print("Introduce un número correcto")
    break

os.system("cls")  # esto no sé en realidad que hace...

sys.exit()
