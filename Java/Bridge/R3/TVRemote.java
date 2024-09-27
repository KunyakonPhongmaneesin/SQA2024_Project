package Java.Bridge.R3;

public class TVRemote implements Remote {
    @Override
    public void pressButton() {
        System.out.println("TV Remote: Button pressed");
    }
}