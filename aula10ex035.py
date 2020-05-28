print('-='*20)
print('ANALISANDO TRIÂNGULOS')
print('-='*20)
r1 = float(input('Segmento do primeiro triângulo: '))
r2 = float(input('Segmento do segundo triãngulo: '))
r3 = float(input('Segmento do segundo triângulo: '))
if r1< r2 + r3 and r2< r3 + r1 and r3< r1 + r2:
    print('PODE formar um triângulo')
else:
    print('Não pode formar um triângulo')
