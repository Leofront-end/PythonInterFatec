convidados_noivo = set()
convidados_noiva = set()
 
convite = input()
 
while convite != 'ACABOU':
    convidado, convidou = convite.split(';')
    if convidou == 'noivo':
        convidados_noivo.add(convidado)
    else:
        convidados_noiva.add(convidado)
    convite = input()
 
print('-' * 20)
print('LISTA FINAL')
print('-' * 20)
convidados = list(convidados_noivo | convidados_noiva)
convidados.sort()
for convidado in convidados:
    print(convidado)
print('*')
 
print('-' * 20)
print('APENAS NOIVA')
print('-' * 20)
convidados = list(convidados_noiva - convidados_noivo)
convidados.sort()
for convidado in convidados:
    print(convidado)
print('*')
 
print('-' * 20)
print('APENAS NOIVO')
print('-' * 20)
convidados = list(convidados_noivo - convidados_noiva)
convidados.sort()
for convidado in convidados:
    print(convidado)
print('*')
 
print('-' * 20)
print('POR AMBOS')
print('-' * 20)
convidados = list(convidados_noivo & convidados_noiva)
convidados.sort()
for convidado in convidados:
    print(convidado)
print('*')
 
print('-' * 20)
print('POR APENAS UM DELES')
print('-' * 20)
convidados = list(convidados_noivo ^ convidados_noiva)
convidados.sort()
for convidado in convidados:
    print(convidado)