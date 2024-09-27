package Java.Bridge.R3;

// Main.java
public class Main {
    public static void main(String[] args) {
        Device tv = new Television(new TVRemote());
        tv.operate();

        Device ac = new AirConditioner(new ACRemote());
        ac.operate();
    }
}
