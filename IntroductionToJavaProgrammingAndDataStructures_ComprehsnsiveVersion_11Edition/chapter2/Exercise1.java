import java.util.Scanner;

public class Exercise1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a degree in Celsius: ");
        double degree = scanner.nextDouble();
        double fah = 9.0 / 5 * degree + 32;
        System.out.println(degree + " Celsius is " + fah + " Fahrenheit");
    }
}