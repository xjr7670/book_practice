public class TestRegularPolygen {
    public static void main(String[] args) {
        RegularPolygen polygen1 = new RegularPolygen(6, 4);
        RegularPolygen polygen2 = new RegularPolygen(10, 4, 5.6, 7.8);

        System.out.printf("polygen1 的周长是：%-10.4f，面积是：%-10.4f\n", polygen1.getPerimeter(), polygen1.getArea());
        System.out.printf("polygen2 的周长是：%-10.4f，面积是：%-10.4f\n", polygen2.getPerimeter(), polygen2.getArea());
    }
}