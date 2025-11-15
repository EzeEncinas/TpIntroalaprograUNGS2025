# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j

    # Si el algoritmo terminó
    if j >= n - 1:
        return {"done": True}

    a = i
    b = i +1

    # Comparar e intercambiar si corresponde
    swap = False
    if items[a] > items[b]:
        aux = items[a]
        items[a] = items[b]
        items[b] = aux
        swap = True 

    # Avanzar punteros
    i = i + 1
    if  i >= n - 1 - j: # Llego al final de la pasada
        i = 0 
        j = j + 1
    return {"a": a, "b": b, "swap": swap, "done": False}
