package DevFront_DevBack_DevFull;

public class DevFull implements DevFront, DevBack {

    @Override
    public void Tela_de_sistema() {
        System.out.println("Tela de sistema web");
    }

    @Override
    public void Logica_de_sistema() {
        System.out.println("Lógica de sistema web");
    }

    public void FullStack() {
        Tela_de_sistema();
        Logica_de_sistema();
    }
}
