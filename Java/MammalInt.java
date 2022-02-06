/* Implementing an Interface */
// Takes from Animals.java file

public class MammalInt implements Animal {
    public void eat(){
        System.out.println("Mammals eat");
    }

    public void travel() {
        System.out.println("Mammals travel");
    }

    public void noOfLegs() {
        return 0;
    }

    public static void main(String args[]) {
        MammalInt m = new MammalInt();
        m.eat();
        m.travel();
    }
}