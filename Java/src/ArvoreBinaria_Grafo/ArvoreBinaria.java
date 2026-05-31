package ArvoreBinaria_Grafo;

public class ArvoreBinaria {

    private Node raiz;

    public ArvoreBinaria() {
        this.raiz = null;
    }

    public void inserir(int valor) {
        raiz = inserirRecursivamente(raiz, valor);
    }

    public Node inserirRecursivamente(Node atual, int valor) {
        if (atual == null) {
            return new Node(valor);
        }
        if (valor < atual.valor) {
            atual.esquerda = inserirRecursivamente(atual.esquerda, valor);
        } else if (valor > atual.valor) {
            atual.direita = inserirRecursivamente(atual.direita, valor);
        }
        return atual;
    }

    public void percorrer() {
        percorrerRecursivamente(raiz);
    }

    public void percorrerRecursivamente(Node atual) {
        if (atual != null) {
            percorrerRecursivamente(atual.esquerda);
            System.out.print(atual.valor + " ");
            percorrerRecursivamente(atual.direita);
        }
    }

}
