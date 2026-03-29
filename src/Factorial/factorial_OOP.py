import sys

class Factorial:
    def __init__(self):
        """Constructor de la clase"""
        pass

    def _calcular_individual(self, num):
        "Método para calcular el factorial de un solo número"
        if num < 0: return 0
        elif num == 0: return 1
        else: 
            fact = 1
            while(num > 1): 
                fact *= num 
                num -= 1
            return fact 

    def run(self, min_val, max_val):
        "Calcula y muestra el factorial entre los números min y max"
        if min_val > max_val:
            print(f"Error: El inicio ({min_val}) no puede ser mayor al fin ({max_val}).")
            return

        print(f"\nProcesando rango: {min_val} a {max_val}")
        for i in range(min_val, max_val + 1):
            resultado = self._calcular_individual(i)
            print(f"  {i}! = {resultado}")

def parsear_rango(rango_str):
    try:
        partes = rango_str.split('-')
        if partes[0] == "" and partes[1] != "":
            return 1, int(partes[1])
        elif partes[0] != "" and partes[1] == "":
            return int(partes[0]), 60
        elif partes[0] != "" and partes[1] != "":
            return int(partes[0]), int(partes[1])
    except (ValueError, IndexError):
        return None, None
    return None, None


if __name__ == "__main__":
    # Obtener entrada
    if len(sys.argv) > 1:
        rango_input = sys.argv[1]
    else:
        rango_input = input("Ingrese el rango (ej. 1-10): ")

    # Procesar entrada
    inicio, fin = parsear_rango(rango_input)

    if inicio is not None:
        # Instanciar la clase y ejecutar
        calculadora = Factorial()
        calculadora.run(inicio, fin)
    else:
        print("Error: Formato de rango no válido.")