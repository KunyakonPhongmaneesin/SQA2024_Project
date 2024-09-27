public abstract class RemoteControl {
    protected Car car;

    public RemoteControl(Car car) {
        this.car = car;
    }

    public abstract void pressUnlockButton();
    public abstract void pressLockButton();
    public abstract void pressStartButton();
    public abstract void pressStopButton();
}
