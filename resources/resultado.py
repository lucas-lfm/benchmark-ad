#!/usr/bin/python3
# -*- coding: UTF-8 -*-
# Libraries to import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# exibindo resultados do teste de CPU
df_resultados_cpu = pd.read_csv("resources/resultados/result-cpu.csv")

repeticoes = np.array(df_resultados_cpu["repeticao"])
valores = np.array(df_resultados_cpu["tempo"])
media = valores.mean()
medias = []

for i in range(repeticoes.max()):
    medias.append(media)

plt.figure(1, figsize=(12,6))
plt.subplot(2,2,1)
plt.title('Desempenho da CPU')
plt.xlabel('Repetição')
plt.ylabel('Tempo (s)')
plt.ylim(0,valores.max()*2)
plt.plot(repeticoes, valores, color='blue')
plt.plot(repeticoes, medias, 'b--', color='blue')
plt.plot(repeticoes, valores, 'o')
plt.legend(['Tempo gasto (s)', 'Média (s)'], loc=0)

# exibindo resultados do teste de HD
df_resultados_hd = pd.read_csv("resources/resultados/result-hd.csv")

repeticoes = np.array(df_resultados_hd["repeticao"])
escritas = np.array(df_resultados_hd["escrita"])
leituras = np.array(df_resultados_hd["leitura"])
media_e = escritas.mean()
media_l = leituras.mean()
medias_e = []
medias_l = []

for i in range(repeticoes.max()):
    medias_e.append(media_e)
    medias_l.append(media_l)

plt.subplot(2,2,2)
plt.title('Desempenho do HD')
plt.xlabel('Repetição')
plt.ylabel('Taxa de E/S (MB/s)')
plt.ylim(0,leituras.max()*2)
plt.plot(repeticoes, escritas, color='red')
plt.plot(repeticoes, leituras, color='blue')
plt.plot(repeticoes, medias_e, 'b--', color='red')
plt.plot(repeticoes, medias_l, 'b--', color='blue')
plt.plot(repeticoes, escritas, 'o', repeticoes, leituras, 'o')
plt.legend(['Taxa de Escrita', 'Taxa de Leitura'], loc=0)

# exibindo resultados do teste de Memória Principal
df_resultados_mem = pd.read_csv("resources/resultados/result-mem.csv")

repeticoes = np.array(df_resultados_mem["repeticao"])
escritas = np.array(df_resultados_mem["escrita"])
leituras = np.array(df_resultados_mem["leitura"])
media_e = escritas.mean()
media_l = leituras.mean()
medias_e = []
medias_l = []

for i in range(repeticoes.max()):
    medias_e.append(media_e)
    medias_l.append(media_l)

plt.subplot(2,2,3)
plt.title('Desempenho da Memória Principal')
plt.xlabel('Repetição')
plt.ylabel('Velocidade (GB/s)')
plt.ylim(0,leituras.max()*2)
plt.plot(repeticoes, escritas, color='red')
plt.plot(repeticoes, leituras, color='blue')
plt.plot(repeticoes, medias_e, 'b--', color='red')
plt.plot(repeticoes, medias_l, 'b--', color='blue')
plt.plot(repeticoes, escritas, 'o', repeticoes, leituras, 'o')
plt.legend(['Taxa de Escrita', 'Taxa de Leitura'], loc=0)

plt.tight_layout()
plt.show()
