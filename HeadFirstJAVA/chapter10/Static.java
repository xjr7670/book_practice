public class Static {
    static int size = 10;
    public static void main(String[] args) {
        Static s = new Static();
        s.func();
    }

    public void func() {
        System.out.println(size);
    }
}