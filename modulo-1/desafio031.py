distance = int(input('Distância da viagem em KM :'))
print('Preço da passagem {}').format(distance)
if distance <= 200:
  print('VALOR DA PASSAGEM {}').format(distance*0.50)