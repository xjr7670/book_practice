import java.util.Scanner;

public class ComputeFactorial {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a nonegative integer: ");
        int n = input.nextInt();

        // Display factorial
        System.out.println("Factorial of " + n + " is " + factorial(n));
    }

    /** Return the fatorial for the specified number */
    public static long factorial(int n) {
        if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }
}