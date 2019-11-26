import java.util.LinkedHashSet;
import java.util.Collections;
import java.util.Set;

public class Practice21_1 {
    public static void main(String[] args) {
        Set<String> set1 = new LinkedHashSet<>();
        Set<String> set2 = new LinkedHashSet<>();
        
        set1.add("George");
        set1.add("Jim");
        set1.add("John");
        set1.add("Blake");
        set1.add("Kevin");
        set1.add("Michael");

        set2.add("George");
        set2.add("Katie");
        set2.add("Kevin");
        set2.add("Michelle");
        set2.add("Ryan");

        Set<String> crossSet = new LinkedHashSet<>();
        crossSet.addAll(set1);
        crossSet.retainAll(set2);
        System.out.println("交集：" + crossSet);

        Set<String> subtractSet = new LinkedHashSet<>();
        subtractSet.addAll(set1);
        subtractSet.removeAll(set2);
        System.out.println("差集：" + subtractSet);

        Set<String> combineSet = new LinkedHashSet<>();
        combineSet.addAll(set1);
        combineSet.addAll(set2);
        System.out.println("并集：" + combineSet);
    }
}