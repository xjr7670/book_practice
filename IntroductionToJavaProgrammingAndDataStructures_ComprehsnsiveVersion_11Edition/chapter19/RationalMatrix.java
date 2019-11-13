public class RationalMatrix extends GenericMatrix<Rational> {
    /** Add two rational numbers */
    @Override
    protected Rational add(Rational r1, Rational r2) {
        return r1.add(r2);
    }

    /** Multiply two rational numbers */
    @Override
    protected Rational multiply(Rational r1, Rational r2) {
        return r1.multiply(r2);
    }

    /** Specify zero for a Rational number */
    @Override
    protected Rational zero() {
        return new Rational(0, 1);
    }
}