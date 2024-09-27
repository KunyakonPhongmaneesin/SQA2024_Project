public class SUV implements Car {
    @Override
    public void unlock() {
        System.out.println("SUV unlocked.");
    }

    @Override
    public void lock() {
        System.out.println("SUV locked.");
    }

    @Override
    public void startEngine() {
        System.out.println("SUV engine started.");
    }

    @Override
    public void stopEngine() {
        System.out.println("SUV engine turned off.");
    }
}