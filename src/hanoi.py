contador_pasos = 0

def hanoi(n_discos: int, origen: str, destino: str, auxiliar: str):
    # Declaramos que vamos a modificar la variable global
    global contador_pasos
    
    # 1. CASO BASE: Mover solo 1 disco
    if n_discos == 1:
        contador_pasos += 1
        print(f"Paso {contador_pasos}: mover disco desde {origen} hacia {destino}")
        return
    
    # Si N > 1, aplicamos la estrategia de 3 pasos:
    
    # Paso 1: Mover N-1 discos de Origen a Auxiliar
    hanoi(n_discos - 1, origen, auxiliar, destino)
    
    # Paso 2: Mover el disco N (el más grande) de Origen a Destino
    contador_pasos += 1
    print(f"Paso {contador_pasos}: mover disco desde {origen} hacia {destino}")
    
    # Paso 3: Mover N-1 discos de Auxiliar a Destino
    hanoi(n_discos - 1, auxiliar, destino, origen)
def main():
    """
    Función principal para manejar la entrada, validación de errores y ejecución.
    """
    MIN_DISCOS = 1
    MAX_DISCOS = 20 # Rango razonable
    
    print("--- Problema de las Torres de Hanoi (Recursivo) ---")
    
    try:
        # Petición de entrada
        n_input = input(f"Ingresa el número de discos (entre {MIN_DISCOS} y {MAX_DISCOS}): ")
        
        # 1. Intentar la conversión a entero (puede lanzar ValueError)
        n_discos = int(n_input)
        
        # 2. Validar que el entero esté dentro del rango permitido
        if not (MIN_DISCOS <= n_discos <= MAX_DISCOS):
            print(f"\nError: El número de discos debe ser un entero entre {MIN_DISCOS} y {MAX_DISCOS}.")
            return
        
    except ValueError:
        # Captura si la conversión a int falla (si el usuario ingresó texto o un flotante)
        print("\nError: Tipo de entrada inválido. Por favor, ingresa un número entero positivo.")
        return
    
    # Reiniciar el contador global antes de empezar
    global contador_pasos
    contador_pasos = 0

    # Ejecutar el algoritmo. Usamos las torres estándar: A (Origen), C (Destino), B (Auxiliar)
    # n_discos debe ser > 0 aquí
    hanoi(n_discos, 'A', 'C', 'B')
    
    # Calcular y mostrar el resumen final
    total_esperado = (2 ** n_discos) - 1
    
    print("\n--- Resumen Final ---")
    print(f"Total de movimientos realizados: {contador_pasos}")
    print(f"Total de movimientos esperado (2^{n_discos} - 1): {total_esperado}")

if __name__ == "__main__":
    main()