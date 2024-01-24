class Dad extends Person {
    private int numberOfChildren;

    // Constructor
    public Dad(int id, String name, int age, int numberOfChildren) {
        super(id, name, age);
        this.numberOfChildren = numberOfChildren;
    }

    // Get the number of children
    public int getNumberOfChildren() {
        return numberOfChildren;
    }

    // Override toString method
    @Override
    public String toString() {
        return super.toString() + ", numberOfChildren=" + numberOfChildren;
    }
}

