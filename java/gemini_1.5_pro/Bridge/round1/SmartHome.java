public class SmartHome {
    public static void main(String[] args) {
        // Arrange
        Light livingRoomLight = new Light();
        Speaker bedroomSpeaker = new Speaker();

        RemoteControl basicRemote1 = new BasicRemote(livingRoomLight);
        RemoteControl advancedRemote = new AdvancedRemote(bedroomSpeaker);

        // Act 
        System.out.println("---- Using Basic Remote for Light ----");
        basicRemote1.togglePower(); 
        basicRemote1.togglePower();  

        System.out.println("\n---- Using Advanced Remote for Speaker ----");
        advancedRemote.togglePower(); // Turns on
        ((AdvancedRemote) advancedRemote).volumeUp();
        ((AdvancedRemote) advancedRemote).volumeUp(); 
        advancedRemote.togglePower(); // Dims instead of turning off completely
    }
}