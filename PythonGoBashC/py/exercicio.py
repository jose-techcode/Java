print("Acesso autorizado")

print("Acesso autorizado", "Acesso negado")

# variavel com print
nome = "Cristiano Ronaldo"
print(f"Seja bem-vindo, {nome}")

# variavel com condicionais
idade = 19
if idade >= 19:
    print("Válido")
else:
    print("Inválido")

# variavel com condicionais
senha = 1234
if senha == 1234:
    print("Acessado")
else:
    print("Não acessado")

# variavel com condicionais
nota = 6
if nota >= 7:
    print("Aprovado")
else:
    print("Reprovado")

# variavel com condicionais
login = ["educprofessor"]
if login in ["educprofessor"]:
    print("Correto")
else:
    print("Incorreto")
mensagem = ["Oi, Python"]

# controle de fluxo com lista
for i in mensagem:
    print(i)
listadenomes = ["Jose", "Joao", "Josafa"]
for i in listadenomes:
    print(i)

# controle de fluxo com for
for i in range(5):
    print(f"{i + 1}")

# controle de fluxo completa com for
for i in range(3, 10, 2):
    print(i)

# controle de fluxo completa com numero negativo com for
for i in range(10, 0,  -1):
    print(i)
contador = 5

# controle de fluxo indefinida com while
while contador <= 10:
    print(f"Cronômetro: {contador}")
    contador += 1

# controle de fluxo com condicionais e com quebra de fluxo
for i in range(10):
    if i == 4:
        break
    print(i)
contador = 3

# controle de fluxo indefinido com while com condicionais e com quebra de fluxo
while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1
    if contador == 2:
        break

# lista com controle de fluxo com for com condicionais e com pulo de fluxo
listadepalavras = ["nome", "senha", "login"]
for i in listadepalavras:
    if i in ["senha"]:
        continue
    print(i)

# controle de fluxo com condicionais com pulo de fluxo
for i in range(5):
    if i == 1:
        continue
    print(i)

# funcao normal


def pessoa(nome):
    print(f"Olá, {nome}")


pessoa("Gabriel")

# funcao normal


def idade(mostrar_idade):
    print(f"Olá, você tem {mostrar_idade} anos!")


idade(10)

# funcao com retorno


def nomes(nome):
    return (f"Oi, {nome}")


print(nomes("Joao"))

# funcao com retorno


def valor():
    return 10


resultado = valor()
print(resultado)

# funçao com condicionais com retorno


def verificacao(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperacao"
    else:
        return "Reprovado"


print(f"{verificacao(6)}")

# funcao com condicionais e com retorno


def numero(par):
    if par % 2 == 0:
        return True
    else:
        return False


print(f"{numero(3)}")

# funçao anonima com variaveis/incognitas


def divisao(x, y): return int(x / y)


print(divisao(8, 2))

# funcao com controle de fluxo de geraçao


def contando():
    for i in range(3):
        yield i


for numero in contando():
    print(numero)

# bool
x = 10
if x > 5 and x < 15:
    print(True or False)

# bool
y = 15
if y > 10 or y == 20:
    print(True or False)

 # bool
z = 20
if z > 15 and not z < 25:
    print(True)
else:
    print(False)

# dicionario simples com deletaçao de uma parte
pessoa = {"nome": "John", "senha": "1234",
          "email": "Jhon1234@gmail.com", "login": "admin"}
print(pessoa["email"])
del (pessoa["login"])

# dicionario composto
clientes = [
    {"nome": "Jose", "senha": "Brasileiro1234", "email": "Jose1234@gmail.com"},
    {"nome": "John", "senha": "Brasil1234", "email": "Jhon1234@gmail.com"}
]
for cliente in clientes:
    print("nome:", cliente["nome"])

# tupla de produtos com controle de fluxo
produto1 = ("Mouse", 150, "Informática")
produto2 = ("Teclado", 200, "Informática")
produto3 = ("Monitor", 500, "Informática")
listarprodutos = [produto1, produto2, produto3]
for nome, preco, categoria in listarprodutos:
    print(f"Produto: {nome}, R$ {preco}, {categoria}")

# conjunto por causa do len e do {}
pacientespresentes = {"Lucas", "Daniel"}
pacientesausentes = {"Pedro", "Paulo"}
print(f"Presentes: {len(pacientespresentes)}")
print(f"Ausentes: {len(pacientesausentes)}")
print(f"Só vieram: {pacientespresentes - pacientesausentes}")
print(f"Não vieram: {pacientesausentes - pacientespresentes}")

lista = [x * 1 for x in range(5)]
print(lista)

dicionario = {x: x * 1 for x in range(5)}
print(dicionario)

conjunto = {x * 1 for x in range(5)}
print(conjunto)

tupla = tuple(x * 1 for x in range(5))
print(tupla)
