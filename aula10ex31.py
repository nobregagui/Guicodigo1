n1 = float(input('Quantos Km tem a sua viagem? '))
if n1 <=200:
    print('Sua viagem ira custar R${}'.format(n1*0.50))
else:
    print('Sua viagem custará R${}'.format(n1*0.45))