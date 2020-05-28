import math
an = float(input('Digite o Ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O seno é {:.2f}\nO Cosseno é {:.2f}\nE a Tangente é {:.2f}'.format(sen, cos, tan))
