import java.util.Scanner;

public class Exercise12 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter an integer number with 3 digits: ");
        int number = Math.abs(input.nextInt());
        
        int firstNum = number / 100;
        int thirdNum = number % 10;

        if (firstNum == thirdNum) {
            System.out.println(number + " is a palindrome");
        } else {
            System.out.println(number + " is not a palindrome");
        }
    }
}