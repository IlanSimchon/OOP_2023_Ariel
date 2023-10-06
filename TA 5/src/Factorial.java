/**
 * The Factorial class provides a utility for calculating the factorial of a non-negative integer.
 * The factorial of a non-negative integer 'x' is the product of all positive integers less than
 * or equal to 'x'.
 */
public class Factorial {

    /**
     * Calculates the factorial of a non-negative integer 'x'.
     *
     * @param x The non-negative integer for which the factorial is calculated.
     * @return The factorial of 'x'.
     * @throws IllegalArgumentException If 'x' is a negative number, or if the factorial
     *                                  calculation exceeds the range of the 'long' data type.
     */
    public static long factorial(int x) {
        if (x < 0) {
            throw new IllegalArgumentException("Factorial is not defined for negative numbers.");
        }

        if (x > 20) {
            throw new IllegalArgumentException("Factorial calculation exceeds the long data type's range.");
        }

        if (x == 0 || x == 1)
            return 1;
        return x * factorial(x - 1);
    }
}
