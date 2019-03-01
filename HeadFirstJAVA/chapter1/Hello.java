public class Hello {
    public static void main(String[] args) {
        int x = 1;
        System.out.println("Out of Loop");
        while (x < 4) {
            System.out.println("In the Loop");
            System.out.println("The Value of x is: " + x);
            x = x + 1;
        }
        System.out.println("After the Loop");
    }
}