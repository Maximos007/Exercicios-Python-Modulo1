import random
number = int(input('Digite um número : '))
x = random.randint(0, 5)
print('escolhido : {}'.format(x))
print('VENCEU' if x == number else 'perdeu')
