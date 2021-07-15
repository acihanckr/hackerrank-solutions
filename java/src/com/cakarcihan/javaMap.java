package com.cakarcihan;

 {
}
//Complete this code or write your own from scratch
import java.util.*;
        import java.io.*;

public class javaMap{
    public static void main(String []argh)
    {
        Scanner scan = new Scanner(System.in);
        int n=scan.nextInt();
        scan.nextLine();
        Map<String, Long> phoneBook = new HashMap<>(); // added
        for(int i=0;i<n;i++)
        {
            String name=scan.nextLine();
            long phone=scan.nextInt();
            scan.nextLine()
            phoneBook.put(name, phone); // added

        }
        while(scan.hasNext())
        {
            String s=scan.nextLine();
            // start
            if (phoneBook.get(s)==null) System.out.println("Not found");
            else System.out.println(s+ "=" + phoneBook.get(s));
            // end
        }
    }
}

