public class IntegerMatrix extends GenericMatrix<Integer> {
    /** Add two integers */
    @Override
    protected Integer add(Integer o1, Integer o2) {
        return o1 + o2;
    }

    /** Multiply tow integers */
    @Override
    protected Integer multiply(Integer o1, Integer o2) {
        return o1 * o2;
    }

    /** Specify zero for an integer */
    @Override
    protected Integer zero() {
        return 0;
    }
}