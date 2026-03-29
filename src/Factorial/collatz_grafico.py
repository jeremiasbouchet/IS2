#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* src/collatz_grafico.py                                                 *
#* Calcula iteraciones de la conjetura de Collatz y grafica los resultados*
#* Rango: 1 a 10,000                                                      *
#*-------------------------------------------------------------------------*

import matplotlib.pyplot as plt

def calcular_iteraciones_collatz(n):
    """
    Aplica las reglas de la conjetura de Collatz a un número n 
    y devuelve el número de iteraciones necesarias para llegar a 1.
    
    Reglas:
    - Si n es par: n = n / 2
    - Si n es impar: n = 3n + 1
    """
    if n <= 0:
        return 0 # La conjetura es solo para enteros positivos
        
    contador = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2 # Division entera
        else:
            n = 3 * n + 1
        contador += 1
    return contador

def generar_grafico(numeros_inicio, iteraciones):
    """
    Genera un gráfico de dispersión usando Matplotlib.
    Eje X (Abscisas): Número de iteraciones
    Eje Y (Ordenadas): Número de inicio (n)
    """
    print("Generando gráfico...")
    
    # Crear la figura y los ejes
    # Usamos scatter (dispersión) porque son puntos individuales
    plt.figure(figsize=(12, 8)) # Tamaño de la ventana del gráfico
    plt.scatter(iteraciones, numeros_inicio, s=1, alpha=0.5, color='blue') # s=tamaño punto, alpha=transparencia
    
    # Configurar títulos y etiquetas según la solicitud
    plt.title("Conjetura de Collatz (Rango 1 - 10,000)")
    plt.ylabel("Número de comienzo 'n' (Ordenadas)")
    plt.xlabel("Número de iteraciones para converger a 1 (Abscisas)")
    
    # Añadir cuadrícula para facilitar la lectura
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    print("Mostrando gráfico en pantalla.")
    # Mostrar el gráfico
    plt.show()

# --- Bloque Principal ---
if __name__ == "__main__":
    limite_superior = 10000
    
    # Listas para almacenar los datos
    numeros_inicio = list(range(1, limite_superior + 1))
    iteraciones = []
    
    print(f"Calculando iteraciones de Collatz para números del 1 al {limite_superior}...")
    
    # Calcular las iteraciones para cada número
    for n in numeros_inicio:
        iters = calcular_iteraciones_collatz(n)
        iteraciones.append(iters)
    
    print("Cálculos finalizados.")
    
    # Llamar a la función para graficar
    generar_grafico(numeros_inicio, iteraciones)