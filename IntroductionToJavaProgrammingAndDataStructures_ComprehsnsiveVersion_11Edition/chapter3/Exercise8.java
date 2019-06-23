import java.util.Scanner;

public class Exercise8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int temp;
        System.out.print("Enter number1: ");
        int number1 = input.nextInt();
        System.out.print("Enter number2: ");
        int number2 = input.nextInt();
        System.out.print("Enter number3: ");
        int number3 = input.nextInt();

        if (number1 < number2) {
            temp = number1;
            number1 = number2;
            number2 = temp;
            if (number3 > number1) {
                System.out.println(number3);
                System.out.println(number1);
                System.out.println(number2);
            } else if (number3 < number2) {
                System.out.println(number1);
                System.out.println(number2);
                System.out.println(number3);
            } else {
                System.out.println(number1);
                System.out.println(number3);
                System.out.println(number2);
            }
        }
    }
}