import java.util.Scanner;

public class Exercise12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter speed and acceleration: ");
        String inStr = scanner.nextLine();
        Double speed = Double.valueOf(inStr.split(" ")[0]);
        Double acceleration = Double.valueOf(inStr.split(" ")[1]);

        Double minRunway = Math.pow(speed, 2) / (2 * acceleration);
        System.out.println("The mininum runway length for this airplane is " + minRunway);
    }
}