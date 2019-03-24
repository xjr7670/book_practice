import java.util.ArrayList;
public class UseArrayList {
    public static void main(String[] args) {
        ArrayList<String> arr = new ArrayList<String>();
        arr.add(new String("String1"));
        arr.add(new String("String2"));
        System.out.println(arr.get(1));
        System.out.println(arr.size());
    }
}