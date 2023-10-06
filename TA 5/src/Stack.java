import java.util.ArrayList;
import java.util.EmptyStackException;
import java.util.List;

/**
 * A generic stack implementation in Java using the T keyword.
 *
 * @param <T> the type of elements stored in the stack
 */
public class Stack<T> {
    private List<T> stack;

    /**
     * Initializes an empty stack.
     */
    public Stack() {
        stack = new ArrayList<>();
    }

    /**
     * Pushes an element onto the stack.
     *
     * @param item the item to push onto the stack
     */
    public void push(T item) {
        stack.add(item);
    }

    /**
     * Pops the top element from the stack.
     *
     * @return the top element of the stack
     * @throws EmptyStackException if the stack is empty
     */
    public T pop() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        int lastIndex = stack.size() - 1;
        T poppedItem = stack.get(lastIndex);
        stack.remove(lastIndex);
        return poppedItem;
    }

    /**
     * Retrieves the top element of the stack without removing it.
     *
     * @return the top element of the stack
     * @throws EmptyStackException if the stack is empty
     */
    public T peek() {
        if (isEmpty()) {
            throw new EmptyStackException();
        }
        return stack.get(stack.size() - 1);
    }

    /**
     * Checks if the stack is empty.
     *
     * @return true if the stack is empty, false otherwise
     */
    public boolean isEmpty() {
        return stack.isEmpty();
    }

    /**
     * Returns the number of elements in the stack.
     *
     * @return the number of elements in the stack
     */
    public int size() {
        return stack.size();
    }

    /**
     * Clears all elements from the stack.
     */
    public void clear() {
        stack.clear();
    }
}
