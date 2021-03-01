#!/bin/bash

#################################################################################
#                                                                               #
# Nome: benchmark-hd.sh                                                 				#
#                                                                               #
# Autor: Lucas Mendes (lucas.mendes@ifce.edu.br)                                #
# Data: 26/02/2021                                                              #
#                                                                               #
# Descrição: Realiza um teste de desempenho no HD da máquina.  									#
#                                                                               #
# Uso: ./benchmark-hd.sh [repeticoes] [nivel]                                   #
#                                                                               #
#################################################################################

RPT=$1
NIVEL=$2

TAMANHO=0

if [[ $NIVEL -eq 1 ]]; then
	TAMANHO=25600
elif [[ $NIVEL -eq 2 ]]; then
	TAMANHO=51200
else
	TAMANHO=102400
fi

if [[ -e "resources/resultados/result-hd.csv" ]]; then
	rm resources/resultados/result-hd.csv
fi

touch resources/resultados/result-hd.csv

echo -e "repeticao,escrita,leitura" >> resources/resultados/result-hd.csv

echo
echo -n "Testando HD"

for i in $(seq $RPT); do
	dd bs=16K count=$TAMANHO oflag=direct if=/dev/zero of=arquivo_teste 2> teste.txt
	echo -n "."
	VALOR_E=$(cat teste.txt | grep copiados | cut -d " " -f10 | tr "," ".")
	dd bs=16K count=$TAMANHO  iflag=direct if=arquivo_teste of=/dev/null 2> teste.txt
	echo -n "."
	VALOR_L=$(cat teste.txt | grep copiados | cut -d " " -f10 | tr "," ".")
	echo -e "${i},${VALOR_E},${VALOR_L}" >> resources/resultados/result-hd.csv
	rm arquivo_teste
done

rm -f teste.txt

echo
echo
echo "Teste de HD concluído!"
echo

exit 0
