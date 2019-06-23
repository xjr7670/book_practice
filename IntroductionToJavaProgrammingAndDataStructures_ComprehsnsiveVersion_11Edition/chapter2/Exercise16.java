import java.util.Scanner;

public class Exercise16 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the length of the side: ");
        Double sideLength = scanner.nextDouble();
        
        Double area = 3 * Math.sqrt(3) / 2 * Math.pow(sideLength, 2);
        
        System.out.println("The area of the hexagon is " + area);
    }
}