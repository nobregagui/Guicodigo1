d = int(input('Quantos dias o carro foi usado?'))
k = float(input('Quantos Km ele andou?'))
print('Como o carro correu {}Km com {} dias de uso, o preço de seu aluguel sera R${}'.format(k, d, (d * 60) + (k * 0.15)))


