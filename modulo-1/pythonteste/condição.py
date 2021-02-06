n1 = float(input('Primeira nota :'))
n2 = float(input('Segunda nota :'))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
print('PARABÉNS' if m >=6.0 else 'ESTUDE MAIS !')
