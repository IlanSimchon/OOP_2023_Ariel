public class Main {
    public static void main(String[] args) throws InvalidAgeException {

        // generics

        Stack<Integer> integerStack = new Stack<>();
        Stack<Person> PersonStack= new Stack<>();
        // Stack<int> intStack = new Stack<>();  // invalid!!

        integerStack.push(1);
        integerStack.push(2);
        integerStack.push(3);

        System.out.println("Popped: " + integerStack.pop()); // Popped: 3
        System.out.println("Peek: " + integerStack.peek());   // Peek: 2
        System.out.println("Size: " + integerStack.size());   // Size: 2

        integerStack.clear();
        System.out.println("Is Empty: " + integerStack.isEmpty()); // Is Empty: true

        PersonStack.push(new Person("David", 25));
        System.out.println("Is Empty: " + PersonStack.isEmpty()); // Is Empty: false

        // Exceptions

        // Creating a person object with an invalid age without using try-catch
        Person person1 = new Person("John", 150);
        System.out.println(person1);


        // Creating a person object with an invalid age using try-catch
        try {
            Person person2 = new Person("John", 150);
            System.out.println(person2);
        } catch (InvalidAgeException e) {
            System.err.println("Error: " + e.getMessage());
        }


        System.out.println("The exception did not stop the program!");
    }
}