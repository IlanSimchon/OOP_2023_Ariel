import java.util.*;

/**
 * This program demonstrates the functions of the Iterator class in Java.
 * It showcases the usage of Iterator for traversing different types of data structures.
 * Author: Ilan Simchon
 * Date: 04/09/2023
 * */
public class IteratorExample {

    public static void main(String[] args) {

        // Create an ArrayList of integers and a LinkedList of strings //
        ArrayList<Integer> intArr = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5));
        LinkedList<String> stringArr = new LinkedList<>(Arrays.asList("Noam", "David", "Maya", "Rom", "Shachar"));

        // Create iterators for both collections
        Iterator<Integer> intIter = intArr.iterator();
        Iterator<String> stringIter = stringArr.iterator();

        // Traverse the ArrayList using the hasNext and next functions
        while (intIter.hasNext()) {
            Integer nextElement = intIter.next();
            System.out.println("Next element: " + nextElement);
        }

        System.out.println();

        // Use forEachRemaining to go through the LinkedList and perform actions on each element
        // with the help of a lambda function or a reference to the function
        stringIter.forEachRemaining((element) -> {
            System.out.println("Next element: " + element);
        });
        // Another option is to give a reference to the function
        /* stringIter.forEachRemaining(System.out::println); */

        System.out.println();

        // After using the remove method of the Iterator class, check the size of IntArr
        System.out.println("IntArr size before remove method: " + intArr.size());
        intIter.remove(); // Removes the last element returned by next()
        System.out.println("IntArr size after remove method: " + intArr.size());

        System.out.println();

        // Attempt to call remove without a prior call to next
        Iterator<Integer> removeIter = intArr.iterator();
        try {
            removeIter.remove(); // This will throw an exception
        } catch (Exception ex) {
            System.out.println("Remove method can be called only once per call to next");
        }
    }
}
