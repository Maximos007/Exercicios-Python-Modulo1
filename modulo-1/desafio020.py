from random import shuffle
name1 =  str(input('Primeiro nome : '))
name2 = str(input('Segundo nome: '))
name3 = str(input('Terceiro nome: '))
name4 = str(input('Quarto name : '))

list =[name1, name2, name3, name4]
shuffle(list)

print('A ordem de apresentação é : {}'.format(list))