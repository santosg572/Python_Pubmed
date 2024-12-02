import subprocess

fil = open('fecha_rango_M10D02_titulos.txt', 'r')

datos = fil.readlines()

print(len(datos))

for ss in datos:
  ss = ss.replace('\n', '')
  i = ss.find('"')
  i = ss.find('"',i+1)
  i = ss.find('"',i+1)
  ss = ss[i+1:]
  ln = len(ss)
  ss = ss[:ln-2]
  print(ss)
  dd = subprocess.run(["/path/to/your/shell/script", 
                "arguments"], shell=True)  



