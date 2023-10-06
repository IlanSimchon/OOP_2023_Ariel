 import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

    public class FactorialTest {

        @Test
        public void testFactorialWithZero() {
            assertEquals(1, Factorial.factorial(0));
        }

        @Test
        public void testFactorialWithPositiveNumbers() {
            assertEquals(1, Factorial.factorial(1));
            assertEquals(2, Factorial.factorial(2));
            assertEquals(6, Factorial.factorial(3));
            assertEquals(24, Factorial.factorial(4));
            assertEquals(120, Factorial.factorial(5));
            assertEquals(720, Factorial.factorial(6));
            // Add more positive number test cases as needed
        }

        @Test
        public void testFactorialWithNegativeNumber() {
            // Factorial of a negative number is not defined, so you can check for an exception
            assertThrows(IllegalArgumentException.class, () -> Factorial.factorial(-1));
            assertThrows(IllegalArgumentException.class, () -> Factorial.factorial(-10));
        }

        @Test
        public void testFactorialWithLargeNumber() {
            // Test with a large positive number (e.g., 20)
            assertEquals(2432902008176640000L, Factorial.factorial(20));
            // You can add more tests with even larger numbers if needed
        }

        @Test
        public void testFactorialWithOne() {
            // Factorial of 1 is 1
            assertEquals(1, Factorial.factorial(1));
        }

        @Test
        public void testFactorialWithMaxValue() {
            // Test with the maximum positive integer value (2,147,483,647)
            // This will test the function's ability to handle large numbers and potential overflows
            assertThrows(IllegalArgumentException.class, () -> Factorial.factorial(Integer.MAX_VALUE));
        }
    }


