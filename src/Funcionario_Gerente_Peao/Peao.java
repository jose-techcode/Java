package Funcionario_Gerente_Peao;

public class Peao extends Funcionario {

    public Peao(double salariopagamento) {
        super(salariopagamento);
    }

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