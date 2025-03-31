noivo = set()
noiva = set()
while True:
    nome = input()
    if (nome == 'ACABOU'):
        break
    x,y = nome.split(';')
    if (y == 'noivo'):
        noivo.add(x)
    else:
        noiva.add(x)

lista = noivo | noiva
Anoiva = noiva - noivo
Anoivo = noivo - noiva
ambos = noiva & noivo
umDeles = noiva ^ noivo

print("-"*20)
print("LISTA FINAL")
print("-"*20)
for nome in lista:
    print(nome)
print("*")

print("-"*20)
print("APENAS NOIVA")
print("-"*20)
for nome in Anoiva:
    print(nome)
print("*")

print("-"*20)
print("APENAS NOIVO")
print("-"*20)
for nome in Anoivo:
    print(nome)
print("*")

print("-"*20)
print("POR AMBOS")
print("-"*20)
for nome in ambos:
    print(nome)
print("*")

print("-"*20)
print("POR APENAS UM DELES")
print("-"*20)
for nome in umDeles:
    print(nome)