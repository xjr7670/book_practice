public class TestCircleWithPrivateDataFields {
    public static void main(String[] args) {
        Tmp myCircle = new Tmp(5.0);
        System.out.println("The area of the circle of radius " + myCircle.getRadius() + " is " + myCircle.getArea());

        // Increase myCircle's radius by 10%
        myCircle.setRadius(myCircle.getRadius() * 1.1);
        System.out.println("The area of the circle of radius " + myCircle.getRadius() + " is " + myCircle.getArea());

        System.out.println("The number of the objects created is " + Circle9_8.getNumberOfObjects());
    }
}