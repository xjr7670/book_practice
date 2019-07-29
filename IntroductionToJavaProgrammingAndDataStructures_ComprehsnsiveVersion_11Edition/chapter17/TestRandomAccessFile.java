import java.io.*;

public class TestRandomAccessFile {
    public static void main(String[] args) throws IOException {
        try (
            RandomAccessFile inout = new RandomAccessFile("inout.dat", "rw");
        ) {
            // Clear the file to destroy the old contents if exists
            inout.setLength(0);

            // Write new integers to the file
            for (int i = 0; i < 200; i++) {
                inout.writeInt(i);
            }

            // Display the current length of the file
            System.out.println("Current file length if " + inout.length());

            // Retrieve the first number
            inout.seek(0);
            System.out.println("The first number is " + inout.readInt());
            
            inout.seek(1 * 4);
            System.out.println("The second number is " + inout.readInt());

            inout.seek(9 * 4);
            System.out.println("The tenth number is " + inout.readInt());

            // Modify the eleventh number
            inout.writeInt(555);

            // Append a new number
            inout.seek(inout.length());
            inout.writeInt(999);

            // Display the new length
            System.out.println("The new length is " + inout.length());

            // Retrieve the new eleventh number
            inout.seek(10 * 4);
            System.out.println("The eleventh number is " + inout.readInt());
        }
    }
}