package Funcionario_Gerente_Peao;

public class Gerente extends Funcionario {

    public Gerente(double salariopagamento) {
        super(salariopagamento);
    }

    @Override
    public double salariopagamento(double valor) {
        if (valor >= 5000) {
            System.out.println("Pagamento mensal realizado: " + valor);
        } else {
            System.out.println("Valor do pagamento deve ser igual ou maior que 5000 para gerente. Tente novamente.");
        }
        return valor;
    }

}
