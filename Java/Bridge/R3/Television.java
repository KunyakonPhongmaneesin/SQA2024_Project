package Java.Bridge.R3;

public class Television extends Device {

    public Television(Remote remote) {
        super(remote);
    }

    @Override
    public void operate() {
        System.out.print("Television operating with remote: ");
        remote.pressButton();
    }
}
