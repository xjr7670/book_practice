import java.util.Scanner;

public class Exercise20 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter balance and interest rate (e.g., 3 for 3%): ");
        String inStr = scanner.nextLine();
        Double balance = Double.valueOf(inStr.split(" ")[0]);
        Double rate = Double.valueOf(inStr.split(" ")[1]);

        Double interest = balance * (rate / 1200);

        System.out.println("The ineterest is " + interest);
    }
}