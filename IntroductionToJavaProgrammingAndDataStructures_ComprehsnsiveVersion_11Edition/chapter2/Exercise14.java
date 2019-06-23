import java.util.Scanner;

public class Exercise14 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter weight in pounds: ");
        Double weight = scanner.nextDouble();
        System.out.print("Enter height in inches: ");
        Double height = scanner.nextDouble();

        Double weightKG = weight * 0.45359237;
        Double heightM = height * 0.0254;
        Double bmi = weightKG / (heightM * heightM);
        
        System.out.println("BMI is " + bmi);
    }
}