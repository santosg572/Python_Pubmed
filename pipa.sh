#!/bin/bash

#palabra="parkinson"
#file1="parkinson"

#palabra="Lotka-Volterra"
#file1="Lotka_Volterra"

#palabra="machine-learning" 
#file1="machine_learning"

palabra="dynamic-simulation" 
file1="dynamic_simulation"

python buscar.py "${palabra}" "${file1}" 

python resumen.py "${file1}"







