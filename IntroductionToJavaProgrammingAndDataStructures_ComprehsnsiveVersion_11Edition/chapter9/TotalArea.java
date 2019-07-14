public class TotalArea {
    public static void main(String[] args) {
        Circle9_8[] circleArray;

        circleArray = createCircleArray();

        printCircleArray(circleArray);
    }

    /** Create an array of Circle objects */
    public static Circle9_8[] createCircleArray() {
        Circle9_8[] circleArray = new Circle9_8[5];

        for (int i = 0; i < circleArray.length; i++) {
            circleArray[i] = new Circle9_8(Math.random() * 100);
        }

        // Return Circle array
        return circleArray;
    }

    /** Print an array of circles and their total area */
    public static void printCircleArray(Circle9_8[] circleArray) {
        System.out.printf("%-30s%-15s\n", "Radius", "Area");
        for (int i = 0; i < circleArray.length; i++) {
            System.out.printf("%-30f%-15f\n", circleArray[i].getRadius(), circleArray[i].getArea());
        }
    }
}