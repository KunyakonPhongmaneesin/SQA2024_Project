public class CarTestDrive {
    public static void main(String[] args) {
        // Arrange
        Car sportsCar = new SportsCar();
        RemoteControl sportsCarRemote = new SportsCarRemote(sportsCar);

        Car suv = new SUV();
        RemoteControl basicRemote = new BasicRemote(suv);

        // Act & Assert (Implicit - Using console output for demo)
        System.out.println("--- Controlling Sports Car ---");
        sportsCarRemote.pressUnlockButton();
        sportsCarRemote.pressStartButton();
        ((SportsCarRemote) sportsCarRemote).pressBoostButton();
        sportsCarRemote.pressStopButton();
        sportsCarRemote.pressLockButton();

        System.out.println("\n--- Controlling SUV ---");
        basicRemote.pressUnlockButton();
        basicRemote.pressStartButton();
        basicRemote.pressStopButton();
        basicRemote.pressLockButton();
    }
}