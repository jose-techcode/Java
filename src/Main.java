import ContaBancariaPrincipal_ContaBancariaConjunta.ContaBancariaConjunta;
import ContaBancariaPrincipal_ContaBancariaConjunta.ContaBancariaPrincipal;
import Funcionario_Gerente_Peao.Funcionario;
import Funcionario_Gerente_Peao.Gerente;
import Funcionario_Gerente_Peao.Peao;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class Main {

    // --FUNÇÕES--

    // Hello sem return

    public static void Hello() {
        System.out.println("Hello");
    }

    // Hello com return

    public static String hello() {
        return "hello";
    }

    // Soma

    public static int soma(int x, int y) {
        return x + y;
    }

    // Subtração

    public static double subtracao(double a, double b) {
        return a - b;
    }

    // Par

    public static boolean par(int valor) {
        if (valor == 0) {
            return false;
        }
        for (int i = 2; i <= valor;) {
            return valor % i == 0;
        }
        return false;
    }

    // Ímpar

    public static boolean impar(int valorzinho) {
        if (valorzinho == 0) {
            return false;
        }
        if (valorzinho == 1) {
            return true;
        }
        for (int i = 2; i <= valorzinho;) {
            return valorzinho % i != 0;
        }
        return false;
    }

    // Primo

    public static boolean primo(int numero) {
        if (numero <= 1) {
            return false;
        }
        for (int i = 2; i < numero; i++) {
            if (numero % i == 0) {
                return false;
            }
        }
        return true;
    }

    // Composto

    public static boolean composto(int numerozinho) {
        if (numerozinho <= 1) {
            return false;
        }
        for (int i = 2; i < numerozinho; i++) {
            if (numerozinho % i == 0) {
                return true;
            }
        }
        return false;
    }

    // Scanner (texto)

    public static String login() {
        Scanner scanner = new Scanner(System.in);
        String login_nome = "";
        try {
            System.out.println("Digite seu nome:");
            login_nome = scanner.nextLine();
        } catch (InputMismatchException e) {
            System.out.println("Tipo de dado inválido passado a pergunta: " + e.getMessage());
        } catch (NoSuchElementException e) {
            System.out.println("Não foi encontrado o elemento chamado: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        }
        return login_nome;
    }

    // Scanner (número inteiro)

    public static int idade() {
        Scanner scanner = new Scanner(System.in);
        int idade = -1;
        while (idade < 1) {
            try {
                System.out.println("Digite sua idade: ");
                idade = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Tipo de dado inválido passado a pergunta: " + e.getMessage());
                scanner.next();
            } catch (NoSuchElementException e) {
                System.out.println("Não foi encontrado o elemento chamado: " + e.getMessage());
                scanner.next();
            } catch (Exception e) {
                System.out.println("Erro: " + e.getMessage());
                scanner.next();
            }
        }
        return idade;
    }

    // Scanner (texto e número inteiro)

    public static void nome_idade() {
        Scanner scanner = new Scanner(System.in);
        String nome = "";
        int idade = 0;
        try {
            System.out.println("Digite seu nome: ");
            nome = scanner.nextLine();

            System.out.println("Digite sua idade: ");
            idade = scanner.nextInt();

            System.out.println("Nome: " + nome + " | " + "Idade: " + idade);
        } catch (InputMismatchException e) {
            System.out.println("Tipo de dado inválido passado a pergunta: " + e.getMessage());
        } catch (NoSuchElementException e) {
            System.out.println("Não foi encontrado o elemento chamado: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Erro: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    static void main(String[] args) {

        // Package: ContaBancariaPrincipal_ContaBancariaConjunta

        ContaBancariaPrincipal minha_Conta = new ContaBancariaPrincipal("José", 1000);

        minha_Conta.getSaldo();
        minha_Conta.deposito(500);
        minha_Conta.saque(250);
        minha_Conta.setSaldo();
        minha_Conta.getSaldo();

        ContaBancariaConjunta Conta_conjunta = new ContaBancariaConjunta();

        Conta_conjunta.getSaldo();
        Conta_conjunta.deposito(-50);
        Conta_conjunta.saque(0);
        Conta_conjunta.setSaldo();
        Conta_conjunta.getSaldo();

        // Package: Funcionario_Gerente_Peao

        Funcionario funcionario0 = new Funcionario(100);

        funcionario0.getSalarioPagamento();
        funcionario0.salariopagamento(-50);
        funcionario0.salariopagamento(0);
        funcionario0.salariopagamento(100);
        funcionario0.setSalarioPagamento();
        funcionario0.getSalarioPagamento();

        Gerente gerente = new Gerente(5000);

        gerente.getSalarioPagamento();
        gerente.salariopagamento(-50);
        gerente.salariopagamento(0);
        gerente.salariopagamento(100);
        gerente.salariopagamento(5500);
        gerente.setSalarioPagamento();
        gerente.getSalarioPagamento();

        Peao peao = new Peao(1518);

        peao.getSalarioPagamento();
        peao.salariopagamento(-50);
        peao.salariopagamento(0);
        peao.salariopagamento(100);
        peao.salariopagamento(2000);
        peao.setSalarioPagamento();
        peao.getSalarioPagamento();

        // Scanner (Input/Output)

        //Scanner scanner = new Scanner(System.in);
        //try {

        //System.out.println("Digite seu nome (texto): ");
        //String nomee = scanner.nextLine(); // nextLine para texto

        //System.out.println("Digite sua idade (número inteiro): ");
        //int idadee = scanner.nextInt(); // nextInt para número inteiro e nextDouble para número decimal

        //System.out.println("Olá, " + nomee + "! Você tem " + idadee + " anos.");
        //} catch (InputMismatchException e) {
        //System.out.println("Tipo de argumento inválido passado a função: " + e.getMessage());
        //} catch (NoSuchElementException e) {
        //System.out.println("Não foi encontrado o elemento chamado: " + e.getMessage());
        //} catch (Exception e) {
        //System.out.println("Erro genérico: " + e.getMessage());
        //} finally {
        //System.out.println("Café: Java");
        //scanner.close();
        //}

        // --TIPOS DE DADOS E OPERADORES--

        System.out.println("Java");
        System.out.println(5 + 5);

        // int (Integer), byte (Byte), short (Short), long (Long), float (Float), double (Double), String, char (Char), boolean (Boolean)
        // + - * / % += -= *= /= = == > < != >= <= && || ! ++ -- ?: instanceof new

        // --ESTRUTURA DE CONTROLE--

        // -If-

        int nota0 = 7;
        if (nota0 >= 7) {
            System.out.println("Passou");
        } else {
            System.out.println("Não passou");
        }

        double nota1 = 6.5;
        if (nota1 >= 7) {
            System.out.println("Passou");
        } else if (nota1 >= 6) {
            System.out.println("Recuperação");
        } else {
            System.out.println("Reprovou");
        }

        String login = "jose";
        if (login.equals("jose")) {
            System.out.println("Concedido");
        } else {
            System.out.println("Negado");
        }

        char letra = 'a';
        if (letra == 'b') {
            System.out.println("Permitido");
        } else {
            System.out.println("Não permitido");
        }

        // -For-

        // Crescente

        for (int i = 1; i <= 3; i++) {
            System.out.println("For crescente: " + i);
        }

        // Decrescente

        for (int i = 3; i >= 1; i--) {
            System.out.println("For decrescente: " + i);
        }

        // -While-

        // ++

        int contador0 = 1;
        while (contador0 <= 3) {
            System.out.println("Contador0: " + contador0);
            contador0++;
        }

        // +=

        int contador1 = 0;
        while (contador1 <= 2) {
            contador1 += 1;
            System.out.println("Contador1: " + contador1);
        }

        // Par

        int par = 1;
        while (par <= 10) {
            par += 1;
            System.out.println("Pares: " + par);
            par++;
        }

        // Ímpar

        int impar = 2;
        while (impar <= 10) {
            impar += 1;
            System.out.println("Ímpares: " + impar);
            impar++;
        }

        // -Lógica Booleana-

        // And

        boolean x = true;
        boolean y = false;
        boolean xy = x && y;
        System.out.println(xy);

        // Or

        boolean z0 = true;
        boolean z1 = false;
        boolean z0z1 = z0 || z1;
        System.out.println(z0z1);

        // Not

        boolean a0 = true;
        boolean b1 = !a0;
        System.out.println(b1);

        // And, Or, Not

        boolean q = true;
        boolean v = false;
        boolean w = false;
        boolean qvw = (q && !v) || w;
        System.out.println(qvw);

        // --ESTRUTURA DE DADOS-- OBS: Implementações das interfaces list, map e set

        // -Lista sem coleção 1 (String[])-

        String[] fruta0 = new String[2];

        fruta0[0] = "Maçã";
        fruta0[1] = "Banana";

        for (int i = 0; i < fruta0.length; i++) {
            System.out.println(fruta0[i]);
        }

        System.out.println(Arrays.toString(fruta0));
        System.out.println(fruta0[0]);

        // -Lista sem coleção 2 (String[])-

        String[] fruta1 = {"Maçã", "Banana"};

        // fruta1[0] = "Uva";

        for (int i = 0; i < fruta1.length; i++) {
            System.out.println(fruta0[i]);
        }

        System.out.println(Arrays.toString(fruta1));
        System.out.println(fruta1[1]);

        // -Lista sem coleção 3 (String[])-

        String[] fruta2 = new String[]{"Maçã", "Banana"};

        // fruta2[1] = "Uva";

        for (int i = 0; i < fruta2.length; i++) {
            System.out.println(fruta0[i]);
        }

        System.out.println(Arrays.toString(fruta2));
        System.out.println(fruta2[1]);

        // - Lista mutável (ArrayList)-

        // Frutas

        ArrayList<String> frutas0 = new ArrayList<>(Arrays.asList("Maçã", "Banana"));

        frutas0.add("Uva");

        // frutas0.remove("Banana");
        // frutas0.remove(1);

        if (frutas0.contains("Uva")) {
            System.out.println("A fruta uva existe na lista");
        } else {
            System.out.println("A fruta uva não existe na lista");
        }

        for (int i = 0; i < frutas0.size(); i++) {
            System.out.println(frutas0.get(i));
        }

        System.out.println(frutas0);
        System.out.println(frutas0.getFirst());

        // Nomes

        ArrayList<String> nomes = new ArrayList<>(Arrays.asList("José", "João"));

        nomes.add("Davi");

        // nomes.remove("José");
        // nomes.remove(0);

        if (nomes.contains("Joel")) {
            System.out.println("Joel está na lista");
        } else {
            System.out.println("Joel não está na lista");
        }

        for (int i = 0; i < nomes.size(); i++) {
            System.out.println(nomes.get(i));
        }

        System.out.println(nomes);
        System.out.println(nomes.get(1));

        // Números inteiros

        ArrayList<Integer> numeros_int = new ArrayList<>(Arrays.asList(1, 2));

        numeros_int.add(3);

        // numeros_int.remove(Integer.valueOf(2));
        // numeros_int.remove(1);

        if (numeros_int.contains(2)) {
            System.out.println("Tem o número 2 na lista");
        } else {
            System.out.println("Não tem o número 2 na lista");
        }

        for (int i = 0; i < numeros_int.size(); i++) {
            System.out.println(numeros_int.get(i));
        }

        System.out.println(numeros_int);
        System.out.println(numeros_int.get(2));

        // Números decimais

        ArrayList<Double> numeros_decimais = new ArrayList<>(Arrays.asList(7.0, 6.5));

        numeros_decimais.add(10.0);

        // numeros_decimais.remove(Double.valueOf(10.0));
        // numeros_decimais.remove(2);

        if (numeros_decimais.contains(9.0)) {
            System.out.println("O número 9.0 está listado");
        } else {
            System.out.println("O número 9.0 não está listado");
        }

        for (int i = 0; i < numeros_decimais.size(); i++) {
            System.out.println(numeros_decimais.get(i));
        }

        System.out.println(numeros_decimais);
        System.out.println(numeros_decimais.getFirst());

        // -Lista imutável (List)-

        // Frutas

        List<String> frutas1 = List.of("Maçã", "Banana");

        if (frutas1.contains("Maçã")) {
            System.out.println("A fruta maçã está na lista");
        } else {
            System.out.println("A fruta maçã não está na lista");
        }

        for (int i = 0; i < frutas1.size(); i++) {
            System.out.println(frutas1.get(i));
        }

        System.out.println(frutas1);
        System.out.println(frutas1.getFirst());

        // -Lista mutável encadeada (LinkedList)-

        // Nomes

        LinkedList<String> nomes0 = new LinkedList<>();

        nomes0.add("José");
        nomes0.add("João");
        nomes0.add("Davi");

        // nomes0.remove("José");
        // nomes0.remove(0);

        if (nomes0.contains("João")) {
            System.out.println("O nome João está na lista");
        } else {
            System.out.println("O nome João não está na lista");
        }

        for (int i = 0; i < nomes0.size(); i++) {
            System.out.println(nomes0.get(i));
        }

        System.out.println(nomes0);
        System.out.println(nomes0.getFirst());

        // Notas

        LinkedList<Double> notas0 = new LinkedList<>();

        notas0.add(7.5);
        notas0.add(7.0);
        notas0.add(6.5);

        // notas0.remove(7.5);
        // notas0.remove(0);

        if (notas0.contains(7.5)) {
            System.out.println("O número 7.5 está na lista");
        } else {
            System.out.println("O número 7.5 não está na lista");
        }

        for (int i = 0; i < notas0.size(); i++) {
            System.out.println(notas0.get(i));
        }

        System.out.println(notas0);
        System.out.println(notas0.get(1));

        // -Dicionário/Mapa (HashMap)-

        // Alunos

        HashMap<String, Double> alunos = new HashMap<>();

        alunos.put("José", 6.0);
        alunos.put("João", 8.0);
        alunos.put("Bob", 7.0);

        // alunos.remove("Bob");

        String nomeb = "Bob";
        Double notab = alunos.get(nomeb);
        System.out.println("Nome: " + nomeb + "  " + "Nota: " + notab);

        if (alunos.containsKey("José")) {
            System.out.println("O aluno José está na lista");
        } else {
            System.out.println("O aluno José não está na lista");
        }

        if (alunos.containsValue(6.0)) {
            System.out.println("A nota 6.0 está presente na lista");
        } else {
            System.out.println("A nota 6.0 não está presente na lista");
        }

        for (Map.Entry<String, Double> alunos0 : alunos.entrySet()) { // keySet() values()
            String aluno = alunos0.getKey();
            Double nota = alunos0.getValue();
            System.out.println("Aluno: " + aluno + "  " + "Nota: " + nota);
        }

        System.out.println("Alunos: " + alunos);

        // Pessoas

        HashMap<String, Integer> pessoas = new HashMap<>();

        pessoas.put("Joel", 22);
        pessoas.put("Hermón", 25);
        pessoas.put("Jó", 28);

        // pessoas.remove("Joel");

        String nomeh = "Hermón";
        int idadeh = pessoas.get(nomeh);
        System.out.println("Nome: " + nomeh + " " + "Idade: " + idadeh);

        if (pessoas.containsKey("Josafá")) {
            System.out.println("Josafá está na lista");
        } else {
            System.out.println("Josafá não está na lista");
        }

        if (pessoas.containsValue(20)) {
            System.out.println("A idade 20 está presente");
        } else {
            System.out.println("A idade 20 não está presente");
        }

        for (Map.Entry<String, Integer> pessoas0 : pessoas.entrySet()) { // // keySet() values()
            String pessoa = pessoas0.getKey();
            Integer idade = pessoas0.getValue();
            System.out.println("Pessoa: " + pessoa + "  " + "Idade: " + idade);
        }

        System.out.println("Pessoas: " + pessoas);

        // -Dicionário/Mapa encadeado (LinkedHashMap)-

        LinkedHashMap<String, Double> alunos_notas = new LinkedHashMap<>();

        alunos_notas.put("Josafá", 7.5);
        alunos_notas.put("Joel", 9.0);
        alunos_notas.put("Jó", 8.0);

        // alunos_notas.remove("Josafá");

        String aluno = "Joel";
        double nota = alunos_notas.get(aluno);
        System.out.println("Aluno: " + aluno + "  " + "Nota: " + nota);

        if (alunos_notas.containsKey("Jó")) {
            System.out.println("O aluno Jó está na lista");
        } else {
            System.out.println("O aluno Jó não está na lista");
        }

        if (alunos_notas.containsValue(7.0)) {
            System.out.println("A nota 7.0 está presente na lista");
        } else {
            System.out.println("A nota 7.0 não está presente na lista");
        }

        for (Map.Entry<String, Double> alunos_nota : alunos_notas.entrySet()) { // keySet() values()
            String aluninho = alunos_nota.getKey();
            double notinha = alunos_nota.getValue();
            System.out.println("Aluno: " + aluninho + " " + "Nota: " + notinha);
        }

        System.out.println("Alunos (2): " + alunos_notas);

        // -Conjunto (HashSet)-

        HashSet<String> funcionarios = new HashSet<>();

        funcionarios.add("Maria");
        funcionarios.add("Maria");
        funcionarios.add("José");

        // funcionarios.remove("Maria");

        if (funcionarios.contains("José")) {
            System.out.println("O funcionário José está na lista");
        } else {
            System.out.println("O funcionário José não está na lista");
        }

        for (String funcionario : funcionarios) {
            System.out.println("Funcionário: " + funcionario);
        }

        System.out.println(funcionarios);

        // -Conjunto encadeado (LinkedHashSet)-

        LinkedHashSet<Integer> numeros = new LinkedHashSet<>();

        numeros.add(0);
        numeros.add(0);
        numeros.add(1);
        numeros.add(1);

        // numeros.remove(0);

        if (numeros.contains(0)) {
            System.out.println("O número 0 está na lista");
        } else {
            System.out.println("O número 0 não está na lista");
        }

        for (int numero : numeros) {
            System.out.println("Número: " + numero);
        }

        System.out.println(numeros);
        System.out.println(numeros.getFirst());

        // --FUNÇÕES--

        // Hello sem return

        Hello();

        // Hello com return

        String mensagem = hello();
        System.out.println(mensagem);

        // Soma

        int resultado0 = soma(5, 5);
        System.out.println(resultado0);

        // Subtração

        double resultado1 = subtracao(7.5, 2.5);
        System.out.println(resultado1);

        // Par

        int ehpar = 9;
        if (par(ehpar)) {
            System.out.println(ehpar + " é par");
        } else {
            System.out.println(ehpar + " não é par");
        }

        // Ímpar

        int ehimpar = 9;
        if (impar(ehimpar)) {
            System.out.println(ehimpar + " é ímpar");
        } else {
            System.out.println(ehimpar + " não é ímpar");
        }

        // Primo

        int ehprimo = 7;
        if (primo(ehprimo)) {
            System.out.println(ehprimo + " é primo");
        } else {
            System.out.println(ehprimo + " não é primo");
        }

        // Composto

        int ehcomposto = 7;
        if (composto(ehcomposto)) {
            System.out.println(ehcomposto + " é composto");
        } else {
            System.out.println(ehcomposto + " não é composto");
        }

        // Scanner (texto)

        //String login_nome_2 = login();
        //System.out.println(login_nome_2);

        // Scanner (número inteiro)

        //int idade_2 = idade();
        //System.out.println(idade_2);

        // Scanner (texto e número)

        //nome_idade();

        // --TRATAMENTO DE ERROS--

        // -Verificados-

        // IOException: Problemas de entrada e saída.
        // SQLException: Erros relacionados a operações em bancos de dados.
        // ClassNotFoundException: Classe não encontrada.
        // FileNotFoundException: Arquivo não encontrado.
        // ParseException: Erros ao processar (especialmente em formatação de datas).
        // InterruptedException: Interrupção de uma operação em uma thread.
        // NoSuchFieldException: Campo não encontrado em uma classe.
        // NoSuchMethodException: Método não encontrado na classe.

        // IOException

        try {
            FileReader arquivo_io = new FileReader("requirements.txt");
        } catch (IOException e) {
            System.out.println("Erro de entrada/saída em um arquivo: " + e.getMessage());
        }

        // FileNotFoundException

        try {
            FileReader arquivo_inexistente = new FileReader("requirements.txt");
        } catch (FileNotFoundException e) {
            System.out.println("Erro de arquivo não encontrado: " + e.getMessage());
        }

        // FileNotFoundException + IOException

        try {
            FileReader arquivo_io_inexistente = new FileReader("requirements.txt");
        } catch (FileNotFoundException e) {
            System.out.println("Erro de pasta ou arquivo não existente: " + e.getMessage());
        } catch (IOException e) {
            System.out.println("Erro de entrada/saída: " + e.getMessage());
        }

        // } finally {
        // System.out.println("Execução de código independente da exceção");
        // }

        // -Não Verificados-

        // ArithmeticException: Erros aritméticos (como divisão por zero).
        // NullPointerException: Tentativa de usar um objeto nulo.
        // ArrayIndexOutOfBoundsException: Acesso a um índice de array inválido.
        // ClassCastException: Tentativa de converter um objeto para um tipo inválido.
        // IllegalArgumentException: Argumento ilegal ou inadequado passado a um método.
        // IllegalStateException: Chamada de método em um estado inválido para a operação.
        // NumberFormatException: Falha ao converter uma string em um número.
        // IndexOutOfBoundsException: Acesso a um índice fora dos limites de uma lista.

        // ArithmeticException

        try {
            int divisao_por_zero = 5 / 0;
        } catch (ArithmeticException e) {
            System.out.println("Erro aritmético: " + e.getMessage());
        }

        // NullPointerException

        try {
            String nulo = null;
            System.out.println(nulo.length());
        } catch (NullPointerException e) {
            System.out.println("Erro de acesso a uma variável nula: " + e.getMessage());
        }

        // ArrayIndexOutOfBoundsException ([])

        try {
            int[] vetor = {1, 2, 3};
            System.out.println(vetor[3]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Erro de acesso a um índice inválido em uma lista []: " + e.getMessage());
        }

        // NumberFormatException

        try {
            String palavra = "Java";
            Integer palavra_numero = Integer.valueOf(palavra); // Ou Double
        } catch (NumberFormatException e) {
            System.out.println("Erro de conversão de string para um número: " + e.getMessage());
        }

        // IndexOutOfBoundsException (arraylist ou list)

        try {
            ArrayList<Integer> lista = new ArrayList<>(Arrays.asList(1, 2, 3));
            System.out.println(lista.get(3));
        } catch (IndexOutOfBoundsException e) {
            System.out.println("Erro de acesso a um índice inválido em uma lista arraylist ou list: " + e.getMessage());
        }

        // } finally {
        // System.out.println("Execução de código independente da exceção");
        // }
    }
}