import java.awt.*;
import java.util.ArrayList;
import java.util.Comparator;

class Person {
    private int id;
    private String name;
    private int age;

    // Constructor
    public Person(int id, String name, int age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    // Getters

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    // Implementing Comparators

    // Comparator for sorting by age
    public static Comparator<Person> ageComparator = Comparator.comparingInt(Person::getAge);

    // Comparator for sorting by name
    public static Comparator<Person> nameComparator = Comparator.comparing(Person::getName);

    // Comparator for sorting by id
    public static Comparator<Person> idComparator = Comparator.comparingInt(Person::getId);

    // Example of usage: sorting a list of persons


    // Override toString method
    @Override
    public String toString() {
        return "Person{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                '}';
    }


}