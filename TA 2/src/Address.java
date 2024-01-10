class Address {
    private String city;
    private String street;

    public Address(String city, String street) {
        this.city = city;
        this.street = street;
    }

// copy constructor
//    public Address(Address other) {
//        this.city = other.getCity();
//        this.street = other.getStreet();
//    }

    public String getCity() {
        return city;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
}