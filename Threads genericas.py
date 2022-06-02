import random as r
import threading as t
lista = [r.randint(1,100)for i in range(1000)]
#print(lista)

lista_aux = []

num = int(input("digite o número Threads "))
inicio = 0
fim = len(lista)//num - 1


partes = len(lista)//num
print(partes)
def sumList(lista,inicio,fim,lista_aux,partes):
    value = sum(lista[inicio:fim])
    #print(inicio)
    #print(fim)
    lista_aux.append(value)
    inicio = fim + 1
    fim = fim + partes
    return inicio,fim
lista_th = []
for i in range(num):
    th = t.Thread(target=sumList, args=(lista,inicio,fim,lista_aux,partes))
    th.start()
    inicio,fim = sumList(lista,inicio,fim,lista_aux,partes)


print(lista_aux, "\n")

