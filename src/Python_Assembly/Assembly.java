package Python_Assembly;

public class Assembly extends Python {

    @Override
    public void Gerenciamento_de_registradores() {
        System.out.println("Registradores de 8, 16, 32 e 64 bits");
    }

    @Override
    public void Gerenciamento_de_memoria() {
        System.out.println("Malloc, Calloc, Realloc, Free, Garbage Collector (GC)");
    }
}
