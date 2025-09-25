# Torres de Hanoi en Python (Recursivo)

Este proyecto implementa una solución recursiva al clásico problema de las **Torres de Hanoi**, con soporte para `N` discos, validaciones de entrada y visualización paso a paso de cada movimiento.

---

## Objetivo
Aplicar el concepto de **recursividad** en Python resolviendo el problema de las Torres de Hanoi para un número arbitrario de discos.  
El programa imprime en consola cada movimiento y muestra al final el número total de pasos realizados y el esperado.

---

## Requisitos Funcionales
- Aceptar un número de discos `N` (entero entre 1 y 20).  
- Imprimir todos los movimientos en orden, numerados desde `1` hasta `(2^N - 1)`.  
- Usar los nombres de torres `A`, `B` y `C` (origen, auxiliar y destino).  
- Mostrar un resumen final con el número total de movimientos.  

---

## Requisitos Técnicos
- **Algoritmo estrictamente recursivo**.  
- **Manejo de errores**:  
  - Validar que `N` sea un entero dentro del rango permitido.  
  - Mensajes claros en caso de entradas inválidas.  
- **Código legible** con comentarios y docstrings.  

---

## Estructura del Proyecto
```
/src/hanoi.py
README.md
```

---

## Ejecución
1. Descargar el archivo `hanoi.py` en tu equipo.  
2. Desde la terminal, ejecutar:  
   ```bash
   python src/hanoi.py
   ```
3. Ingresar el número de discos cuando el programa lo solicite:  
   ```
   --- Problema de las Torres de Hanoi (Recursivo) ---
   Ingresa el número de discos (entre 1 y 20): 3
   ```

---

## Ejemplo de salida (N = 3)
```
Paso 1: mover disco desde A hacia C
Paso 2: mover disco desde A hacia B
Paso 3: mover disco desde C hacia B
Paso 4: mover disco desde A hacia C
Paso 5: mover disco desde B hacia A
Paso 6: mover disco desde B hacia C
Paso 7: mover disco desde A hacia C

--- Resumen Final ---
Total de movimientos realizados: 7
Total de movimientos esperado (2^3 - 1): 7
```

---

## Pruebas sugeridas
Verificar la cantidad de movimientos para algunos valores de `N`:

| N  | Movimientos esperados (2^N - 1) |
|----|---------------------------------|
| 1  | 1                               |
| 2  | 3                               |
| 3  | 7                               |
| 4  | 15                              |

---

## Notas
- Rango permitido: `1 ≤ N ≤ 20`.  
- Para valores grandes de `N`, la cantidad de pasos crece exponencialmente y puede tardar en imprimir todos los movimientos.  
