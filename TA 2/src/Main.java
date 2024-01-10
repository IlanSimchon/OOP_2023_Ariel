import java.util.Arrays;

public class Main {
    public static void main(String[] args) {


        //  static keyword
        Student john = new Student("John");
        Student sarah = new Student("Sarah");

        john.addGrade(90);
        sarah.addGrade(95);

        john.addGrade(80);
        sarah.addGrade(88);

        double overallAverage = Student.getOverallAverageGrade();
        System.out.println("overall average: " + overallAverage);


        // encapsulation
        AccessModifiers obj = new AccessModifiers();

        // Can only access public field and method
        System.out.println(obj.publicField);
        obj.publicMethod();

        // Can access protected field and method
        System.out.println(obj.protectedField);
        obj.protectedMethod();

        // Can access default field and method
        System.out.println(obj.defaultField);
        obj.defaultMethod();

        // Create an address
        Address originalAddress = new Address("CityA", "Street1");

        // Create a person with the original address
        Person originalPerson = new Person("John", originalAddress);

        // Create a person using the shallow copy constructor
        Person shallowCopyPerson = new Person(originalPerson, false);

        // Create a person using the deep copy constructor
        Person deepCopyPerson = new Person(originalPerson, true);

        // Modify the address in the original person
        originalPerson.getAddress().setStreet("Street2");

        // Print information
        System.out.println("Original Person: " + originalPerson.getName() + ", " + originalPerson.getAddress().getStreet());
        System.out.println("Shallow Copy Person: " + shallowCopyPerson.getName() + ", " + shallowCopyPerson.getAddress().getStreet());
        System.out.println("Deep Copy Person: " + deepCopyPerson.getName() + ", " + deepCopyPerson.getAddress().getStreet());


        // arrays
        int[] original = {0,1,2,3,4};

        // shallow copy
        int[] ShallowCopy = original;

        // deep copy
        int[] deepCopy = new int[original.length];
        for (int i = 0; i < deepCopy.length; i++) {
            deepCopy[i] = original[i];
        }

        // update original
        for (int i = 4; i > 0 ; i--) {
            original[i] = i;
        }

        System.out.println("original: " + Arrays.toString(original));
        System.out.println("shallow: " + Arrays.toString(ShallowCopy));
        System.out.println("deep: "+ Arrays.toString(deepCopy));
    }
}
