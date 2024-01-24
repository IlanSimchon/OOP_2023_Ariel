import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Create instances of Person
        Person person1 = new Person(1, "John", 30);
        Person person2 = new Person(2, "Jane", 25);

        // Create instances of Student
        Student student1 = new Student(3, "Alice", 20);
        student1.addGrade(90);
        student1.addGrade(85);
        student1.addGrade(95);

        Student student2 = new Student(4, "Bob", 22);
        student2.addGrade(80);
        student2.addGrade(88);
        student2.addGrade(92);

        // Create instances of Dad
        Dad dad1 = new Dad(5, "Charlie", 40, 2);
        Person dad2 = new Dad(6, "Diana", 35, 1);

        // Create a list of Person objects and add them
        List<Person> peopleList = new ArrayList<>();
        peopleList.add(person1);
        peopleList.add(person2);
        peopleList.add(student1);
        peopleList.add(student2);
        peopleList.add(dad1);
        peopleList.add(dad2);

        // Print information using for-each loop
        for (Person person : peopleList) {
            System.out.println(person);
        }


        // overloading
        // Example 1: Overloaded methods with different parameter types
        printMessage("Hello, World!"); // String argument
        printMessage(42); // int argument

        // Example 2: Overloaded methods with different number of parameters
        calculateArea(5); // Calculate area of a square
        calculateArea(3, 4); // Calculate area of a rectangle

        // Example 3: Overloaded methods with different parameter order
        displayInfo("John", 25); // String followed by int
        displayInfo(30, "Jane"); // Int followed by String

    }



    // Example 1: Overloaded methods with different parameter types
    static void printMessage(String message) {
        System.out.println("String Message: " + message);
    }

    static void printMessage(int number) {
        System.out.println("Integer Number: " + number);
    }


    // Example 2: Overloaded methods with different number of parameters
    static void calculateArea(int side) {
        System.out.println("Area of Square: " + (side * side));
    }

    static void calculateArea(int length, int width) {
        System.out.println("Area of Rectangle: " + (length * width));
    }


    // Example 3: Overloaded methods with different parameter order
    static void displayInfo(String name, int age) {
        System.out.println("Name: " + name + ", Age: " + age);
    }

    static void displayInfo(int age, String name) {
        System.out.println("Age: " + age + ", Name: " + name);
    }
}
