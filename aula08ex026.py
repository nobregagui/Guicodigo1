frase = str(input('Digite uma frase: ').strip().upper())
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')))
print('A letra A aparece pela ultima vez em {}'.format(frase.rfind('A')))
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))

