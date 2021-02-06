dias = float(input('Quantos dias o carro foi alugado ? '))
km = float(input('KM percorrido ?'))
print('Total a pagar R$ : {:.2f}'.format(dias*60 + km*0.15))