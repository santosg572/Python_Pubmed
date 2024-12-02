#!/bin/bash

mes=10

dia=02

filo="fecha_rango_M"${mes}"D"${dia}
echo $filo

python fecha_rango.py $mes $dia > ${filo}".txt"

filt=${filo}"_titulos" 
cat ${filo}".txt" | grep \"title\": > ${filt}".txt" 




