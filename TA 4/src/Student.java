import java.util.ArrayList;
import java.util.List;

class Student extends Person {
    private List<Integer> grades;

    // Constructor
    public Student(int id, String name, int age) {
        super(id, name, age);
        this.grades = new ArrayList<>();
    }

    // Add grades to the list
    public void addGrade(int grade) {
        grades.add(grade);
    }

    // Calculate and return the average of grades
    public double getAverage() {
        if (grades.isEmpty()) {
            return 0.0;
        }

        int sum = 0;
        for (int grade : grades) {
            sum += grade;
        }

        return (double) sum / grades.size();
    }

    // Override toString method
    @Override
    public String toString() {
        return super.toString() + ", grades=" + grades + ", average=" + getAverage();
    }
}