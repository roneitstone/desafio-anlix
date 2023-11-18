from datetime import datetime, timezone, timedelta
data_hora_formatada =[]
# Converter para uma string formatada
x = "2022/03/22 22:22:33"
y = x.split(" ")
x = y[0].split("/")
for i in x:
  data_hora_formatada.append(i)
  x= y[1].split(":")
for i in x:
  data_hora_formatada.append(i)
  print(data_hora_formatada)