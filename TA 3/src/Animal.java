public abstract class Animal {
    // Concrete method
    public void eat() {
        System.out.println("Animal is eating.");
    }
    // Abstract method
    public abstract void makeSound();
}

// Concrete class - Dog
class Dog extends Animal {
    // Implementation of the abstract method
    @Override
    public void makeSound() {
        System.out.println("Dog barks.");
    }

    // Additional method specific to Dog
    public void wagTail() {
        System.out.println("Dog is wagging its tail.");
    }
}

// Concrete class - Cat
class Cat extends Animal {
    // Implementation of the abstract method
    @Override
    public void makeSound() {
        System.out.println("Cat meows.");
    }

    // Additional method specific to Cat
    public void purr() {
        System.out.println("Cat is purring.");
    }



    public static void main(String[] args) {
        // Creating instances of Dog and Cat
        Dog dog = new Dog();
        Cat cat = new Cat();

        // Calling methods on the objects
        dog.eat();  // Inherited from Animal
        dog.makeSound();  // Overridden in Dog
        dog.wagTail();  // Specific to Dog

        System.out.println();

        cat.eat();  // Inherited from Animal
        cat.makeSound();  // Overridden in Cat
        cat.purr();  // Specific to Cat
    }
}
