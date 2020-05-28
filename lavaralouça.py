from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
n5 = input('Quinto nome: ')
n6 = input('Sexto nome: ')
lista = [n1, n2, n3, n4, n5, n6]
shuffle(lista)
print('A ordem de quem vai lavar a louça será: ')
print(lista)
