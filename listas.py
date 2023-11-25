def estaEnRango(valor, minimo, maximo):
    return valor >= minimo and valor <= maximo

def estaEnLista(valor, lista):
    return valor in lista

num1 = 44
lista1 = [6,14,11,78,5]
max = 44
min = 22

resultado = estaEnRango(num1,min,max)
print(resultado)

