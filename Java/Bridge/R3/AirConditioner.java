package Java.Bridge.R3;

public class AirConditioner extends Device {

    public AirConditioner(Remote remote) {
        super(remote);
    }

    @Override
    public void operate() {
        System.out.print("Air Conditioner operating with remote: ");
        remote.pressButton();
    }
}