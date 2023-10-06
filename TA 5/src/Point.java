/**
 * The Point class represents a point in 2D space with x and y coordinates.
 */
public class Point {
    private double x;
    private double y;

    /**
     * Constructs a Point object with the specified x and y coordinates.
     *
     * @param x The x-coordinate of the point.
     * @param y The y-coordinate of the point.
     */
    public Point(double x, double y) {
        this.x = x;
        this.y = y;
    }

    /**
     * Gets the x-coordinate of the point.
     *
     * @return The x-coordinate.
     */
    public double getX() {
        return x;
    }

    /**
     * Gets the y-coordinate of the point.
     *
     * @return The y-coordinate.
     */
    public double getY() {
        return y;
    }

    /**
     * Calculates the distance between this point and another point.
     *
     * @param otherPoint The other point to calculate the distance to.
     * @return The distance between this point and the other point.
     */
    public double distanceTo(Point otherPoint) {
        double dx = this.x - otherPoint.x;
        double dy = this.y - otherPoint.y;
        return Math.sqrt(dx * dx + dy * dy);
    }

    /**
     * Checks if this point is equal to another point.
     *
     * @param otherPoint The other point to compare with.
     * @return true if the points are equal (have the same x and y coordinates), false otherwise.
     */
    public boolean equals(Point otherPoint) {
        if (this == otherPoint) {
            return true;
        }
        if (otherPoint == null || getClass() != otherPoint.getClass()) {
            return false;
        }
        return Double.compare(otherPoint.x, x) == 0 && Double.compare(otherPoint.y, y) == 0;    }

    /**
     * Returns a string representation of the point.
     *
     * @return A string in the format "(x, y)".
     */
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }

}