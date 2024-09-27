public class Light implements Device {
    private boolean isOn = false;
    private int brightness = 50; // 0-100

    @Override
    public void turnOn() {
        isOn = true;
        System.out.println("Light is ON");
    }

    @Override
    public void turnOff() {
        isOn = false;
        System.out.println("Light is OFF");
    }

    public void setBrightness(int level) {
        brightness = Math.max(0, Math.min(level, 100)); 
        System.out.println("Light brightness set to: " + brightness + "%");
    }

    public int getBrightness() {
        return brightness;
    }
}