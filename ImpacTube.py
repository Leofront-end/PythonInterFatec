N = int(input(''))
cadastro = []
for i in range(0,N):
    nome,inscritos,monetizacao,premium = input("").split(';')
    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    cadastro.append([nome,inscritos,monetizacao,premium])

X = float(input(''))
Y = float(input(''))
print('-----')
print('BÔNUS')
print('-----')
for nome,inscritos,monetizacao,premium in cadastro:
    valorMais = 0
    if (premium == 'sim'):
        valorMais = (inscritos//1000) * X + monetizacao
    else:
        valorMais = (inscritos//1000) * Y + monetizacao
    print(f'{nome}: R$ {valorMais:.2f}')

    
