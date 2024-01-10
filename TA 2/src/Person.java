class Person {
    private String name;
    private Address address;

    public Person(String name, Address address) {
        this.name = name;
        this.address = address;
    }

//    // Shallow copy constructor
//    public Person(Person original) {
//        this.name = original.name;
//        this.address = original.address; // Shallow copy - both Person objects reference the same Address object
//    }

    // Deep copy constructor
    public Person(Person original, boolean deepCopy) {
        this.name = original.name;

        // deep or shallow
        if (deepCopy) {
            this.address = new Address(original.address.getCity(), original.address.getStreet());
            // this.address = new Address(original.address); // if there is copy constructor
        }
        else {
            this.address = original.address; // Shallow copy
        }
    }
    public String getName() {
        return name;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }
}