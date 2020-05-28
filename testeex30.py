print('\033[33;46m -=-=-==-=-=-=-=-=-=-=-=-==-=Analisando-=-=-=-=-=-==-=-=-=-=-=-=-=-\033[m')

import emoji
e1 = emoji.emojize('Fico Feliz que tenha gostado!! :simple_smile:', use_aliases=True)
e2 = emoji.emojize('Me desculpa, prometo melhorar!! :tired_face:', use_aliases=True)
e3 = emoji.emojize('Volte sempre que quiser!! :kissing_smiling_eyes:', use_aliases=True)
n = emoji.emojize('Eae caralho :sob:', use_aliases=True)
num = int(input('Digite um número de 0 a 50: '))
if num %5==0:
    print('Este número faz parte da tabuada de 50!!')
else:
    print('Este número não faz parte da tabuada de 50')
per = str(input('Gostou?? ')).lower().strip().split()
if per == 'Sim' or per == 'Gostei' or per == 'Aham'.lower():
    print(e1)
else:
    print('\033[34;42m\033[m', e2)
print(e3)
print(n)



