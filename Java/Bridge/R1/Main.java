package Java.Bridge.R1;

public class Main {
    public static void main(String[] args) {
        Implementer implementerA = new ConcreteImplementerA();
        Abstraction abstractionA = new RefinedAbstraction(implementerA);
        abstractionA.operation();

        Implementer implementerB = new ConcreteImplementerB();
        Abstraction abstractionB = new RefinedAbstraction(implementerB);
        abstractionB.operation();
    }
}
