print("Olá, Phyton")

print(10+5-10)

# variaveis condicionais
venda = 1000
custo = 500
lucro = venda - custo
print("O lucro foi de:", lucro)

if venda == 1250:
    print("Ganhou bônus")
elif venda == 1125:
    print("Ganhou bônus simplificado")
else:
    print("Não ganhou bônus")

# Sistema de listas com controle de fluxo for (algo definido)
listarprodutos = ["iphone", "samsung", "motorola"]
listarpreços = [5000, 3500, 3000]
for item in listarprodutos:
    print(item)
for item in listarpreços:
    print(item - 500)

for i in range(2):
    print("Estude")

# controle de fluxo com quebra no caminho
for i in range(10):
    if i == 5:
        break
    print(i)

# controle de fluxo com incerteza
contador = 1
while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1

# controle de fluxo com indefiniçao
numero = 0
while numero < 10:
    numero += 1
    if numero % 2 == 0:
        continue
    print(numero)

# função anonima, ou seja, funcao com variaveis/incognitas


def subtracao(x, y): return x - y


print(subtracao(3, 5))

# funçao para retornar nome


def saudação(nome):
    return (f"Olá, {nome}!")


print(saudação("José"))

# funçao com gerador controlado por fluxo for


def contagem():
    for i in range(5):
        yield i


for valor in contagem():
    print(valor)

# logica booleana com and
x = 10
if x > 5 and x < 15:
    print(True or False)

# logica booleana com or
y = 15
if y > 10 or y == 20:
    print(True or False)

# logica booleana com not
z = 20
if z > 15 and not z < 25:
    print(True)
else:
    print(False)

# dicionario simples
pessoa = {"nome": "Josafa", "senha": "abcd", "email": "Josafa1234@gmail.com"}
print(pessoa["email"])

# dicionario composto (mais de uma pessoa)
clientes = [
    {"nome": "Davi", "senha": "davizinho_ss", "email": "Davi1234@gmail.com"},
    {"nome": "Josafa", "senha": "abcd", "email": "Josafa1234@gmail.com"}
]
for cliente in clientes:
    print("email:", cliente["email"])

# lista
aluno1 = ["Jose", 15, 7]
aluno2 = ["Davi", 15, 8]
aluno3 = ["Hermon", 15, 6]
listaralunos = [aluno1, aluno2, aluno3]
for nome, idade, nota in listaralunos:
    print(f"aluno: {nome}, {idade}, {nota}")

# conjunto por causa do {}
presenca = {"João", "Maria"}
faltaram = {"Pedro", "Maria"}
print(f"Presentes: {len(presenca)}")
print(f"Faltaram: {len(faltaram)}")
print(f"Só presentes: {presenca - faltaram}")
print(f"Só faltaram: {faltaram - presenca}")
