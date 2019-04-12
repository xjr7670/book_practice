import java.util.ArrayList;

public class Dec2Bin {
    public static void main(String[] args) {
        ArrayList<Integer> binList = new ArrayList<Integer>();
        long number = 111111111111L;
        GetBin(number, binList);
        for (int i = binList.size()-1; i >= 0; i--) {
            System.out.print(binList.get(i));
        }
    }

    public static long GetBin(long number, ArrayList<Integer> list) {
        int rest = 0;
        long shang = 0L;
        rest = (int) (number % 2);
        shang = (long) (number / 2);
        list.add(rest);
        if (shang <= 1) {
            list.add((int) shang);
            return shang;
        } else {
            return GetBin(shang, list);
        }
    }
}