money = float(input('Carteira R$ : '))
cotaçao = float(input('Cotação do dolar US$: '))
total = money / cotaçao
print('R$ {} pode compra US$ {}'.format(money, total))
