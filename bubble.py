import matplotlib as mpl
from random import randint
import timeit


mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x,y, nome, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('nome.png')
OP=[]
def bubble_sort(lista):
  elementos = len(lista)-1
  ordenado = False
  aux=0
  while not ordenado:
    ordenado = True
    for i in range(elementos):
      if lista[i] > lista[i+1]:
           lista[i], lista[i+1] = lista[i+1],lista[i]
           ordenado = False  
           aux+=1;  
  OP.append(aux)             
  return lista

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

tempo=[]
list=[10000,20000,50000,100000]
for i in list:

  lista=geraLista(i)
   
  tempo.append(timeit.timeit("bubble_sort({})".format(lista),setup="from __main__ import bubble_sort",number=1))
  print(i)

desenhaGrafico(list,tempo,'bolha_tempo')
desenhaGrafico(list,OP,'bolha_operação')
