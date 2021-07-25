# coding: "utf-8"

__Author__ = "Bruno Sevalho Wesen"

import numpy

matrizExC = numpy.array([[26, 160], [25, 163], [7, 47]])

print(matrizExC)


def calcula_as_medias(lista):
    i = 2
    media = []
    colunas = []
    linhas = []

    while i >= 0:
        j = []

        for m in lista[i]:  # Retorna todos elementos de uma linha de uma matriz
            j.append(m)

        linhas.append(j)
        j = numpy.array(j)
        media.append(j.mean())
        i -= 1

    linhas = numpy.array(linhas)

    print("\nA media da linha 1: %i"
          "\nA media da linha 2: %i"
          "\nA media da linha 3: %i"
          "\nDesvio padrão da linha 1: %i"
          "\nDesvio padrão da linha 2: %i"
          "\nDesvio padrão da linha 3: %i" % (media[0], media[1], media[2], linhas[0].std(),
                                              linhas[1].std(), linhas[2].std()))

    i = 2
    media = []

    while i > 0:
        j = []
        k = len(lista)

        while k > 0:  # Retorna todos os elementos de uma coluna de uma matriz
            j.append(lista[k - 1][i - 1])
            k -= 1

        colunas.append(j)
        j = numpy.array(j)
        media.append(j.mean())
        i -= 1

    colunas = numpy.array(colunas)

    print("\nA media da coluna 1: %.2f"
          "\nA media da coluna 2: %.2f"
          "\nDesvio padrão da coluna 1: %.2f"
          "\nDesvio padrão da coluna 2: %.2f" % (media[0], media[1], colunas[0].std(), colunas[1].std()))

    # print(colunas, linhas)


calcula_as_medias(matrizExC)
