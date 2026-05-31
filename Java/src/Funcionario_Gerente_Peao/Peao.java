// Pacote

package Funcionario_Gerente_Peao;

// Classe

public class Peao extends Funcionario {

    // Metódo construtor com herança dos metódos e atributos da superclasse

    public Peao(double salariopagamento) {
        super(salariopagamento);
    }

    // Polimorfismo (metódo setter salariopagamento)

    @Override
    public double salariopagamento(double valor) {
        if (valor >= 1518.0) {
            System.out.println("Pagamento mensal realizado: " + valor);
        } else {
            System.out.println("Valor do pagamento para peão deve ser igual ou maior que 1518 reais. Tente novamente.");
        }
        return valor;
    }
}