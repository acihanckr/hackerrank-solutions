package com.cakarcihan;

import java.util.*;
import java.math.*;

public class javaBigInteger {

    public static void main(String[] args) {
        // start
        Scanner scan = new Scanner(System.in);
        BigInteger a = new BigInteger(scan.nextLine());
        BigInteger b = new BigInteger(scan.nextLine());
        System.out.println(a.add(b));
        System.out.println(a.multiply(b));
        // end
    }
}