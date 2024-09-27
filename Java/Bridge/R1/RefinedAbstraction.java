public class RefinedAbstraction extends Abstraction {

    public RefinedAbstraction(Implementer implementer) {
        super(implementer);
    }

    @Override
    public void operation() {
        implementer.operationImpl();
    }
}