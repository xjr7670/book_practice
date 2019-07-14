public class TestRectangle {
    public static void main(String[] args) {
        Rectangle rectangle1 = new Rectangle(4, 40);
        Rectangle rectangle2 = new Rectangle(3.5, 35.9);
    
        System.out.println(rectangle1.width + " " + rectangle1.height + " " + rectangle1.getArea() + " " + rectangle1.getPerimeter());
        System.out.println(rectangle2.width + " " + rectangle2.height + " " + rectangle2.getArea() + " " + rectangle2.getPerimeter());
    }
}