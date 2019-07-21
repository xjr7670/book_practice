public class ReviewQuestion_12_11_5 {
    public static void main(String[] args) throws Exception {
        java.io.File file = new java.io.File("noExist.txt");
        try (
            java.io.PrintWriter output = new java.io.PrintWriter(file);
        ) {
            output.println("line one");
        }
    }
}