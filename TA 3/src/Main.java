import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Main {
    public static void main(String[] args) {

        List<Person> personList = new ArrayList<>();
        personList.add(new Person(3, "John", 25));
        personList.add(new Person(1, "Alice", 30));
        personList.add(new Person(2, "Bob", 22));

        Person p1 = new Person(3, "John", 25);
        Person p2 = new Person(3, "John", 25);

        System.out.println(p1.equals(p2));

        System.out.println("Before sorting: " + personList);

        // Sorting by age using AgeComparator (outer class)
        Person.AgeComparator outerAgeComparator = new Person.AgeComparator();
        personList.sort(outerAgeComparator);
        System.out.println("After sorting by age using AgeComparator (outer class): " + personList);

        // Sorting by age using AgeComparator (inner class)
        Person.AgeComparator innerAgeComparator = new Person.AgeComparator();
        personList.sort(innerAgeComparator);
        System.out.println("After sorting by age using AgeComparator (inner class): " + personList);

        // Sorting by Comparator field (ageComparator)
        personList.sort(Person.ageComparator);
        System.out.println("After sorting by age using ageComparator field: " + personList);

        // Sorting by name
        personList.sort(Person.nameComparator);
        System.out.println("After sorting by name using nameComparator field: " + personList);

        // Sorting by id
        personList.sort(Person.idComparator);
        System.out.println("After sorting by id using idComparator field: " + personList);


        // Sorting by age using lambda
        personList.sort((a, b) -> a.getAge() - b.getAge());
        System.out.println("After sorting by Age using lambda: " + personList);


        // Sorting by age using Anonymous class
        Comparator<Person> AnonymousComparator = new Comparator<Person>() {
            @Override
            public int compare(Person o1, Person o2) {
                return o1.getAge() - o2.getAge();
            }
        };
        personList.sort(AnonymousComparator);
        System.out.println("After sorting by Age using Anonymous class: " + personList);



    }
}

