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