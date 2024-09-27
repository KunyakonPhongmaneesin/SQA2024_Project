public class BasicRemote extends RemoteControl {

    public BasicRemote(Car car) {
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
}
