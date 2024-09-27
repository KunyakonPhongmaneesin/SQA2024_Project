public class SportsCarRemote extends RemoteControl {
    public SportsCarRemote(Car car) {
        super(car);
    }

    @Override
    public void pressUnlockButton() {
        car.unlock();
    }

    @Override
    public void pressLockButton() {
        car.lock();
    }

    @Override
    public void pressStartButton() {
        car.startEngine();
    }

    @Override
    public void pressStopButton() {
        car.stopEngine();
    }

    public void pressBoostButton() {
        // Only available for SportsCar
        if (car instanceof SportsCar) {
            ((SportsCar) car).engageBoost(); 
        }
    }
}