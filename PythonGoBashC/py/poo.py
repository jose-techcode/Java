class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("João", 15)
print(p1.nome)
print(p1.idade)


class Retângulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura


r1 = Retângulo(15, 10)
print(r1.largura)
print(r1.altura)
print(r1.area())


class Contabancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def getsaldo(self):
        return self.__saldo

    def setsaldo(self, valor):
        print("Não é permitido alterar o saldo!")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(
                f"Valor depositado com sucesso. Saldo atual: RS:{self.saldo: .1f}")
        else:
            print("Valor inválido! Valor depositado deve ser maior que zero!")

    def sacar(self, valor):
        if valor > 0:
            self.saldo -= valor
            print(
                f"Valor sacado com sucesso! Saldo atual: RS:{self.saldo: .1f}")
        else:
            print("Valor inválido! Valor sacado deve ser maior que zero!")


c1 = Contabancaria("Jose", 1000)
c1.depositar(500)
c1.sacar(250)
print(c1.saldo)


class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

    def media(self):
        if self.nota >= 7:
            print("Aprovado")
        else:
            print("Reprovado")


a1 = Aluno("Jose", 20172204, 7)
a1.media()


class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def calcularpagamento(self):
        return 0

    def exibirpagamento(self):
        print(f"{self.nome} vai receber {self.calcularpagamento(): .1f}")


class FuncionarioHora(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcularpagamento(self):
        return self.horas_trabalhadas * self.valor_hora


class FuncionarioMensal(Funcionario):
    def __init__(self, nome, salariomensal):
        super().__init__(nome)
        self.salariomensal = salariomensal

    def calcularpagamento(self):
        return self.salariomensal


class FuncionarioComissao(Funcionario):
    def __init__(self, nome, vendas, percentual_comissao):
        super().__init__(nome)
        self.vendas = vendas
        self.percentual_comissao = percentual_comissao

    def calcularpagamento(self):
        return self.vendas * self.percentual_comissao


funcionarios = [
    FuncionarioHora("Jose", 8, 100),
    FuncionarioMensal("Joao", 1518),
    FuncionarioComissao("Emanuel", 20, 100)
]

for funcionario in funcionarios:
    funcionario.exibirpagamento()


class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def media(self):
        if self.nota >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


while True:
    try:
        nome = str(input("Digite seu nome:")) # permite qualquer tipo de caractere
        idade = int(input("Digite sua idade:"))
        nota = float(input("Digite sua nota:"))
        a1 = Aluno(nome, idade, nota)
        print(f"Nome: {a1.nome}, Idade: {a1.idade}, Nota: {a1.nota}")
        print(a1.media())
        break
    except ValueError:
        print("Erro: Valor inválido!")
