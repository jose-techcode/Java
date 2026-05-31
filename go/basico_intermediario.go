package main

import (
	"fmt"
)

// Classe

type Pessoa struct {
	Nome  string
	Idade int
}

// Funções

func anonima() {
	multiplicacao := func(x float32, y float32) float32 {
		return x * y
	}
	fmt.Println(multiplicacao(10, 10))
}

func anonima2() {
	soma := func(a, z int) int {
		return a + z
	}
	fmt.Println(soma(5, 5))
}

func pessoa(nome string) string {
	return fmt.Sprintf("Seu nome: %s", nome)
}

func humano(idade int) string {
	return fmt.Sprintf("Sua idade: %d", idade)
}

func valor(numero float32) string {
	return fmt.Sprintf("Decimal: %f", numero)
}

func portugues(palavra string) string {
	return fmt.Sprintf("Palavra: %s", palavra)
}

func cadastro(nome0 string) string {
	return fmt.Sprintf("Nome: %s", nome0)
}

func calculadora_anonima(a, b float64) float64 {
	soma := func(a, b float64) float64 {
		return a + b
	}
	subtracao := func(a, b float64) float64 {
		return a - b
	}
	multiplicacao := func(a, b float64) float64 {
		return a * b
	}
	divisao := func(a, b float64) float64 {
		return a / b
	}
	fmt.Println(soma(a, b))
	fmt.Println(subtracao(a, b))
	fmt.Println(multiplicacao(a, b))
	fmt.Println(divisao(a, b))

	return soma(a, b)
	// return subtracao(c, d)
	// return multiplicacao(e, f)
	// return divisao(g, h)
}

func par_impar(valor int) int {

	if valor%2 == 0 {
		fmt.Printf("É par: %d\n", valor)
	} else {
		fmt.Printf("É ímpar: %d\n", valor)
	}

	return valor
}

func primo_composto(valor int) bool {

	var i int
	for i = 2; i < valor; i++ {
		if valor%i == 0 {
			return false
		} else {
			return true
		}
	}
	return true
}

// Função central

func main() {

	// numero, err := // valor com parametro
	// if err != nil {
	// fmt.Println("Oi")
	// }

	// Estrutura de controle

	var resultado float64
	resultado = calculadora_anonima(5, 5)
	fmt.Println("Resultado:", resultado)

	fmt.Println("Go funcionando!")

	fmt.Println(10 + 5)

	var venda int
	venda = 1000

	var custo int
	custo = 500

	var lucro int
	lucro = venda - custo

	fmt.Println(lucro)

	// If-Else

	var nota int
	nota = 7
	if nota >= 7 {
		fmt.Println("Passou")
	} else {
		fmt.Println("Não passou")
	}

	sim_nao := 0
	if sim_nao > 0 {
		fmt.Println(true)
	} else {
		fmt.Println(false)
	}

	// For

	var i int
	for i = 3; i > 0; i-- {
		fmt.Println(i)
	}

	for i := 1; i < 3; i++ {
		fmt.Println(i)
	}

	// While

	var contador int
	contador = 1
	for contador < 3 {
		fmt.Printf("Contagem: %d\n", contador)
		contador += 1
	}

	// Lógica Booleana

	numero1 := true
	numero2 := false
	fmt.Println(!numero1)           // not (true)
	fmt.Println(numero1 && numero2) // and (igual)
	fmt.Println(numero1 || numero2) // or (true)

	// Estrutura de dados

	list_slice := []int{1, 2, 3, 4}
	list_array := [4]int{1, 2, 3, 4}
	dict_texto := map[string]string{"Nome": "José"}
	dict_inteiro := map[string]int{"Idade": 25}

	fmt.Println(list_slice)
	fmt.Println(list_slice[0])
	fmt.Println(list_array)
	fmt.Println(list_array[1])
	fmt.Println(dict_texto)
	fmt.Println(dict_inteiro)

	// Funções

	anonima()

	anonima2()

	mensagem := pessoa("José")
	fmt.Println(mensagem)

	numero := humano(25)
	fmt.Println(numero)

	decimal := valor(24.75)
	fmt.Println(decimal)

	termo := portugues("Olá")
	fmt.Println(termo)

	pessoa := Pessoa{Nome: "José", Idade: 25}

	fmt.Println(pessoa.Nome)
	fmt.Println(pessoa.Idade)

	cadastro0 := cadastro("João")
	fmt.Println(cadastro0)

	var par_ou_impar int
	par_ou_impar = 2
	par_impar(par_ou_impar)

	var primo_ou_composto int
	primo_ou_composto = 2
	if primo_composto(primo_ou_composto) {
		fmt.Printf("É primo: %d\n", primo_ou_composto)
	} else {
		fmt.Printf("É composto: %d\n", primo_ou_composto)
	}

	interactive()

}

func interactive() {

	// Normal

	// Nome

	var nome string
	fmt.Print("Digite seu nome:")
	fmt.Scanln(&nome) // Equivalente ao input do python
	fmt.Println("Olá,", nome)

	// Idade

	var idade int
	fmt.Print("Digite sua idade:")
	fmt.Scanln(&idade)
	fmt.Println("Sua idade é:", idade)

	// Tratamento de erros

	// Nome

	var nome1 string
	fmt.Println("Digite seu nome:")

	if _, err := fmt.Scanln(&nome1); err != nil {
		fmt.Println("Erro na entrada:", err)
		return
	}

	fmt.Println("Seu nome é:", nome1)

	// Idade

	var idade0 int
	fmt.Println("Digite sua idade:")

	if _, err := fmt.Scanln(&idade0); err != nil {
		fmt.Println("Erro na entrada:", err)
		return
	}

	fmt.Println("Sua idade é:", idade0)

	// While true (for infinito) com tratamento de erros incluído

	var texto string
	fmt.Println("Digite um texto (ou 'sair' para sair):")

	for {
		fmt.Print("Saída:")
		_, err := fmt.Scanln(&texto)

		if err != nil {
			fmt.Println("Erro na digitação do texto:", err)
			continue // continue ou break
		}

		if texto == "sair" {
			fmt.Println("Encerrado.")
			break
		}

		fmt.Println("Texto:", texto)
	}
}
