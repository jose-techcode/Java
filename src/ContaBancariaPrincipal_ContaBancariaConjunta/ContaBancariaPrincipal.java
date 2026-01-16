// Pacote

package ContaBancariaPrincipal_ContaBancariaConjunta;

// Classe

public class ContaBancariaPrincipal {

    // Atributo (privado)

    private double saldo;

    // Metódo Construtor

    public ContaBancariaPrincipal(String titular, double saldo) {
        this.saldo = saldo;
    }

    // Metódo Setter

    public void deposito(double valor) {
        if (valor > 0) {
            this.saldo += valor;
            System.out.println("Depósito realizado: " + valor);
        } else {
            System.out.println("Valor deve ser maior que zero. Tente novamente.");
        }
    }

    // Metódo Setter

    public void saque(double valor) {
        if (valor > 0) {
            this.saldo -= valor;
            System.out.println("Saque realizado: " + valor);
        } else {
            System.out.println("Valor deve ser maior que zero. Tente novamente.");
        }
    }

    // Metódo Getter

    public double getSaldo() {
        System.out.println("Saldo: " + this.saldo);
        return this.saldo;
    }

    // Metódo Setter (simulado)

    public void setSaldo() {
        System.out.println("Simulação: Saldo não pode ser alterado diretamente!");
    }
}