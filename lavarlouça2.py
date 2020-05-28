from random import choice
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('Quem vai lavar a louça domingão será: {}'.format(escolhido))

