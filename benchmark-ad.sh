#!/bin/bash

#################################################################################
#                                                                               #
# Nome: benchmark-lucas.sh                                                      #
#                                                                               #
# Autor: Lucas Mendes (lucas.mendes@ifce.edu.br)                                #
# Data: 26/02/2021                                                              #
#                                                                               #
# Descrição: Executa uma série de operações aritméticas com inteiro e ponto     #
#		flutuante a fim de analisar o desempenho da CPU da máquina. Além disso,     #
#   realiza testes de escrita e leitura no HD e na memória principal.           #
#   Ao final, exibe grṕaficos e relatórios de desempenho.                       #
#                                                                               #
# Uso: ./benchmark-lucas.sh [repeticoes] [nivel]                                #
#                                                                               #
#################################################################################

# Verifica e instala dependências, se necessário.
sudo ./resources/install-dependencies.sh

clear

NIVEL=0
RPT=0

if [[ $# -eq 0 ]]; then
  read -p "Informe o número de repetições dos testes: " RPT
  echo
  cat resources/config/info
  echo
  while [[ $NIVEL -ne 1 && $x -ne 2 && $x -ne 3 ]]; do
    read -p "Informe o nível da carga de trabalho para os testes: (1 - Baixo; 2 - Moderado; 3 - Alto) " NIVEL
  done
elif [[ $# -eq 1 ]]; then
  RPT=$1
  echo
  cat resources/config/info
  echo
  while [[ $NIVEL -ne 1 && $x -ne 2 && $x -ne 3 ]]; do
    read -p "Informe o nível da carga de trabalho para os testes: (1 - Baixo; 2 - Moderado; 3 - Alto) " NIVEL
  done
elif [[ $# -eq 2 ]]; then
  RPT=$1
  NIVEL=$2
else
  echo "São permitidos somente 2 parâmetros: número de repetições e nível dos testes (1 - Baixo, 2 - Moderado, 3 - Alto)! Tente novamente!"
  exit 1
fi

python3 resources/benchmark-cpu.py $RPT $NIVEL
./resources/benchmark-hd.sh $RPT $NIVEL
./resources/benchmark-mem.sh $RPT $NIVEL

clear

./resources/RelatorioMaquina.sh $RPT $NIVEL

echo
echo

python3 resources/resultado.py

rm -f teste.txt
rm -f resources/resultados/*.csv

exit 0
