import java.util.ArrayList;

public class Student {

    private String name;
    private ArrayList<Integer> grades = new ArrayList<>();

    // static fields
    private static int sumOfGrades = 0;
    private static int numOfGrades = 0;


    public Student(String name) {
        this.name = name;
    }

    public double getAverageGrade() {
        int sum = 0;
        for(int grade : grades) {
            sum += grade;
        }
        return grades.size() > 0 ? (double)sum / grades.size() : 0;
    }
    public void addGrade(int grade) {
        grades.add(grade);
        addGradeForOverall(grade);
    }

    // static methods
    public static double getOverallAverageGrade() {
        return numOfGrades > 0 ?
                (double)sumOfGrades / numOfGrades : 0;
    }

    private static void addGradeForOverall(int grade) {
        sumOfGrades += grade;
        numOfGrades++;
    }

}

