package com.cakarcihan;

import java.util.Scanner;

public class javaStringReverse {
    public static void main(String []args){

    Scanner sc=new Scanner(System.in);
    String A=sc.next();
    // start
    String B = new StringBuilder(A).reverse().toString();
        if (A.equals(B)){
        System.out.println("Yes");
    } else {
        System.out.println("No");
    }

    // end

    }
}
