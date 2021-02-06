varName = str(input('Digite seu nome completo: ')).upper().strip()
name = varName.split()

print('Primeiro nome {}'.format(name[0]))
print('Último nome {}'.format(name[len(name)-1]))
