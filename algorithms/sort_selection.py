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

    if i >= n - 1:
        return {done: True}

    
    for i in range(0, len(lista)):
        min_idx = i
        for j in range (i+1, len(lista)): 
            if min_idx > lista[j]:
                min_idx =j
                
    aux = lista[j]
    lista[i] = lista[min_idx]
    lista[min_idx] = aux 
    
    return {"done": True}
