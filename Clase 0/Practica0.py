def pasarElObeliscoConbilletes():
    dia = 0
    obelisco = 67.5
    pila = 0.11
    while (pila <= obelisco):
        pila = pila * 2
        dia += 1
    return dia  

print(pasarElObeliscoConbilletes())
