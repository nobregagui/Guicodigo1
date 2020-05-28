nome = input('Digite seu nome completo: ')
print('Analisando os dados...')
n1 = nome.split()
n2 = nome.__len__()
print('O seu primeiro nome é {} e tem {} letras'.format((n1[0]), len(n1[0])))
print('Seu nome inteiro em maiusculo é {}'.format(nome.upper()))
print('Seu nome completo em minusculo é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome.strip())))






