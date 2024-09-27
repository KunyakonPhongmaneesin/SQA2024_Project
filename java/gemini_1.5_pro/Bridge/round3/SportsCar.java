public class SportsCar implements Car {
    @Override
    public void unlock() {
        System.out.println("Sports car unlocked.");
    }

    @Override
    public void lock() {
        System.out.println("Sports car locked.");
    }

    @Override
    public void startEngine() {
        System.out.println("Sports car engine roaring to life!");
    }

    @Override
    public void stopEngine() {
        System.out.println("Sports car engine turned off.");
    }

    public void engageBoost() {
        System.out.println("Engaging boost! Zoom zoom!");
    }
}