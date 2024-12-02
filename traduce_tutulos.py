from deep_translator import GoogleTranslator

fil = open('./Resp_dic0224/fecha_rango_M10D02y24_titulos.txt', 'r')

datos = fil.readlines()

print(len(datos))

traductor = GoogleTranslator(source='en', target='es')
for ss in datos:
  ss = ss.replace('\n', '')
  i = ss.find('"')
  i = ss.find('"',i+1)
  i = ss.find('"',i+1)
  ss = ss[i+1:]
  ln = len(ss)
  ss = ss[:ln-2]
  print(ss)
  resultado = traductor.translate(ss)
  print(resultado)


