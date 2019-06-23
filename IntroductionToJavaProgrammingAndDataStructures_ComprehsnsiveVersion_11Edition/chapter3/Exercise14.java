import java.util.Scanner;

public class Exercise14 {
    public static void main(String[] args) {
        int number = Math.random() > 0.5? 1: 0;

        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter 0 or 1 to guess: ");
        int guess = input.nextInt();
        
        if (guess == number) {
            System.out.println("You are correct!");
        } else {
            System.out.println("You get wrong!");
        }
    }
}