# coding: "utf-8"

__Author__ = "Bruno Sevalho Wesen"

from copy import copy
import numpy
import random

competidores = ["Emmerson", "Josué", "Maria", "Albert", "Ribamar", "Alessandro"]


def x():
    lista = []

    for i in competidores:
        tempo = float("%.2f" % (random.random() * 1000))
        listax = [i, tempo]
        lista.append(listax)

    return numpy.array(
        [lista[0], lista[1], lista[2], lista[3],
         lista[4], lista[5]])


matriz_corrida = {"volta1": x(), "volta2": x(), "volta3": x(), "volta4": x(),
                  "volta5": x(), "volta6": x(), "volta7": x(),
                  "volta8": x(), "volta9": x(), "volta10": x()}

j = []
x = 0
vazio = []
# print(list(matriz_corrida.keys())[1])
i = 0
volta = []

# Tempo total dos competidores
c1 = 0.0
c2 = 0.0
c3 = 0.0
c4 = 0.0
c5 = 0.0
c6 = 0.0

while x < 10:
    k = len(matriz_corrida["volta1"])

    while k > 0:  # Retorna todos os elementos de uma coluna de uma matriz
        j.append(matriz_corrida[list(matriz_corrida.keys())[i]][k - 1][1])  # O tempo de todos os competidores
        k -= 1

    media = numpy.array(list(map(float, j)))
    volta.append(media.mean())
    j.reverse()
    m = copy(j)  # O tempo de todos os competidores em ordem correta
    j.sort()
    vazio.append(matriz_corrida[(list(matriz_corrida.keys())[i])][m.index(j[0])])

    c1 += float(m[0])
    c2 += float(m[1])
    c3 += float(m[2])
    c4 += float(m[3])
    c5 += float(m[4])
    c6 += float(m[5])
    i += 1
    x += 1
    j = []

k = len(vazio)

while k > 0:  # Retorna todos os elementos de uma coluna de uma matriz
    j.append(vazio[k - 1][1])
    k -= 1

j.reverse()
m = copy(j)
j.sort()

# print(ç)
# print(m.index(j[0]))
# print(ç[m.index(j[0])])

print("O(A) %s foi quem fez a melhor volta no tempo de %.2f segundos na volta %i" % (vazio[m.index(j[0])][0],
                                                                                     float(vazio[m.index(j[0])][1]),
                                                                                     m.index(j[0]) + 1))
classificacao = [c1, c2, c3, c4, c5, c6]
cl = copy(classificacao)
classificacao.sort()

print("\nPrimeiro lugar:", competidores[cl.index(classificacao[0])],
      "\nSegundo lugar:", competidores[cl.index(classificacao[1])],
      "\nTerceiro lugar:", competidores[cl.index(classificacao[2])],
      "\nQuarto lugar:", competidores[cl.index(classificacao[3])],
      "\nQuinto lugar:", competidores[cl.index(classificacao[4])],
      "\nÚltimo lugar:", competidores[cl.index(classificacao[5])])

voltar = copy(volta)
volta.sort()

print("\nA volta com a média mais rápida foi a volta %i com a média de %.2f segundos" % (
    voltar.index(volta[0]) + 1, volta[0]))
# j[0]  # Menor tempo
# print(matriz_corrida["volta1"][m.index(j[0])][0])  # Retorna a pessoa com o menor tempo na volta
