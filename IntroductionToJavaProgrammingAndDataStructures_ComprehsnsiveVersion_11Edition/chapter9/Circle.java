public class Circle {
    double radius;

    static int numberOfObjects = 0;

    Circle() {
        radius = 1;
        numberOfObjects++;
    }

    Circle(double newRadius) {
        radius = newRadius;
        numberOfObjects++;
    }

    static int getNumberOfObjects() {
        return numberOfObjects;
    }

    double getArea() {
        return radius * radius * Math.PI;
    }
}