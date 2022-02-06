/* Implementing Array, Linkedlist, Hashset & HashMap */

import java.util.*; //Importing all the classes and interfaces that are part of the util package

public class CollectionsDemo {
    public static void main(String[] args) {
        // Array List
        List a1 = new ArrayList();
        a1.add("Zara");
        a1.add("Mahnaz");
        a1.add("Ayan");
        System.out.println(" Array Elements");
        System.out.print("\t", a1);
        
        // Linkedlist
        List l1 = new LinkedList();
        l1.add("Zara");
        l1.add("Mahnaz");
        l1.add("Ayan");
        System.out.println();
        System.out.println(" LinkedList Elements");
        System.out.print("\t", l1);

        // Hashset
        Set s1 = new HashSet();
        s1.add("Zara");
        s1.add("Mahnaz");
        s1.add("Ayan");
        System.out.println();
        System.out.println(" HashSet Elements");
        System.out.print("\t", s1);

        // HashMap
        Map m1 = new HashMap();
        m1.put("Zara", "8"); // put is used instead of add in  LinkedList, Array and HashSet
        m1.put("Mahnaz", "31");
        m1.put("Ayan", "12");
        m1.put("Daisy", "14");
        System.out.println();
        System.out.println(" HashMap Elemets");
        System.out.print("\t", m1);
    }
}