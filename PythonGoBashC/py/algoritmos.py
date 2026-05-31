# -BUSCA-

# 1 linear


def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1


lista = [2, 4, 3, 1]
busca = busca_linear(lista, 4)
print(f"O item foi encontrado em busca {busca} linear")

# 2 linear


def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1


lista = [4, 9, 2, 3, 1]
busca = busca_linear(lista, 3)
print(f"O item foi encontrado em procura {busca} linear")

# 3 linear 


def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1


lista = [4, 2, 8, 6]
localizacao = busca_linear(lista, 8)
print(f"O item foi encontrado em localização {localizacao} linear")

# 4 linear


def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1


lista = [29, 24, 37, 32]
busca = busca_linear(lista, 24)
print(f"O item foi encontrado em busca {busca} linear")

# 5 linear


def busca_linear(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1


lista = [39, 34, 47, 44, 52]
busca = busca_linear(lista, 44)
print(f"O item foi encontrado em busca {busca} linear ")

# 1 binaria


def procura_binaria(lista, item):
    esquerda = 0
    direita = len(lista) - 1
    # formula
    while esquerda <= direita:
        meio = (esquerda + direita) // 2  # formula
        if lista[meio] == item:
            return meio
        if lista[meio] < item:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


lista = [1, 2, 3, 4]
procura = procura_binaria(lista, 2)
print(f"O item foi encontrado em procura {procura} binaria")

# 2 binaria


def busca_binaria(lista, item):
    suposto_menor = 0
    suposto_maior = len(lista) - 1
    # formula
    while suposto_menor <= suposto_maior:
        meio_termo = (suposto_menor + suposto_maior) // 2  # formula
        if lista[meio_termo] == item:
            return meio_termo
        elif lista[meio_termo] < item:
            suposto_menor = meio_termo + 1
        else:
            suposto_maior = meio_termo - 1
    return -1


lista = [1, 2, 3, 4]
busca = busca_binaria(lista, 3)
print(f"O item foi encontrado em busca {busca} binaria")

# 3 binaria


def localizacao_binaria(lista, item):
    numero1 = 0
    numero2 = len(lista) - 1
    # formula
    while numero1 <= numero2:
        numero3 = (numero1 + numero2) // 2  # formula
        if lista[numero3] == item:
            return numero3
        if lista[numero3] > item:
            numero2 = numero3 - 1
        else:
            numero1 = numero3 + 1
    return -1


lista = [1, 2, 3, 4]
localizaçao = localizacao_binaria(lista, 4)
print(f"O item foi encontrado em localização {localizaçao} binaria")

# 4 binaria


def busca_binaria(lista, item):
    numero1 = 0
    numero2 = len(lista) - 1
    # formula
    while numero1 <= numero2:
        numero3 = (numero1 + numero2) // 2
        if lista[numero3] == item:
            return numero3
        if lista[numero3] > item:
            numero2 = numero3 - 1
        else:
            numero1 = numero3 + 1
    return -1


lista = [1, 2, 3, 4]
busca = busca_binaria(lista, 3)
print(f"O item foi encontrado em busca {busca} binaria")

# 5 binaria


def busca_binaria(lista, item):
    numero0 = 0
    numero1 = len(lista) - 1
    # formula
    while numero0 <= numero1:
        numero2 = (numero0 + numero1) // 2
        if lista[numero2] == item:
            return numero2
        if lista[numero2] > item:
            numero1 = numero2 - 1
        else:
            numero2 = numero1 + 1
    return -1

lista = [4, 5, 6, 7]
busca = busca_binaria(lista, 5)
print(f"O item foi encontrado em busca {busca} binaria")

# -ORDENAÇÃO-

# 1 bubblesort


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):  # formula
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


lista = [5, 4, 3, 2, 1, 10]
ordenacao = bubble_sort(lista)
print(f"A lista é {ordenacao} 1 bubblesort")

# 2 bubblesort


def bubble_sort(lista):
    x = len(lista)
    for i in range(x):
        for j in range(0, x - i - 1):  # formula
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


lista = [29, 24, 16, 9, 100]
ordenaçao = bubble_sort(lista)
print(f"A lista é {ordenaçao} 2 bubblesort")

# 3 bubblesort


def bubble_sort(lista):
    y = len(lista)
    for i in range(y):
        for j in range(0, y - i - 1):  # formula
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


lista = [20, 23, 16, 19, 77]
ordenaçao = bubble_sort(lista)
print(f"A lista é {ordenaçao} 3 bubblesort")

# 4 bubblesort


def bubble_sort(lista):
    x = len(lista)
    for i in range(x):
        # formula
        for j in range(0, x - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [9, 4, 7, 14, 11]
ordenacao = bubble_sort(lista)
print(f"A lista é {ordenaçao} 4 bubblesort")

# 5 bubblesort


def bubble_sort(lista):
    z = len(lista)
    for i in range(z):
        # formula
        for j in range(0, z - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [19, 17, 24, 29, 14]
ordenacao = bubble_sort(lista)
print(f"A lista é {ordenaçao} 5 bubblesort")


lista = [21, 14, 9, 7, 28]  # aguenta 10
ordenacao = bubble_sort(lista)
print(f"A lista é ordenacao {ordenacao} 4 bubblesort")

# 1 selectionsort


def selection_sort(lista):
    x = len(lista)
    for i in range(x):
        menor = i
        for j in range(i + 1, x):  # formula
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista


lista = [5, 4, 9, 7, 32, 29]
ordenaçao = selection_sort(lista)
print(f"A lista é {ordenaçao} 1 selectionsort")

# 2 selectionsort


def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        maior = i
        for j in range(i + 1, n):  # formula
            if lista[j] > lista[maior]:
                j = maior
        lista[i], lista[maior] = lista[maior], lista[i]
    return lista


lista = [7, 5, 10, 24, 21]
ordenaçao = selection_sort(lista)
print(f"A lista é {ordenaçao} 2 selectionsort")

# 3 selectionsort


def selection_sort(lista):
    y = len(lista)
    for i in range(y):
        igual = i
        for j in range(i + 1, y):  # formula
            if lista[igual] > lista[j]:
                igual = j
        lista[i], lista[igual] = lista[igual], lista[i]
    return lista


lista = [5, 9, 7, 4, 11]
ordenaçao = selection_sort(lista)
print(f"A lista é {ordenacao} 3 selectionsort")

# 4 selectionsort


def selection_sort(lista):
    x = len(lista)
    for i in range(x):
        continuacao = i
        # formula
        for j in range(i + 1, x):
            if lista[continuacao] > lista[j]:
                continuacao = j
                lista[i], lista[continuacao] = lista[continuacao], lista[i]
    return lista


lista = [11, 9, 14, 7, 3]  # aguenta 100
ordenacao = selection_sort(lista)
print(f"A lista é {ordenacao} 4 selectionsort")

# 5 selectionsort
def selection_sort(lista):
    y = len(lista)
    for i in range(y):
        outro = 1
        for j in range(i + 1, y):
            if lista[outro] > lista[j]:
                outro = j
                lista[i], lista[outro] = lista[outro], lista[i]
    return lista

lista = [34, 39, 29, 24, 27]
ordenacao = selection_sort(lista)
print(f"A lista é {ordenacao} 5 selectionsort")


# 1 insertionsort


def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        # formula
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave


lista = [4, 1, 7, 5, 9]
insertion_sort(lista)
print("A lista é 1 insertionsort", lista)

# 2 insertionsort


def insertion_sort(lista):
    for i in range(1, len(lista)):
        colchete = lista[i]
        # formula
        j = i - 1
        while j >= 0 and lista[j] > colchete:
            lista[j + 1] = lista[j]
            j -= 1
            lista[j + 1] = colchete


lista = [9, 7, 4, 2, 5]
insertion_sort(lista)
print("A lista é 2 insertionsort", lista)

# 3 insertionsort


def insertion_sort(lista):
    for i in range(1, len(lista)):
        parenteses = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > parenteses:
            lista[j + 1] = lista[j]
            j -= 1
            lista[j + 1] = parenteses


lista = [14, 11, 17, 27, 24]
insertion_sort(lista)
print("A lista é 3 insertionsort", lista)

# 4 insertionsort


def insertion_sort(lista):
    for i in range(1, len(lista)):
        arroba = lista[i]
        # formula
        j = i - 1
        while j >= 0 and lista[j] > arroba:
            lista[j + 1] = lista[j]
            j -= 1
            lista[j + 1] = arroba


lista = [4, 7, 9, 5, 2]
insertion_sort(lista)
print("A lista é 4 insertionsort", lista)


# 5 insertionsort


def insertion_sort(lista):
    for i in range(1, len(lista)):
        hastag = lista[i]
        # formula
        j = i - 1
        while j >= 0 and lista[j] > hastag:
            lista[j + 1] = lista[j]
            j -= 1
            lista[j + 1] = hastag


lista = [29, 34, 27, 24, 37]  # aguenta 200
insertion_sort(lista)
print("A lista é 5 insertionsort", lista)

# formula do bubblesort = 0, variavel - i - 1, for, if, return
# formula do selectionsort = i + 1, variavel, for, if, return
# formula do insertionsort = j = i - 1, variaveis, for e while.