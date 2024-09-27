// Abstraction.java
public abstract class Abstraction {
    protected Implementer implementer;

    protected Abstraction(Implementer implementer) {
        this.implementer = implementer;
    }

    public abstract void operation();
}