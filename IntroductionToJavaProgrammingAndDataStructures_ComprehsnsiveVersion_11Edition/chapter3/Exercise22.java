import java.util.Scanner;

public class Exercise22 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter a point like 3,4: ");
        String inStr = input.nextLine();

        int number1 = Integer.valueOf(inStr.split(",")[0]);
        int number2 = Integer.valueOf(inStr.split(",")[1]);

        double dist = Math.sqrt(number1 * number1 + number2 * number2);
        if (dist <= 10) {
            System.out.println("yes");
        } else {
            System.out.println("no");
        }
    }
}