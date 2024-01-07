
public class AccessModifiers {

    // Private field - only accessible within class
    private String privateField = "private";

    // Public field
    public String publicField = "public";

    // Protected field
    protected String protectedField = "protected";

    // Default field
    String defaultField = "default";

    // Private method - only accessible within class
    private void privateMethod() {
        System.out.println(privateField + " method");
    }

    // Public method
    public void publicMethod() {
        System.out.println(publicField + " method");
    }

    // Protected method
    protected void protectedMethod() {
        System.out.println(protectedField + " method");
    }

    // Default method
    void defaultMethod() {
        System.out.println(defaultField + " method");
    }

}

