public interface Pet {
    public abstract void beFriendly();
    public abstract void play();
}

public class Dog extends Canine implements Pet {
    public void beFriendly() {}
    public void play() {}

    public void roam() {}
    public void eat() {}
}