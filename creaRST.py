file = 'parkinson_title'

fil = open(file+'.txt', 'r')

datos = fil.readlines()
fil.close()

filo = open(file+'.rst', 'w')

filo.write('parkinson\n')
filo.write('=========\n')
filo.write('\n')

k = 1
for ss in datos:
  ss = ss.replace('\n', '')
  i = ss.find('"')
  i = ss.find('"', i+1)
  i = ss.find('"', i+1)
  ss = ss[i:]
  ss2 = str(k)+'. '+ss+ '\n' 
  print(ss2)
  k = k+1
  filo.write(ss2)

filo.close()

