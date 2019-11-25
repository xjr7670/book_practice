import java.util.Set;
import java.util.HashSet;

public class ReviewQuestion21_2_6 {
    public static void main(String[] args) {
        Set<String> set1 = new HashSet<>();
        Set<String> set2 = new HashSet<>();
        set1.add("red");
        set1.add("yellow");
        set1.add("green");
        set2.add("red");
        set2.add("yellow");
        set2.add("blue");
        set1.clear();
        System.out.println(set1);
        System.out.println(set2);
    }
}