package Funcionario_Gerente_Peao;

public class Funcionario {
    private double pagamento;

    public Funcionario(double pagamento) {
        this.pagamento = pagamento;
    }

    public double salariopagamento(double valor) {
        if (valor > 0) {
            pagamento = valor;
            System.out.println("Pagamento mensal: " + valor);
        } else {
            System.out.println("Valor do pagamento deve ser maior que zero. Tente novamente.");
        }
        return valor;
    }

    public double getSalarioPagamento() {
        System.out.println("Pagamento mensal realizado pela última vez: " + pagamento);
        return this.pagamento;
    }

    public void setSalarioPagamento() {
        System.out.println("O valor do pagamento não pode ser alterado diretamente!");
    }
}