print("Oi, mundo")

A = 10
B = 5
print(A - B)

area = 3.14 * 7
print(area)

X = 25
Y = 20
SOMA = print(X + Y)


def SOMA(x, z): return (x*z)


print(SOMA(5, 5))

PROD = 100 - 25
print(PROD)


def PROD(a, b): return (a - b)


print(PROD(100, 25))

MEDIA = (6.0 + 7.1)/2
print(MEDIA)

MEDIA = (7.0 + 9.0 + 8.5)/3
print(MEDIA)


def MEDIA(q, v, x, y, z): return (q + v + x + y)/z


print(MEDIA(4.5, 5.0, 5.5, 7.5, 4))

A = 10
B = 5
C = 8
D = 7
DIFERENCA = (A * B - C * D)
print(DIFERENCA)

horas_trabalhadas = 8
salario_por_hora = 50.50
salario_no_final_do_dia = horas_trabalhadas * salario_por_hora
print(salario_no_final_do_dia)

salario_fixo = 500
faturamento_de_vendas = 1000
jose_vai_receber = salario_fixo + faturamento_de_vendas/5
print(jose_vai_receber)

quantidade_do_produto = 5
valor_unitario = 100
valor_a_pagar = quantidade_do_produto * valor_unitario
print(f"R${valor_a_pagar}")

volume = (4.0/3.0) * 3.14159 * 3.5 ** 3
print(volume)

maior = max(7, 14, 100)
print(f"O maior é o {maior}")

menor = min(7, 14, 100)
print(f"O menor é o {menor}")

distancia_total_percorrida = 250
combustivel_usado = 17.5
distancia_combustivel = distancia_total_percorrida/combustivel_usado
print(f"{distancia_combustivel} km/l")

distancia = ((2.0 - 5.0)**2 + (3.0 - 7.0)**2)**0.5
print(distancia)

carro1 = 60
carro2 = 90
km = carro2 - carro1
minutos = km * 2
print(
    f"São necessários {minutos} minutos para um carro se distanciar 30km um do outro")

km_por_litro = 12
tempo_de_viagem = 8
km_por_hora = 60
litros_necessarios = (km_por_hora * tempo_de_viagem)/km_por_litro
print(litros_necessarios)

segundos = 600
minutos = segundos/60
print(minutos)

dias = 395
anos = dias/365
print(anos)

numerador1 = 10
denominador1 = 5
numerador2 = 20
denominador2 = 10
soma = (numerador1 * denominador2 + numerador2 *
        denominador1)/(denominador1 * denominador2)
subtracao = (numerador1 * denominador2 - numerador2 *
             denominador1)/(denominador1 * denominador2)
multiplicacao = (numerador1 * numerador2)/(denominador1 * denominador2)
print(soma)
print(subtracao)
print(multiplicacao)

salario1 = 1000
salario2 = 2000
reajuste_salarial1 = salario1/5 + salario1
reajuste_salarial2 = salario2/10 + salario2
print(reajuste_salarial1)

valor = 10
tabuada_do_10 = 10 * 1, 10 * 2, 10 * 3, 10 * 4, 10 * \
    5, 10 * 6, 10 * 7, 10 * 8, 10 * 9, 10 * 10
print(tabuada_do_10)

numero1 = 5
numero2 = -5
if numero1 > 0:
    print("Positivo")
if numero2 > 0:
    print("Positivo")
else:
    print("Negativo")

possivel_multiplo1 = 7
possivel_multiplo2 = 20
if possivel_multiplo1 % possivel_multiplo2 == 0:
    print("sao multiplos")
else:
    print("nao sao multiplos")

for i in range(2, 10, 2):
    print(i)

impar = 0
while impar < 10:
    impar += 1
    if impar % 2 == 0:
        continue
    print(impar)

primo = 1
achados = 0
while achados < 5:
    primo += 1
    for i in range(2, primo):
        if primo % 2 == 0:
            break
    else:
        print(primo)
        achados += 1

composto = 1
encontrados = 0
while encontrados < 5:
    composto += 1
    for i in range(1, composto):
        if composto % 2 == 1:
            break
    else:
        print(composto)
        encontrados += 1

estados = {21: "Rio de Janeiro", 11: "Sao Paulo", 61: "Brasilia"}
while True:
    try:
        DDD = int(input("Digite seu DDD:"))
        if DDD == 21:
            print("Rio de Janeiro")
        elif DDD == 11:
            print("Sao Paulo")
        elif DDD == 61:
            print("Brasilia")
        else:
            print("DDD não cadastrado")
        break
    except ValueError:
        print("Erro: Apenas números inteiros são permitidos!")
    except ZeroDivisionError:
        print("Erro: O número deve ser maior que zero!")

while True:
    try:
        km_litro2 = int(input("Digite a quantidade KM/L do carro:"))
        tempo_de_viagem2 = int(input("Digite seu tempo de viagem:"))
        km_por_hora2 = int(input("Digite sua quantidade KM por hora:"))
        litros = (tempo_de_viagem2 * km_por_hora2)/km_litro2
        print(f"Quantidade de litros usadas: {litros: .2f}")
        break
    except ValueError:
        print("Erro: Entrada inválida")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero")
    finally:
        print("Fim de programa")

while True:
    try:
        IR = int(input("Digite a declaração de sua renda:"))
        if IR < 2000:
            print("Isento.")
        if IR > 2000 and IR < 3000:
            print(f"5% tributado: {IR * 0.05}")
        if IR > 3000 and IR < 4500:
            print(f"10% tributado: {IR * 0.10}")
        else:
            print(f"15% tributado: {IR * 0.15}")
        break
    except ValueError:
        print("Erro: Não são válidos letras!")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero")
    finally:
        print("Fim de declaração.")

lista = [x * 1 for x in range(5)]
print(lista)

dicionario = {x: x * 1 for x in range(5)}
print(dicionario)

conjunto = {x * 1 for x in range(5)}
print(conjunto)

tupla = tuple(x * 1 for x in range(5))
print(tupla)
