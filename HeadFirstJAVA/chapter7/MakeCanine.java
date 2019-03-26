abstract public class Canine extends Animal {
    public void roam() {}
}

public class MakeCanine {
    public void go() {
        Canine c;
        c = new Dog();
        c = new Canine();
        c.roam();
    }
}

