import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertNotEquals;

public class PointTest {

    @Test
    public void testConstructorAndGetters() {
        Point point = new Point(3.0, 4.0);
        assertEquals(3.0, point.getX(), 0.0001);
        assertEquals(4.0, point.getY(), 0.0001);
    }

    @Test
    public void testDistanceTo() {
        Point point1 = new Point(1.0, 2.0);
        Point point2 = new Point(4.0, 6.0);
        assertEquals(5.0, point1.distanceTo(point2), 0.0001);
    }

    @Test
    public void testEquals() {
        Point point1 = new Point(2.0, 3.0);
        Point point2 = new Point(2.0, 3.0);
        Point point3 = new Point(3.0, 4.0);

        assertTrue(point1.equals(point2));
        assertFalse(point1.equals(point3));
    }

    @Test
    public void testToString() {
        Point point = new Point(2.5, 3.5);
        assertEquals("(2.5, 3.5)", point.toString());
    }

    @Test
    public void testNegativeCoordinates() {
        Point point = new Point(-2.0, -3.0);
        assertEquals(-2.0, point.getX(), 0.0001);
        assertEquals(-3.0, point.getY(), 0.0001);
    }

    @Test
    public void testZeroCoordinates() {
        Point point = new Point(0.0, 0.0);
        assertEquals(0.0, point.getX());
        assertEquals(0.0, point.getY());

        assertEquals(0.0, point.getX(), 0.0001);
        assertEquals(0.0, point.getY(), 0.0001);
    }

    @Test
    public void testDistanceToSelf() {
        Point point1 = new Point(2.0, 3.0);
        assertEquals(0.0, point1.distanceTo(point1), 0.0001);
    }

    @Test
    public void testDistanceToNegativeCoordinates() {
        Point point1 = new Point(1.0, 1.0);
        Point point2 = new Point(-2.0, -3.0);
        assertEquals(5.0, point1.distanceTo(point2), 0.0001);
    }

    @Test
    public void testDistanceToZeroCoordinates() {
        Point point1 = new Point(1.0, 1.0);
        Point point2 = new Point(0.0, 0.0);
        assertEquals(Math.sqrt(2.0), point1.distanceTo(point2), 0.0001);
    }

    @Test
    public void testEqualsWithSelf() {
        Point point1 = new Point(2.0, 3.0);
        assertTrue(point1.equals(point1));
    }

    @Test
    public void testEqualsWithNull() {
        Point point1 = new Point(2.0, 3.0);
        assertFalse(point1.equals(null));
    }

    @Test
    public void testEqualsWithDifferentClass() {
        Point point1 = new Point(2.0, 3.0);
        assertFalse(point1.equals("NotAPoint"));
    }

}

