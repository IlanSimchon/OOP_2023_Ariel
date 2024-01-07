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

    }
}
