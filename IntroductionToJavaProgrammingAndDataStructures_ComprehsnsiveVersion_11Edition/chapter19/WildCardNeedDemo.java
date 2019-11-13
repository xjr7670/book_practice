public class WildCardNeedDemo {
    public static void main(String[] args) {
        GenericStack<Integer> intStack = new GenericStack<>();
        intStack.push(1);
        intStack.push(2);
        intStack.push(-2);

        System.out.print("The max number is " + max(intStack));
    }

    /** Find the maximum in a stack of numbers */
    public static double max(GenericStack<? extends Number> stack) {
        double max = stack.pop().doublaValue();

        while (!stack.isEmpty()) {
            double value = stack.pop().doubleValue();
            if (value > max) {
                max = value;
            }
        }
        return max;
    }
}