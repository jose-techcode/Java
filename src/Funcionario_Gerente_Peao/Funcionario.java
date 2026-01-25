// Pacote

package Funcionario_Gerente_Peao;

// Polimorfismo com herança única: classe. Polimorfismo com herança múltipla: interface.

public class Funcionario {

    // Atributo (privado)

    private double pagamento;

    // Metódo construtor

    public Funcionario(double pagamento) {
        this.pagamento = pagamento;
    }

    // Metódo setter

    public double salariopagamento(double valor) {
        if (valor > 0) {
            pagamento = valor;
            System.out.println("Pagamento mensal realizado: " + valor);
        } else {
            System.out.println("Valor do pagamento deve ser maior que zero. Tente novamente.");
        }
        return valor;
    }

    // Metódo getter

    public double getSalarioPagamento() {
        System.out.println("Pagamento mensal padrão: " + this.pagamento);
        return this.pagamento;
    }

    // Metódo setter (simulado)

    public void setSalarioPagamento() {
        System.out.println("Simulação: O valor do pagamento não pode ser alterado diretamente!");
    }
}