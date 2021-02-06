phrase = str(input('Digite um frase : ')).upper().strip()
print('A letra "A" aparece {}'.format(phrase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(phrase.find('A')+1))
print('A útima letra A apareceu na posição {}'.format(phrase.rfind('A')+1))
