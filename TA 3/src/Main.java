import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;

public class Main{
    public static void main(String[] args) {
        ArrayList<Person> personList = new ArrayList<>();
        personList.add(new Person(3, "John", 25));
        personList.add(new Person(1, "Alice", 30));
        personList.add(new Person(2, "Bob", 22));

        System.out.println("Before sorting: " + personList);

        // Sorting by age
        personList.sort(Person.ageComparator);
        System.out.println("After sorting by age: " + personList.toString());

        // Sorting by name
        personList.sort(Person.nameComparator);
        System.out.println("After sorting by name: " + personList);

        // Sorting by id
        personList.sort(Person.idComparator);
        System.out.println("After sorting by id: " + personList);
    }
}

