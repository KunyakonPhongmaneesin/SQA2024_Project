package Java.Bridge.R3;

public class ACRemote implements Remote {
    @Override
    public void pressButton() {
        System.out.println("AC Remote: Button pressed");
    }
}