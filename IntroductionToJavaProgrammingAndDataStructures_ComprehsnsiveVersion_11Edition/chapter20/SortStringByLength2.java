import java.util.Comparator;

public class SortStringByLength2 {
    public static void main(String[] args) {
        String[] cities = { "Atlanta", "Savannah", "New York", "Dallas" };
        java.util.Arrays.sort(cities, Comparator.comparing(String::length));

        for (String s : cities) {
            System.out.print(s + " ");
        }
    }
}