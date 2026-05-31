#!/bin/bash

# -eq igual
# -ne diferente
# -gt maior que
# -ge maior ou igual
# -lt menor que
# -le menor ou igual

echo "Olá, Bash"

echo $((10 + 5))

a=5
b=5
soma=$((a+b))
echo $soma

nome="jose"
echo $nome

# -Lógica booleana-

x=5
y=5

# AND

if [ "$x" -eq 5 ] && [ "$y" -eq 5 ]; then
    echo "Juntos"
else 
    echo "Separados"
fi

if [[ "$x" -eq 5 && "$y" -eq 5 ]]; then
    echo "Juntos"
else 
    echo "Separados"
fi

# OR

if [ "$x" -eq 5 ] || [ "$y" -eq 3 ]; then
    echo "Algum é 5"
else 
    echo "Nenhum é 5"
fi

if [[ "$x" -eq 5 || "$y" -eq 5 ]]; then
    echo "Algum é 5"
else 
    echo "Nenhum é 5"
fi

# NOT

if [[ "$x" != 5 ]]; then
    echo "X é diferente de 5"
else 
    echo "X é igual a 5"
fi

if [[ "$x" != 5 && "$y" != 5 ]]; then
    echo "X e Y são diferentes de 5"
else 
    echo "X e Y são iguais a 5"
fi

if [[ "$x" != 5 || "$y" != 5 ]]; then
    echo "X ou Y é diferente de 5"
else 
    echo "X ou Y é igual a 5"
fi

# -Estrutura de controle-

# Se tem then, tem fi

nota=7
if [ $nota -ge 7 ]; then
echo "Passou"
elif [ $nota -ge 5 ]; then
echo "Recuperação"
else
echo "Não passou"
fi

# Definido
# Se tem then, tem fi

nome0="jose"
if [ $nome0 = "jose" ]; then
echo "Válido"
else
echo "Inválido"
fi

# Definido
# Se tem do, tem done

for ((i=1; i <= 3; i++)); do
echo $i
done

# Indefinido
# Se tem do, tem done

contador=1
while ((contador <= 3)); do
echo $contador
((contador++))
done

# -Listas (estrutura de dados)-

lista=("tomate" "cebola" "alface")
echo "${lista[@]}" # @ representa todos os vetores
echo "${lista[0]}"

lista0=(1 2 3)
echo "${lista0[@]}" # @ representa todos os vetores

# Soma

soma_vetor=$(( lista0[0] + lista0[1] ))
echo "$soma_vetor"

# Subtração

subtracao_vetor=$(( lista0[0] - lista0[1] ))
echo "$subtracao_vetor"

# Multiplicação

multiplicacao_vetor=$(( lista0[0] * lista0[1] ))
echo "$multiplicacao_vetor"

divisao_vetor=$(( lista0[0] + lista0[1 ]))
echo "$divisao_vetor"

# -Funções-

soma() {
  local resultado=0 # começa por nenhum numero
  for numero in "$@"; do
    (( resultado += numero ))
  done
  echo "Resultado: $resultado"
}

subtracao() {
    local resultado=$1 # primeiro número
    shift # começa pelo primeiro numero
    for num in "$@"; do
        (( resultado -= num ))
    done
    echo "Resultado: $resultado"
}

multiplicacao() {
    local resultado=$1 # primeiro numero
    shift # começa pelo primeiro numero
    for number in "$@"; do
        (( resultado *= number))
    done
    echo "Resultado: $resultado"
}

divisao() {
    local resultado=$1 # primeiro numero
    shift # começa pelo primeiro numero
    for numerozinho in "$@"; do
        (( resultado /= numerozinho ))
    done
    echo "Resultado: $resultado"
}

par_impar() {
    local valor=$1
    shift
    
    if [[ $valor -eq 0 ]]; then
    echo "0 não é par"
    fi
    
    if (( valor % 2 == 0 )); then
    echo "$valor é par"
    else
    echo "$valor é ímpar"
    fi

}

primo_composto() {
    local valor=$1
    shift

    if [[ $valor -le 1 ]]; then
    echo "0 e 1 não contam"
    fi

    for (( i = 2; i * i <= valor; i++ )) do
    if (( valor % i == 0 )); then
    echo "$valor é composto"
    return
    fi
    done
    echo "$valor é primo"
}

soma 10 10
subtracao 10 5
multiplicacao 5 5
divisao 100 10
par_impar 4
primo_composto 2