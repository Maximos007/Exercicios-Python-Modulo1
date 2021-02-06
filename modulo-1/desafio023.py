number = int(input('Digite um número : '))
numberU = number // 1 % 10
numberD = number // 10 % 10
numberC = number // 100 % 10
numberM = number // 1000 % 10
print('Unidade : {}'.format(numberU))
print('Dezena : {}'.format(numberD))
print('Centena : {}'.format(numberC))
print('MIlhar : {}'.format(numberM))
