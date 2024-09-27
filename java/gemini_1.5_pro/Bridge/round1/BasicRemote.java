public class BasicRemote extends RemoteControl {
    public BasicRemote(Device device) {
        super(device);
    }

    @Override
    public void togglePower() {
        if (device != null) {
            if (device instanceof Light && ((Light) device).getBrightness() > 0) {
                device.turnOff(); // Special case: Turn off light if it's dimmed
            } else { 
                if (device instanceof Light) {
                    ((Light) device).setBrightness(50); // Reset brightness to default
                } 
                device.turnOn(); 
            }
        }
    }
}
