n1 = int(input('Digite um número, sem usar pontos e virgulas!!  '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
dm = n1 // 10000 % 10
cm = n1 // 100000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
print('Dezena de milhar: {}'.format(dm))
print('Centena de milhar: {}'.format(cm))

