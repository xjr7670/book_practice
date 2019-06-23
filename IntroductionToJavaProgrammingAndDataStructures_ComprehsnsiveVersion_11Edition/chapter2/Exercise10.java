import java.util.Scanner;

public class Exercise10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the amount of water in kilograms: ");
        Double amount = scanner.nextDouble();
        System.out.print("Enter the initial temperature: ");
        Double initTemp = scanner.nextDouble();
        System.out.print("Enter the final temperature: ");
        Double finalTemp = scanner.nextDouble();

        Double energy = amount * (finalTemp - initTemp) * 4184;

        System.out.println("The energy needed is " + energy);
    }
}