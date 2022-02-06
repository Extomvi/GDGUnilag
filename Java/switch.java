/* Using a Switch statement in Java */

public class Test {
    public static void main(String[] args) {
        // char grade = args[0].charAt(0);
        char grade = 'C';

        switch (grade) {
            case 'A':
                System.out.print("Excellent Score");
                break;
            case 'B':
            case 'C':
                System.out.print("Well done");
                break;
            case 'D':
                System.out.print("You passed");
                break;
            case 'E':
                System.out.print("You scaled through");
                break;
            case 'F':
                System.out.print("Better try harder next time");
                break;        
            default:
                System.out.print("Invalid grade");
        }
        System.out.println("Your grade is " + grade);
    }
}