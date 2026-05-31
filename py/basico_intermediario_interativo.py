nome = input("Digite seu nome:")
print(f"Seu nome é {nome}!")

# tentativa de cliente com tratamento de erros simples e sem controle de fluxo
try:
    idade = int(input("Digite sua idade:"))
    if idade <= 0:
        raise ValueError("Idade nao pode ser abaixo de zero!")
    print(f"A sua idade é {idade}")
except ValueError:
    print("Erro: Entrada inválida!")
finally:
    print("Fim da execução.")

# imput com condicionais e com controle de fluxo
nome = input("Digite seu nome")
if nome in ["Jose", "Roberto", "Hermon"]:
    print("Acesso aceito")
else:
    print("Acesso negado")

for i in range(2):
    nome = input(f"Digite seu nome {i + 1}: ")

# funçao com input


def saudacoes():
    nome = input("Digite seu nome:")
    print(f"Seja bem-vindo, {nome} !")


saudacoes()
