package ContaBancariaPrincipal_ContaBancariaConjunta;

public class ContaBancariaPrincipal {
    private double saldo;

    public ContaBancariaPrincipal(String titular, double saldo) {
        this.saldo = saldo;
    }

    public void deposito(double valor) {
        if (valor > 0) {
            this.saldo += valor;
            System.out.println("Depósito realizado: " + valor);
        } else {
            System.out.println("Valor deve ser maior que zero. Tente novamente.");
        }
    }

    public void saque(double valor) {
        if (valor > 0) {
            this.saldo -= valor;
            System.out.println("Saque realizado: " + valor);
        } else {
            System.out.println("Valor deve ser maior que zero. Tente novamente.");
        }
    }

    public double getSaldo() {
        System.out.println("Saldo: " + this.saldo);
        return this.saldo;
    }

    public void setSaldo() {
        System.out.println("Saldo não pode ser alterado diretamente!");
    }
}