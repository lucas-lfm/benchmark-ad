#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from __future__ import print_function

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from time import time

repeticoes = int(sys.argv[1])
nivel = int(sys.argv[2])

size = 0

if(nivel == 1):
    size = 512
elif(nivel == 2):
    size = 1024
else:
    size = 2048

lista_repeticoes = []
lista_valores = []
tempo_repeticao = 0;

print()
print("Testando CPU, por favor aguarde um momento!")

# Definindo uma seed para o gerador de números pseudo aleatórios (para reprodutibilidade)
for j in range(repeticoes):

    lista_repeticoes.append(j+1)
    np.random.seed(0)

    A, B = np.random.random((size, size)), np.random.random((size, size))
    C, D = np.random.random((size * 128,)), np.random.random((size * 128,))
    E = np.random.random((int(size / 2), int(size / 4)))
    F = np.random.random((int(size / 2), int(size / 2)))
    F = np.dot(F, F.T)
    G = np.random.random((int(size / 2), int(size / 2)))

    t = time()

    # Multiplicação de Matriz
    N = 20
    #t = time()
    for i in range(N):
        np.dot(A, B)

    del A, B

    # Multiplicação de vetores
    N = 5000

    for i in range(N):
        np.dot(C, D)

    del C, D

    # Singular Value Decomposition (SVD)
    N = 3

    for i in range(N):
        np.linalg.svd(E, full_matrices = False)

    del E

    # Cholesky Decomposition

    for i in range(N):
        np.linalg.cholesky(F)

    # Eigendecomposition

    for i in range(N):
        np.linalg.eig(G)

    tempo_repeticao = time() - t
    lista_valores.append(tempo_repeticao)
    tempo_repeticao = 0;

resultados = {
    "repeticao": [],
    "tempo": []
}

resultados["repeticao"] = lista_repeticoes
resultados["tempo"] = lista_valores

print()
df_resultados = pd.DataFrame(resultados)

df_resultados.to_csv('resources/resultados/result-cpu.csv', index=False)
print("Teste de CPU concluído!")
