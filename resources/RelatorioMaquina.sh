#!/bin/bash

#################################################################################
#                                                                               #
# Nome: RelarotioMaquina.sh                                                     #
#                                                                               #
# Autor: Lucas Mendes (lucas.mendes@ifce.edu.br)                                #
# Data: 05/02/2021                                                              #
#                                                                               #
# Descrição: Exibe um relatório com algumas informações da máquina              #
#                                                                               #
# Uso: ./RelatorioMaquina.sh                                                    #
#                                                                               #
#################################################################################

KERNEL=$(uname -r)
HOSTNAME=$(hostname)
CPUNO=$(cat /proc/cpuinfo | grep "model name" | wc -l)
CPUMODEL=$(cat /proc/cpuinfo | grep "model name" | head -n1 | cut -c14-)
MEMTOTAL=$(expr $(cat /proc/meminfo | grep MemTotal | tr -d ' ' | cut -d: -f2 | tr -d kB) / 1024) # em MB
FILESYS=$(df -h | egrep -v '(tmpfs|udev)')
UPTIME=$(uptime -s)

clear
echo "======================================================================"
echo "Relatório da Máquina: $HOSTNAME"
echo "Data/Hora: $(date)"
echo "Quantidade de Repetições do Teste: $1"
echo "Nível da Carga de Trabalho do Teste: $2"
echo "======================================================================"
echo
echo "Máquina ativa desde: $UPTIME"
echo
echo "Versão do Kernel: $KERNEL"
echo
echo "CPUs:"
echo "Quantidade de CPUs/Core: $CPUNO"
echo "Modelo da CPU: $CPUMODEL"
echo
echo "Memória Total: $MEMTOTAL MB"
echo
echo "Partições:"
echo "$FILESYS"
echo
echo "======================================================================="

exit 0
