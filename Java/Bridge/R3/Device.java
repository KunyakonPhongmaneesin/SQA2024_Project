package Java.Bridge.R3;

// Device.java
public abstract class Device {
    protected Remote remote;

    protected Device(Remote remote) {
        this.remote = remote;
    }

    public abstract void operate();
}