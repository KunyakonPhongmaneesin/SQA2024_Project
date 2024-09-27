// Target.java
interface Target {
    void request();
}

// Adaptee.java
class Adaptee {
    public void specificRequest() {
        System.out.println("Called specificRequest()");
    }
}

// Adapter.java
class Adapter implements Target {
    private Adaptee adaptee;

    public Adapter(Adaptee adaptee) {
        this.adaptee = adaptee;
    }

    @Override
    public void request() {
        adaptee.specificRequest();
    }
}