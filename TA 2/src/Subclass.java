public class Subclass extends AccessModifiers {

    public void test() {
        // Can access public field and method
        System.out.println(publicField);
        publicMethod();

        // Cannot access private field and method


        // Can access protected field and method
        System.out.println(protectedField);
        protectedMethod();

        // Can access default field and method
        System.out.println(defaultField);
        defaultMethod();
    }

}
