# 1) Imprimir "Hola Mundo!"
print("Hola Mundo!")

# 2) Solicitar el nombre del usuario e imprimir un saludo
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Solicitar nombre, apellido, edad y lugar de residencia, e imprimirlos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4) Calcular el área y perímetro de un círculo dado su radio
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

# 5) Convertir segundos a horas
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas:.2f} horas")

# 6) Imprimir la tabla de multiplicar de un número
numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7) Operaciones matemáticas con dos números
num1 = int(input("Ingrese el primer número entero distinto de 0: "))
num2 = int(input("Ingrese el segundo número entero distinto de 0: "))
suma = num1 + num2
division = num1 / num2
multiplicacion = num1 * num2
resta = num1 - num2
print(f"Suma: {suma}, División: {division:.2f}, Multiplicación: {multiplicacion}, Resta: {resta}")

# 8) Calcular el Índice de Masa Corporal (IMC)
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su Índice de Masa Corporal es: {imc:.2f}")

# 9) Convertir temperatura de Celsius a Fahrenheit
temp_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temp_fahrenheit = (9/5) * temp_celsius + 32
print(f"Temperatura en Fahrenheit: {temp_fahrenheit:.2f}")

# 10) Calcular el promedio de tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es: {promedio:.2f}")