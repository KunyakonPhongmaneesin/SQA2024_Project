public class Speaker implements Device {
    private boolean isOn = false;
    private int volume = 50; // 0-100

    @Override
    public void turnOn() {
        isOn = true;
        System.out.println("Speaker is ON");
    }

    @Override
    public void turnOff() {
        isOn = false;
        System.out.println("Speaker is OFF");
    }

    public void setVolume(int level) {
        volume = Math.max(0, Math.min(level, 100));
        System.out.println("Speaker volume set to: " + volume + "%");
    }

    public int getVolume() {
        return volume;
    }
}