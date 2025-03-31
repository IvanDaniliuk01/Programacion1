# -*- coding: utf-8 -*-
"""
Daniliuk Ivan
Resolución del Trabajo Práctico N° 3: Estructuras Condicionales
Tecnicatura Universitaria en Programación - UTN
"""

import statistics
import random
from datetime import date # Importado para el ejercicio 10, aunque no es estrictamente necesario

# --- Ejercicio 1 ---
print("\n--- Ejercicio 1 ---")
try:
    edad_usuario = int(input("Ingrese su edad: "))
    if edad_usuario >= 18:
        print("Es mayor de edad")
    # No se especifica un mensaje si es menor, así que no se añade 'else'.
except ValueError:
    print("Error: Por favor, ingrese un número válido para la edad.")

# --- Ejercicio 2 ---
print("\n--- Ejercicio 2 ---")
try:
    nota_usuario = float(input("Ingrese su nota: "))
    if nota_usuario >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")
except ValueError:
    print("Error: Por favor, ingrese un número válido para la nota.")

# --- Ejercicio 3 ---
print("\n--- Ejercicio 3 ---")
try:
    numero_ingresado = int(input("Ingrese un número par: "))
    if numero_ingresado % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")
except ValueError:
    print("Error: Por favor, ingrese un número entero.")

# --- Ejercicio 4 ---
print("\n--- Ejercicio 4 ---")
try:
    edad_categoria = int(input("Ingrese su edad para determinar la categoría: "))
    if edad_categoria < 0:
        print("Error: La edad no puede ser negativa.")
    elif edad_categoria < 12:
        print("Categoría: Niño/a")
    elif edad_categoria < 18: # Ya sabemos que es >= 12 por el 'elif' anterior
        print("Categoría: Adolescente")
    elif edad_categoria < 30: # Ya sabemos que es >= 18
        print("Categoría: Adulto/a joven")
    else: # Si no entró en ninguna anterior, es >= 30
        print("Categoría: Adulto/a")
except ValueError:
    print("Error: Por favor, ingrese un número válido para la edad.")

# --- Ejercicio 5 ---
print("\n--- Ejercicio 5 ---")
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")
longitud_contrasena = len(contrasena)

if longitud_contrasena >= 8 and longitud_contrasena <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# --- Ejercicio 6 ---
print("\n--- Ejercicio 6 ---")
# Generar la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
print(f"Lista generada: {numeros_aleatorios}") # Mostramos la lista para referencia

try:
    # Calcular moda, mediana y media
    # Nota: La moda puede generar un error si no hay un valor que se repita más que otros.
    # Usamos un try-except para manejar el caso de que no haya una única moda (StatisticsError)
    # o si la lista estuviera vacía (aunque aquí sabemos que tiene 50 elementos).
    media = statistics.mean(numeros_aleatorios)
    mediana = statistics.median(numeros_aleatorios)
    moda = statistics.mode(numeros_aleatorios)

    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")

    # Determinar el sesgo
    if media > mediana and mediana > moda:
        print("Resultado: Sesgo positivo o a la derecha")
    elif media < mediana and mediana < moda:
        print("Resultado: Sesgo negativo o a la izquierda")
    elif media == mediana and mediana == moda:
        print("Resultado: Sin sesgo")
    else:
        # Cubre otros casos posibles (ej. media == mediana != moda)
        # El criterio del ejercicio es estricto, así que los otros casos no tienen un nombre específico según el enunciado.
        print("Resultado: La relación entre media, mediana y moda no corresponde a un sesgo claramente definido según el criterio.")

except statistics.StatisticsError:
    print("Resultado: No se pudo determinar una única moda para calcular el sesgo.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


# --- Ejercicio 7 ---
print("\n--- Ejercicio 7 ---")
frase_palabra = input("Ingrese una frase o palabra: ")
# Convertimos a minúscula para chequear la última letra sin importar el caso
ultima_letra = frase_palabra.lower()[-1] if frase_palabra else '' # Chequeo si el string no está vacío

if ultima_letra in 'aeiouáéíóú': # Incluimos vocales con tilde
    resultado_frase = frase_palabra + "!"
else:
    resultado_frase = frase_palabra

print(f"Resultado: {resultado_frase}")

# --- Ejercicio 8 ---
print("\n--- Ejercicio 8 ---")
nombre_usuario = input("Ingrese su nombre: ")
print("Seleccione una opción:")
print("1. Convertir a mayúsculas")
print("2. Convertir a minúsculas")
print("3. Poner la primera letra en mayúscula (nombre propio)")

try:
    opcion = int(input("Ingrese el número de la opción deseada (1, 2 o 3): "))

    if opcion == 1:
        nombre_transformado = nombre_usuario.upper()
        print(f"Resultado: {nombre_transformado}")
    elif opcion == 2:
        nombre_transformado = nombre_usuario.lower()
        print(f"Resultado: {nombre_transformado}")
    elif opcion == 3:
        nombre_transformado = nombre_usuario.title()
        print(f"Resultado: {nombre_transformado}")
    else:
        print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

except ValueError:
    print("Error: Por favor, ingrese un número (1, 2 o 3).")

# --- Ejercicio 9 ---
print("\n--- Ejercicio 9 ---")
try:
    magnitud_terremoto = float(input("Ingrese la magnitud del terremoto en la escala de Richter: "))

    if magnitud_terremoto < 3:
        clasificacion = "Muy leve (imperceptible)"
    elif magnitud_terremoto < 4: # Ya sabemos que es >= 3
        clasificacion = "Leve (ligeramente perceptible)"
    elif magnitud_terremoto < 5: # Ya sabemos que es >= 4
        clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
    elif magnitud_terremoto < 6: # Ya sabemos que es >= 5
        clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
    elif magnitud_terremoto < 7: # Ya sabemos que es >= 6
        clasificacion = "Muy Fuerte (puede causar daños significativos)"
    else: # Si no entró en ninguna anterior, es >= 7
        clasificacion = "Extremo (puede causar graves daños a gran escala)"

    print(f"Clasificación: {clasificacion}")

except ValueError:
    print("Error: Por favor, ingrese un número válido para la magnitud.")


# --- Ejercicio 10 ---
print("\n--- Ejercicio 10 ---")

# Diccionario para mapear meses a números para facilitar la comparación
meses_a_numeros = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
mes_nombre = input("Ingrese el mes actual (ej. Enero, Febrero, etc.): ").lower()
try:
    dia = int(input("Ingrese el día del mes: "))

    # Validar entradas
    if hemisferio not in ['N', 'S']:
        print("Error: Hemisferio inválido. Use 'N' o 'S'.")
    elif mes_nombre not in meses_a_numeros:
        print(f"Error: Mes '{mes_nombre}' no reconocido.")
    elif not (1 <= dia <= 31): # Validación básica del día
         print("Error: Día inválido.")
    else:
        mes_num = meses_a_numeros[mes_nombre]
        estacion = ""

        # Lógica de estaciones basada en la tabla
        if (mes_num == 12 and dia >= 21) or (mes_num == 1) or (mes_num == 2) or (mes_num == 3 and dia <= 20):
            if hemisferio == 'N':
                estacion = "Invierno"
            else: # Hemisferio S
                estacion = "Verano"
        elif (mes_num == 3 and dia >= 21) or (mes_num == 4) or (mes_num == 5) or (mes_num == 6 and dia <= 20):
            if hemisferio == 'N':
                estacion = "Primavera"
            else: # Hemisferio S
                estacion = "Otoño"
        elif (mes_num == 6 and dia >= 21) or (mes_num == 7) or (mes_num == 8) or (mes_num == 9 and dia <= 20):
            if hemisferio == 'N':
                estacion = "Verano"
            else: # Hemisferio S
                estacion = "Invierno"
        elif (mes_num == 9 and dia >= 21) or (mes_num == 10) or (mes_num == 11) or (mes_num == 12 and dia <= 20):
            if hemisferio == 'N':
                estacion = "Otoño"
            else: # Hemisferio S
                estacion = "Primavera"
        else:
             # Este caso no debería ocurrir si las validaciones anteriores son correctas
             estacion = "Fecha inválida o fuera de rango."


        if estacion and "inválida" not in estacion:
             print(f"En el hemisferio {hemisferio}, el {dia} de {mes_nombre.capitalize()} es {estacion}.")
        elif estacion:
             print(estacion) # Imprime el mensaje de error si lo hubo

except ValueError:
    print("Error: Por favor, ingrese un número válido para el día.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

print("\n--- Fin del Trabajo Práctico ---")

