import java.util.Scanner;

public class Exercise4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number in pounds: ");
        Double pound = scanner.nextDouble();
        Double kg = pound * 0.454;
        System.out.println(pound + " pounds is " + kg + " kilograms");
    }
}