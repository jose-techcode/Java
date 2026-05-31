package ArvoreBinaria_Grafo;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Grafo {
    private final Map<Integer, List<Integer>> grafo;

    public Grafo() {
        this.grafo = new HashMap<>();
    }

    public void adicionarVertice(int vertice) {
        grafo.putIfAbsent(vertice, new ArrayList<>());
    }

    public void adicionarArestaNaoOrientada(int a, int b) {
        adicionarVertice(a);
        adicionarVertice(b);
        grafo.get(a).add(b);
        grafo.get(b).add(a);
    }

    public void adicionarArestaOrientada(int a, int b) {
        adicionarVertice(a);
        adicionarVertice(b);
        grafo.get(a).add(b);
    }

    public void ver() {
        for (Map.Entry<Integer, List<Integer>> entry : grafo.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
