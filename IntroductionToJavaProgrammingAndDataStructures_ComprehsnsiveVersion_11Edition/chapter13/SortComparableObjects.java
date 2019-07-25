import java.math.*;

public class SortComparableObjects {
    public static void main(String[] args) {
        String[] cities = {"Savannah", "Boston", "Atlanta", "Tampa"};
        java.util.Arrays.sort(cities);
        for (String city: cities) {
            System.out.print(city + " ");
        }

        System.out.println();

        BigInteger[] hugeNumbers = {new BigInteger("23232323233131399133"),
                                    new BigInteger("351531413543151345"),
                                    new BigInteger("4311531513453451")};
        java.util.Arrays.sort(hugeNumbers);
        for (BigInteger number: hugeNumbers) {
            System.out.println(number + " ");
        }
    }
}