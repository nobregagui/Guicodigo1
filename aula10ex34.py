s = float(input('Digite o seu salário: '))
if s > 1250:
    print('Parabéns você recebeu um aumento de 10%, seu salário agora é R$: {}'.format((s*0.10)+s))
else:
    print('Parabéns, vocÊ ganhou um salário de 15%, seu salário agora é R$: {}'.format((s*0.15)+s))

