public class AdvancedRemote extends RemoteControl {
    public AdvancedRemote(Device device) {
        super(device);
    }

    @Override
    public void togglePower() {
        if (device != null) {
            if (device instanceof Light) {
                ((Light) device).setBrightness(0); // Dim light instead of turning off
            } else {
                device.turnOff(); 
            }
        }
    }

    public void volumeUp() {
        if (device instanceof Speaker) {
            ((Speaker) device).setVolume(((Speaker) device).getVolume() + 10);
        }
    }

    public void volumeDown() {
        if (device instanceof Speaker) {
            ((Speaker) device).setVolume(((Speaker) device).getVolume() - 10);
        }
    }
}
