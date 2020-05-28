import emoji
e1 = emoji.emojize(':kissing_smiling_eyes:', use_aliases= True)
e2 = emoji.emojize(':tired_face:', use_aliases= True)
print('\033[7;31;40m=-=-=-=-=-=--=-=-=-=-==-ANALISANDO TRIÂNGULOS=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m')
print('\033[31mBoa Noite Diogo!!\033[m')
t1 = float(input('\033[35mDigite a medida do PRIMEIRO triângulo: '))
t2 = float(input('\033[33mDigite a medida do SEGUNDO triângulo: '))
t3 = float(input('\033[34mDigite a medida do TERCEIRO triângulo: \033[m'))
if t1< t2 + t3 and t2< t3 + t1 and t3< t1 + t2:
    print('Pode formar um triângulo: ')
    if t1 == t2 == t3:
        print('\033[4;36;40mEQUILÁTERO\033[m')
    elif t1 != t2 != t3 != t1:
        print('\033[4;31;40mESCALENO\033[m')
    else:
        print('\033[4;34;40mISÓSCELES\033[m')

else:
    print('Não pode ser um triângulo')
print('\033[4;31;40m=-=-=-=--=-=-=--=-=-=-=-AVALIAÇÃO=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m')
per = str(input('E ai diogueira, curtiu? ')).lower().strip()
if per == 'Curti'.lower() or per == 'Sim'.lower() or per == 'Boa'.lower() or per == 'Muito bom'.lower() or per == 'Legal mano'.lower():
    print('\033[34mFico feliz que tenha gostado!!! {}\033[m'.format(e1))
else:
    print('\033[33mPô desculpa mano, eu melhor da próxima!!!{}\033[m '.format(e2))
print('\033[7;30;41m=-=-=-=-=-=-==-=-=-=-FIM=-=-=-=-=-=-=-=-=-=-=\033[m')
