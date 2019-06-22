import java.util.Scanner;

public class Exercise2 {
    public static void main(String[] args) {

        final double PI = 3.1415926;

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the radius and length of a cylinder: ");
        String inputStr = scanner.nextLine().trim();
        String[] input = inputStr.split(" ");
        double radius = Double.valueOf(input[0]);
        double length = Double.valueOf(input[1]);

        double area = radius * radius * PI;
        double volume = area * length;

        System.out.println("The area is " + area);
        System.out.println("The volume is " + volume);
    }
}