package com.cakarcihan;

import java.util.Scanner;

public class javaStringsIntroduction {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        // start
        System.out.println(A.length() + B.length());
        System.out.println(A.compareTo(B)>01? "Yes" : "No");
        System.out.println(A.substring(0, 1).toUpperCase()+A.substring(1)+" "+B.substring(0, 1).toUpperCase()+B.substring(1));
        // end
    }
}
