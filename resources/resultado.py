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


# Relatório Final
media_cpu = df_resultados_cpu["tempo"].mean()
var_cpu = df_resultados_cpu["tempo"].var()
std_cpu = df_resultados_cpu["tempo"].std()

media_mem_e = df_resultados_mem["escrita"].mean()
media_mem_l = df_resultados_mem["leitura"].mean()
var_mem_e = df_resultados_mem["escrita"].var()
var_mem_l = df_resultados_mem["leitura"].var()
std_mem_e = df_resultados_mem["escrita"].std()
std_mem_l = df_resultados_mem["leitura"].std()

media_hd_e = df_resultados_hd["escrita"].mean()
media_hd_l = df_resultados_hd["leitura"].mean()
var_hd_e = df_resultados_hd["escrita"].var()
var_hd_l = df_resultados_hd["leitura"].var()
std_hd_e = df_resultados_hd["escrita"].std()
std_hd_l = df_resultados_hd["leitura"].std()


print("=======================================================================")
print("                         Relatório de Teste                            ")
print("=======================================================================")
print()
print("Resultados do Desempenho da CPU:")
print()
print("     - Média de tempo gasto no processamento: {0:4.2f}s".format(media_cpu))
print("     - Variância: {0:4.2f}".format(var_cpu))
print("     - Desvio Padrão: {0:4.2f}".format(std_cpu))
print()
print("Resultados do Desempenho do HD:")
print()
print("     - Média de Taxa de Escrita: {0:4.1f} MB/s".format(media_hd_e))
print("     - Média de Taxa de Leitura: {0:4.1f} MB/s".format(media_hd_l))
print("     - Variância - Taxa de Escrita: {0:4.1f}".format(var_hd_e))
print("     - Variância - Taxa de Leirura: {0:4.1f}".format(var_hd_l))
print("     - Desvio Padrão - Taxa de Escrita: {0:4.1f}".format(std_hd_e))
print("     - Desvio Padrão - Taxa de Leitura: {0:4.1f}".format(std_hd_l))
print()
print("Resultados do Desempenho da Memória Principal:")
print()
print("     - Média de Taxa de Escrita: {0:4.1f} GB/s".format(media_mem_e))
print("     - Média de Taxa de Leitura: {0:4.1f} GB/s".format(media_mem_l))
print("     - Variância - Taxa de Escrita: {0:4.1f}".format(var_mem_e))
print("     - Variância - Taxa de Leirura: {0:4.1f}".format(var_mem_l))
print("     - Desvio Padrão - Taxa de Escrita: {0:4.1f}".format(std_mem_e))
print("     - Desvio Padrão - Taxa de Leitura: {0:4.1f}".format(std_mem_l))
print()
