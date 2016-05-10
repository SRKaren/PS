#!/bin/bash

#Reconocimiento de comercial
python reco_dev.py #1&2>/dev/null

#Generacion de logs
date=`date +"%Y_%a_%b_%d_%H%M%P"`
cd ./logs
sed 's/[[:space:]]\+/,/' reporte.txt > registro.csv
cp registro.csv ./reportes/registro_$date.csv
