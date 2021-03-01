#!/bin/bash

#################################################################################
#                                                                               #
# Nome: benchmark-mem.sh                                                 				#
#                                                                               #
# Autor: Lucas Mendes (lucas.mendes@ifce.edu.br)                                #
# Data: 26/02/2021                                                              #
#                                                                               #
# Descrição: Realiza um teste de desempenho na memória principal da máquina.		#
#                                                                               #
# Uso: ./benchmark-mem.sh [repeticoes] [nivel] 		                              #
#                                                                               #
#################################################################################

RPT=$1
NIVEL=$2

TAMANHO=0

if [[ $NIVEL -eq 1 ]]; then
	TAMANHO=512
elif [[ $NIVEL -eq 2 ]]; then
	TAMANHO=1024
else
	TAMANHO=2048
fi

if [[ -e "resources/resultados/result-mem.csv" ]]; then
	rm resources/resultados/result-mem.csv
fi

if [[ -d "RAM_teste" ]]; then
	rm -r RAM_teste
fi

touch resources/resultados/result-mem.csv
mkdir RAM_teste
sudo mount tmpfs -t tmpfs RAM_teste/

echo -e "repeticao,escrita,leitura" >> resources/resultados/result-mem.csv

echo -n "Testando Memória Principal"

for i in $(seq $RPT); do
	dd if=/dev/zero of=RAM_teste/arquivo_tmp bs=1M count=$TAMANHO 2> teste.txt
	echo -n "."
	VALOR_E=$(cat teste.txt | grep copiados | cut -d " " -f10 | tr "," ".")
	dd if=RAM_teste/arquivo_tmp of=/dev/null bs=1M count=$TAMANHO 2> teste.txt
	echo -n "."
	VALOR_L=$(cat teste.txt | grep copiados | cut -d " " -f10 | tr "," ".")
	echo -e "${i},${VALOR_E},${VALOR_L}" >> resources/resultados/result-mem.csv
done

sudo umount RAM_teste
rm -r RAM_teste

echo
echo
echo "Teste de Memória Principal concluído!"
echo

exit 0
