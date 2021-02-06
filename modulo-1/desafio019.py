from random import choice
name1 = str(input('Primeiro aluno : '))
name2 = str(input('Segundo aluno : '))
name3 = str(input('Terceiro aluno :'))
name4 = str(input('Quarto aluno :'))

list = [name1, name2, name3, name4]
prizeDraw = choice(list)

print('O aluno escolhido foi : {}'.format(prizeDraw))
