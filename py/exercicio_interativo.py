nome = input("Digite seu nome:")
print(f"Seja bem-vindo, {nome}!")

# tentativa de cliente com tratamento de erros simples sem controle de fluxo e com condicionais
try:
    idade = int(input("Digite sua idade:"))
    print(f"Sua idade é {idade}!")
except ValueError:
    print("Erro: Entrada inválida!")
finally:
    print("Fim da execução")
nome = input("Digite seu nome:")
if nome in ["Jose", "Joao", "Jiraya"]:
    print("Permissão Aceita")
else:
    print("Permissão Negada")

# input com condicionais
senha = input("Digite sua senha")
if senha == "Jose1234@":
    print("Permitido")
else:
    print("Não Permitido")

# tentativa de cliente com condicionais sem controle de fluxo e com tratamento de erros simples
try:
    nota = int(input("Digite sua nota:"))
    if nota >= 6:
        print("Aprovado")
    else:
        print("Reprovado")
except ValueError:
    print("Erro: Não é um número inteiro!")
finally:
    print("Fim da execução")

# input com condicionais
login = input("Digite seu nome:")
if login in ["estud.aluno"]:
    print("Correto")
else:
    print("Incorreto")

# input com controle de fluxo com for e range
for i in range(3):
    mensagem = input(f"Escreva sua mensagem {i + 1}")

# input com condicionais com while e sem if
login = input("Insira seu login")
while login == ["admin"]:
    print("Concedido")
else:
    print("Não Concedido")

# funcao com input


def bemvindo():
    nome = input("Digite seu nome funcional:")
    print(f"Seu nome é {nome}!")


bemvindo()

# funcao com input com condicionais


def saudacao():
    identidade = input("Digite sua identificação:")
    if identidade in ["Shrek", "Burro", "Gatodebotas"]:
        return "Certo"
    else:
        return "Errado"


saudacao()

# funcao com tentativa de cliente com condicionais e com tratamento de erros simples


def tratarerros():
    try:
        id = int(input("Digite seu ID:"))
        if id == 17:
            print("ID disponível")
        else:
            print("ID indisponível")
    except ValueError:
        print("Erro: ID incompatível")
    finally:
        print("Fim")


tratarerros()

# funcao com controle de fluxo antes da tentiva de cliente com condicionais e com tratamento de erros simples


def cadastrossemerros():
    tudo = 0
    for i in range(3):
        try:
            cadastro = int(input(f"Diga seu cadastro {i + 1}:"))
            if cadastro := (f"{19042025 + 1}"):
                print("Compatível")
            else:
                print("Incompatível")
        except ValueError:
            print("Erro: Apenas é permitido números inteiros!")
        finally:
            print("Próximo:")


cadastrossemerros()

# funcao com input


def tempo(idade):
    idade = input("Digite sua idade funcional:")
    print(f"Olá, sua idade é {idade}!")


# controle de fluxo com condicionais com quebra de fluxo, todos cobertos de logica booleana
while True:
    entrada = input("Digite seu nome:")
    if not entrada.isnumeric():
        nome = str(entrada)
        break
    else:
        print("Erro. Tente novamente.")

# controle de fluxo com condicionais com pulo de fluxo e no final com quebra de fluxo, todos cobertos de logica booleana
while True:
    nomezinho = input("Digite seu nomezinho ou pule")
    if nomezinho == " ":
        continue
    print(f"Nome registrado: {nome}")
    break
