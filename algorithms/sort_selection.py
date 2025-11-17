# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase

    # Si terminamos 
    if i >= n - 1:
        return {"done": True} 
        
    # Fase "buscar" (el minimo)
    if fase == "buscar":        
        if j < n:           # Mientras j este dentro de la lista, seguimos comparando
            a = min_idx     # indice del minimo actual
            b = j           # indice que estamos comparando ahora
            
            # Comparacion 
            if items[j]<items[min_idx]:
                min_idx = j     # Nuevo minimo encontrado
            j = j + 1           #Avanzar a la siguiente vuelta
            
            return { "a": a, "b": b, "swap": False, "done": False}
            
        # Si terminamos de desplazarlos, pasamos a la fase swap
        fase = "swap"
        
    # Fase de hacer el swap
    if fase == "swap":
        a = i
        b = min_idx

        hubo_swap = False

        if min_idx != i:
            # Hacemos el swap en items
            aux = items[i]
            items[i] = items[min_idx]
            items[min_idx] = aux
            hubo_swap = True

        # Avanzar a la proxima pasada
        i = i + 1
        j = i + 1 
        min_idx = i 
        fase = "buscar"

        return {"a": a, "b": b, "swap": hubo_swap, "done": False}
