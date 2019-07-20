/** 练习题 11.1 */
import java.util.Scanner;

public class TestTriangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter side1: ");
        double side1 = input.nextDouble();
        System.out.print("Enter side2: ");
        double side2 = input.nextDouble();
        System.out.print("Enter side3: ");
        double side3 = input.nextDouble();
        System.out.print("Enter color: ");
        String color = input.nextLine();
        System.out.print("Enter a boolean for whether is fill: ");
        boolean filled = input.nextBoolean();

        Triangle triangle = new Triangle(side1, side2, side3);
        triangle.setColor(color);
        triangle.setFilled(filled);

        double area = triangle.getArea();
        double perimeter = triangle.getPerimeter();
        boolean isFilled = triangle.isFilled();

        System.out.println("The area of this triangle is: " + area);
        System.out.println("The perimeter of this triangle is: " + perimeter);
        System.out.println("The triangle is filled? " + isFilled);
    }
}