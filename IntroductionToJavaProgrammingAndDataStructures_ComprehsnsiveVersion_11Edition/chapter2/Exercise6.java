import java.util.Scanner;

public class Exercise6 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a number between 0 and 1000: ");
        int num = scanner.nextInt();
        int quotient = num / 10;
        int remainder = num % 10;
        int sum = remainder;

        while (quotient > 0) {
            remainder = quotient % 10;
            quotient = quotient / 10;
            sum += remainder;
        }

        System.out.println("The sum of the digits is " + sum);
    }
}